# maw-js Code Snippets

## CLI Entry and Command Dispatch

### CLI Entry Point
**File:** `src/cli.ts` (lines 1-65)

```typescript
import { dispatchCommand } from "./cli/dispatch";
import { scanCommands } from "./cli/command-registry";

async function main(): Promise<void> {
  const cmd = args[0]?.toLowerCase();
  
  await scanCommands(pluginDir, "user");
  await dispatchCommand(cmd, args);
}

main().catch((e: unknown) => handleTopLevelError(e, args));
```

CLI entry establishes plugin loading, command dispatch, and error handling as the backbone of the system.

### Command Dispatch Routing
**File:** `src/cli/dispatch.ts` (lines 25-53)

```typescript
export async function dispatchCommand(cmd: string, args: string[]): Promise<void> {
  const handled =
    (await routeComm(cmd, args)) ||
    (await routeTools(cmd, args));
  if (handled) return;

  const aliasResult = resolveTopAlias(args);
  if (aliasResult) {
    if (aliasResult.kind === "direct") {
      await invokeDirectHandler(aliasResult.handler, aliasResult.argv);
      return;
    }
    args.splice(0, args.length, ...aliasResult.argv);
  }

  const pluginMatch = matchCommand(args);
  if (pluginMatch) {
    await executeCommand(pluginMatch.desc, pluginMatch.remaining);
    return;
  }

  await dispatchPluginRegistry(cmd, args);
}
```

Dispatch walks a ladder: comm routes → tools → aliases → plugin registry.

### Top-Level Aliases (Direct Handlers)
**File:** `src/cli/top-aliases.ts` (lines 66-101)

```typescript
export const TOP_ALIASES: Record<string, string[] | DirectHandler> = {
  a: ["attach"],
  t: ["team"],
  layout: { kind: "direct", handler: "cmdLayout" },
  bring: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdBring" },
  wake: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdWake" },
  awake: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdAwake" },
  work: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdWake", argv: ["--work", "."] },
  new: { kind: "direct", handler: "./cmd-new:cmdNew" },
  wtf: { kind: "direct", handler: "../commands/plugins/team/team-wtf:cmdTeamWtf" },
};
```

Top-level verbs (wake, bring, a, t) bypass plugin registry and map to direct static handlers.

---

## Message Sending Between Agents

### Hey/Send/Notify Commands
**File:** `src/cli/route-comm.ts` (lines 39-134)

```typescript
export async function routeComm(cmd: string, args: string[]): Promise<boolean> {
  if (cmd === "hey" || cmd === "send" || cmd === "notify") {
    const isNotify = cmd === "notify";
    let inboxOnly = isNotify;  // notify always inbox-only
    let approve = false;
    let target: string | undefined;
    const msgArgs: string[] = [];

    for (let i = 0; i < rest.length; i += 1) {
      if (arg === "--inbox") { inboxOnly = true; continue; }
      if (arg === "--approve") { approve = true; continue; }
      if (arg === "--trust") { trust = true; continue; }
      if (!target) target = arg;
      else msgArgs.push(arg);
    }

    await cmdSend(target, msgArgs.join(" "), force, { approve, trust, inboxOnly, ...(from ? { from } : {}) });
    return true;
  }
  return false;
}
```

Routes `maw hey`, `maw send` (aliases), and `maw notify` to unified delivery—pane-inject vs inbox-only.

### Resolve Oracle Pane (Multi-Pane Routing Fix)
**File:** `src/commands/shared/comm-send.ts` (lines 46-78)

```typescript
export async function resolveOraclePane(
  target: string,
  deps: { tmuxRun?: (...args: string[]) => Promise<string> } = {},
): Promise<string> {
  if (/\.[0-9]+$/.test(target)) return target;

  const run = deps.tmuxRun ?? ((...args: string[]) => new Tmux().run(...args));
  const raw = await run("list-panes", "-t", target, "-F", "#{pane_index} #{pane_current_command}");
  const lines = raw.split("\n").map((l: string) => l.trim()).filter(Boolean);
  
  const agentIndexes: number[] = [];
  for (const line of lines) {
    const spaceIdx = line.indexOf(" ");
    if (spaceIdx < 0) continue;
    const idx = parseInt(line.slice(0, spaceIdx), 10);
    const cmd = line.slice(spaceIdx + 1);
    if (Number.isFinite(idx) && isAgent(cmd)) {
      agentIndexes.push(idx);
    }
  }
  if (agentIndexes.length === 0) return target;
  return `${target}.${Math.min(...agentIndexes)}`;
}
```

Routes messages to the first agent pane (lowest index) when team agents spawn alongside the oracle.

### Sender Identity Resolution
**File:** `src/commands/shared/comm-send.ts` (lines 106-118)

```typescript
export interface SenderIdentity {
  /** Human-facing node name used in visible `[node:oracle]` message prefixes. */
  node: string;
  /** Human-facing oracle/session name. */
  oracle: string;
  /** `node:oracle`, the form operators type with `--from` / `MAW_SENDER`. */
  display: string;
  /** `oracle:node`, the existing v3 from-signing wire form. */
  wireFrom: string | "auto";
  /** Back-compat name for message log rows. */
  senderName: string;
  source: "auto" | "flag" | "env";
}
```

Signed identity envelope for cross-node messages; resolves from env, flag, or tmux session.

---

## Agent/Worker Spawning

### Wake Command (Agent Spawn Entry)
**File:** `src/cli/top-aliases.ts` (lines 90-94)

```typescript
// Direct-handler form — cmdWake is in core (src/commands/shared/wake-cmd.ts)
wake: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdWake" },
awake: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdAwake" },
work: { kind: "direct", handler: "../commands/shared/wake-cmd:cmdWake", argv: ["--work", "."] },
```

Wake and awake are direct handlers that bypass plugin dispatch; resolve to cmdWake in core.

### Spawn Teammate Pane (Multi-Agent Layout)
**File:** `src/commands/plugins/tmux/layout-manager.ts` (lines 140-170)

```typescript
export async function spawnTeammatePane(
  agentName: string,
  command: string,
  opts: { colorIndex: number; leaderPane?: string } = { colorIndex: 0 },
): Promise<SpawnResult> {
  const { withPaneLock } = await import("../../../sdk");
  const anchor = opts.leaderPane || process.env.TMUX_PANE || "";
  const color = nextAgentColor(opts.colorIndex);

  const wrapped = `${command.replace(/'/g, "'\\''")}; printf "\\e[?1049l"; clear; exec zsh -li`;

  let paneId = "";
  await withPaneLock(async () => {
    paneId = (await hostExec(
      `tmux split-window ${targetFlag}-h -P -F '#{pane_id}' '${wrapped}'`,
    )).trim();
  });

  const window = await getWindowTarget();
  const panes = await listPaneIds(window);
  const isFirst = panes.length <= 2;

  if (paneId) await stylePaneBorder(paneId, agentName, color);
  await enableBorderStatus(window);

  return { paneId, color, isFirst };
}
```

Spawns a new agent pane via `tmux split-window` with wrapping logic for TUI cleanup; returns pane ID and color assignment.

### Apply Team Layout
**File:** `src/commands/plugins/tmux/layout-manager.ts` (lines 31-45)

```typescript
export async function applyTeamLayout(
  windowTarget: string,
  leaderPane: string,
  leaderPct = 30,
): Promise<void> {
  await hostExec(`tmux select-layout -t '${windowTarget}' main-vertical`);
  await hostExec(`tmux resize-pane -t '${leaderPane}' -x ${leaderPct}%`);
}

export async function rebalanceAfterSpawn(
  windowTarget: string,
  leaderPane: string,
): Promise<void> {
  await applyTeamLayout(windowTarget, leaderPane);
}
```

Applies main-vertical layout and resizes leader pane to 30% width after teammate spawn.

### Wake Command Implementation (Core)
**File:** `src/commands/shared/wake-cmd.ts` (lines 1-5, 93-98)

```typescript
import { hostExec, tmux, restoreTabOrder, takeSnapshot, getPaneInfos, isAgentCommand } from "../../sdk";
// ... config and fleet helpers ...

async function respawnPaneWithCommand(target: string, command: string): Promise<boolean> {
  const runner = (tmux as unknown as { run?: (subcommand: string, ...args: Array<string | number>) => Promise<string> }).run;
  if (typeof runner !== "function") return false;
  await runner.call(tmux, "respawn-pane", "-k", "-t", target, command);
  return true;
}
```

Core wake logic uses tmux respawn-pane to launch agents; exports fleet management, snapshot restore, and concurrency checks.

---

## HTTP/API Server Routes

### API Router Setup
**File:** `src/api/index.ts` (lines 35-78)

```typescript
export const api = new Elysia({ prefix: "/api" })
  .use(cors())
  .use(federationAuth)
  .use(fromSigningAuth)
  .onAfterHandle(({ set }) => {
    set.headers["Access-Control-Allow-Private-Network"] = "true";
  })
  .use(swagger({ path: "/docs", ... }))
  .use(sessionsApi)
  .use(feedApi)
  .use(teamsApi)
  .use(configApi)
  .use(fleetApi)
  .use(asksApi)
  .use(oracleApi)
  // ... 15+ more route modules ...
  .use(requestReplyApi);

const directRoutes = new Set(api.routes.map(r => `${r.method}|${r.path}`));

// Auto-mount plugin API surfaces from manifests
const bundledPlugins = discoverPackages();
for (const p of bundledPlugins) {
  if (!p.manifest.api) continue;
  const apiPath = p.manifest.api.path;
  const { methods } = p.manifest.api;
  // Mount plugin routes with collision detection
}
```

Elysia app with CORS, federation auth, swagger docs; auto-mounts plugin APIs from manifests with collision detection.

### Sessions API Route (GET /sessions)
**File:** `src/api/sessions.ts` (lines 224-241)

```typescript
api.get("/sessions", async ({ query, set }) => {
  let local: Session[];
  try {
    local = await d.listSessions();
  } catch (error) {
    set.status = 503;
    return sessionsUnavailablePayload(error);
  }
  if (query.local === "true") {
    return dedupeSessionWindows(local.map(s => ({ ...s, source: "local" })));
  }
  const aggregated = await d.getAggregatedSessions(local);
  return dedupeSessionWindows(aggregated);
}, {
  query: t.Object({ local: t.Optional(t.String()) }),
});
```

Lists local or federated tmux sessions; dedupes windows by name and returns aggregated view.

### Send API Route (POST /send)
**File:** `src/api/sessions.ts` (lines 319-~500)

```typescript
api.post("/send", async ({ body, request, set }) => {
  const { target, message, ... } = body;
  
  const resolved = d.resolveTarget(target, config, local);
  
  if (resolved?.type === "local" || resolved?.type === "self-node") {
    const live = await verifyDeliverableTarget(resolved.target);
    if (!live.ok) return queueOrFail(resolved.target, live.reason);
    
    const guard = await checkBusyGuard(target);
    if (guard.busy && !inboxOnly) {
      queueForDispatch({ from: messageFrom, to: target, target: resolved.target, message });
      return queueOrFail(resolved.target, `target busy; queued for auto-delivery`);
    }
    
    await d.sendKeys(resolved.target, message);
    const inbox = await writeInboundInbox(resolved.target);
    const state: "delivered" | "queued" = "delivered";
    
    return { ok: true, target: resolved.target, text, source: "local", ... };
  }
  // Cross-node fallback ...
}, {
  body: SendBody,
});
```

Unified send handler: resolves target, checks busy guard, pane-injects with Enter, writes inbox, emits lifecycle event.

### Capture API Route (GET /capture)
**File:** `src/api/sessions.ts` (lines 262-280)

```typescript
api.get("/capture", async ({ query, set }) => {
  const target = query.target;
  if (!target) { set.status = 400; return { error: "target required" }; }
  try {
    const sessions = await d.listSessions();
    const resolved = resolveCapture(target, sessions, d);
    return { content: await d.capture(resolved) };
  } catch (e: any) {
    // Enrich error with window indices + base-index hint
    set.status = 404;
    return { error: `target not found: ${target}`, ... };
  }
});
```

Reads pane content via `tmux capture-pane`; validates target exists and enriches errors with window index help.

### Wake API Route (POST /wake)
**File:** `src/api/sessions.ts` (line 793)

```typescript
api.post("/wake", async ({ body, set }) => {
  // ... wake target, check concurrency, restore from snapshot ...
  const result = await d.cmdWake(target, { noAttach: true, task: body.task });
  return { ok: true, ... };
}, {
  body: WakeBody,
});
```

Wakes an agent session via HTTP; used by federation peers to spawn/restore agents.

---

## Plugin Example: Oracle Plugin

### Plugin Definition (Manifest)
**File:** `src/commands/plugins/oracle/plugin.ts` (lines 1-32)

```typescript
import { definePlugin } from "maw-js/sdk";

export default definePlugin({
  "name": "oracle",
  "version": "1.0.0",
  "entry": "./index.ts",
  "sdk": "^1.0.0",
  "description": "Oracle management — list, scan, fleet, about",
  "cli": {
    "command": "oracle",
    "aliases": ["oracles"],
    "help": "maw oracle [ls|scan|fleet|about <name>|search <query>] [--json]",
    "flags": {
      "--json": "boolean",
      "--awake": "boolean",
      "--org": "string",
      "--path": "boolean",
      "--scan": "boolean",
      "--stale": "boolean",
      "--sort-by": "string"
    }
  },
  "api": {
    "path": "/api/oracle",
    "methods": ["GET"]
  },
  "weight": 0
} as const);
```

Plugin manifest declares CLI command, flags, API route(s), and metadata; auto-mounted by discovery.

### Plugin Handler (Handler Export)
**File:** `src/commands/plugins/oracle/index.ts` (lines 41-90)

```typescript
export const command = {
  name: ["oracle", "oracles"],
  description: "Oracle management — list, scan, about, prune, register",
};

export function createOracleHandler(overrides: Partial<OracleCommandDeps> = {}) {
  return async function handler(ctx: InvokeContext): Promise<InvokeResult> {
    const logs: string[] = [];
    const origLog = console.log;
    console.log = (...a: any[]) => {
      if (ctx.writer) ctx.writer(...a);
      else logs.push(a.map(String).join(" "));
    };
    
    try {
      if (ctx.source === "cli") {
        const subcmd = (ctx.args as string[])[0]?.toLowerCase();
        if (!subcmd || subcmd === "ls" || subcmd === "list") {
          const flags = parseFlags(args, LS_FLAGS, 1);
          await commands.cmdOracleList({ awake: flags["--awake"], ... });
        } else if (subcmd === "scan") { ... }
      }
      return { ok: true, output: logs.join("\n") || undefined };
    } catch (e: any) {
      return { ok: false, error: e.message, output: logs.join("\n") || undefined };
    } finally {
      console.log = origLog;
    }
  };
}
```

Handler wraps console I/O, dispatches by subcommand (ls/scan/about/etc.), returns structured InvokeResult with ok/error/output.

### Plugin CLI Subcommands
**File:** `src/commands/plugins/oracle/index.ts` (lines 74-150)

```typescript
if (ctx.source === "cli") {
  const args = ctx.args as string[];
  const subcmd = args[0]?.toLowerCase();
  
  if (!subcmd || subcmd === "ls" || subcmd === "list") {
    const flags = parseFlags(args, LS_FLAGS, 1);
    await commands.cmdOracleList({ awake: flags["--awake"], org: flags["--org"], ... });
  } else if (subcmd === "scan") {
    const flags = parseFlags(args, { "--json": Boolean, "--force": Boolean, ... }, 1);
    if (flags["--stale"]) {
      await commands.cmdOracleScanStale({ json: flags["--json"], all: flags["--all"] });
    } else {
      await commands.cmdOracleScan({ json: flags["--json"], force: flags["--force"], ... });
    }
  } else if (subcmd === "prune") {
    const flags = parseFlags(args, { "--stale": Boolean, "--force": Boolean }, 1);
    await commands.cmdOraclePrune({ stale: flags["--stale"], force: flags["--force"] });
  } else if (subcmd === "search") {
    const query = args[1];
    await commands.cmdOracleSearch(query, { json: flags["--json"], awake: flags["--awake"] });
  }
}
```

Plugin subcommands: ls (list), scan (discover), prune (cleanup), search (fuzzy), register (new); each has own flags.

### Transport Plugin (Simpler Example)
**File:** `src/commands/plugins/transport/plugin.ts` (lines 1-23)

```typescript
import { definePlugin } from "maw-js/sdk";

export default definePlugin({
  "name": "transport",
  "version": "1.0.0",
  "entry": "./index.ts",
  "sdk": "^1.0.0",
  "description": "Transport layer status and diagnostics",
  "cli": {
    "command": "transport",
    "aliases": ["tp"],
    "help": "maw transport [status]"
  },
  "api": {
    "path": "/api/transport/status",
    "methods": ["GET"]
  },
  "weight": 10
} as const);
```

Minimal plugin: single CLI command + single GET route; shows the pattern for lightweight diagnostics plugins.

