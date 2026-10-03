# maw-js Architecture

Multi-Agent Workflow (maw) is a CLI and server for orchestrating AI agents across machines via tmux. Built on Bun (TypeScript runtime), engine-agnostic (Claude Code, Codex, Aider, OpenCode), and federated over HTTP with HMAC-SHA256 signing.

## Directory Structure

**Top level** (`src/`, `packages/`, `test/`, `docs/`):

- `src/cli.ts` — main entry point; sets up instance presets, loads plugins, dispatches commands
- `src/api/` — Elysia HTTP server with 40+ routers (sessions, federation, config, teams, plugins, etc.)
- `src/commands/` — CLI plugin dispatchers; `plugins/` subdirs hold 60+ bundled plugins
- `src/core/` — core abstractions: tmux transport, fleet mgmt, runtime, config, gates
- `src/engine/` — `MawEngine` class: WebSocket broadcast loop, session/status polling, feed events
- `src/transports/` — tmux, HTTP, SSH, Zenoh/Scout (peer-to-peer discovery), relay protocols
- `src/plugin/` — plugin loader, registry, manifest validation, lifecycle hooks
- `src/lib/` — shared utilities: feed events, schemas, orbit manifests, sparklines
- `packages/sdk/` — `@maw-js/sdk` workspace package; public API for plugins
- `packages/maw-gateway/` — Rust gateway binary (Phase 3); reverse proxy with `/api/health` native route
- `test/` — 800+ test files split into `isolated/`, `cli/`, `integration/`, `spec/`, federation tests
- `docs/` — federation, fleet, plugins, teams, retrospectives, RFCs

**Entry points**:
- `src/cli.ts` — CLI: parses commands, loads plugins, dispatches via `dispatchCommand()`
- `src/core/server.ts` — HTTP server: `maw serve` entry; starts Bun backend on internal port, Rust gateway on public port (if enabled)
- `maw-gateway` (Rust) — optional public gateway; proxies to Bun backend (:3457 by default), exposes `/api/health` natively
- `ecosystem.config.cjs` — PM2 config for production: runs `server.ts` + optional `fleet restore --all` on boot

## Core Abstractions

### 1. **MawEngine** (`src/engine/index.ts`)
Central WebSocket coordinator. Manages:
- 5 background intervals (capture, sessions, previews, status, teams, peers, crash checks)
- Session cache (tmux list) refreshed on connect/disconnect
- Feed buffer (last N events broadcasted on new client connect)
- Handlers map for WS message routing
- Transport router for remote peer message delivery

Entry: `handleOpen()` / `handleMessage()` / `handleClose()`.

### 2. **Plugin System** (`src/plugin/types.ts`, `src/commands/plugins/*/`)
Two-phase loader:
1. **Compile-time**: bundled plugins symlinked to `~/.maw/plugins/` on first run (`plugin-bootstrap.ts`)
2. **Runtime**: `scanCommands()` discovers plugins from `~/.maw/plugins/` + user plugins

Each plugin has `plugin.json` manifest declaring:
- `cli` — CLI command + flags
- `api` — HTTP GET/POST path auto-mounted at `/api/plugins/<name>`
- `hooks` — lifecycle: gate, filter, on, late, wake, sleep, serve, transport
- `wasm`/`entry` — WASM or TypeScript handler; TS gets full maw-js access
- `cron` — optional background schedule

Invocation: `invokePlugin(manifest, { source, args, flags })` → `InvokeResult`.
60+ plugins bundled under `src/commands/plugins/`: channel, cli, config, federation, fleet, oracle, pane, plugin, scheduler, session, split, swarm, team, tile, tmux, transport, etc.

### 3. **Tmux Transport** (`src/core/transport/tmux.ts`, `tmux-*.ts`)
Abstracts tmux pane/window/session as observable targets. Key types:
- `TmuxSession`, `TmuxWindow`, `TmuxPane` — read-only session hierarchy
- `Tmux` class — queries (listAll, listSessions, findPane), commands (sendKeys, splitWindow, selectWindow)
- `withPaneLock()`, `splitWindowLocked()` — prevents concurrent modifications
- `tagPane()` — writes metadata to pane border (oracle name, transport tags)

Default instance: `tmux` singleton. Used by:
- Engine intervals: 50ms capture, 5s session poll
- Commands: wake, sleep, bring, split, tile
- Transport router: deliver remote messages to target tmux window

### 4. **Federation & Transport** (`src/transports/`, `src/core/transport/`)
Multi-hop agent messaging across machines.

**Transports**:
- `tmux.ts` — local window/pane queries + send-keys
- `http.ts` — HTTP client for REST relay
- `scout.ts` — Zenoh Scout ZeroMQ discovery + subscription protocol
- `zenoh.ts` — Zenoh pub-sub bridge (optional, high-throughput)

**Auth**: HMAC-SHA256 over `METHOD:PATH:TIMESTAMP:SHA256(BODY)` (v2); v1 omits body hash. Configured in `maw.config.json`:
```json
{
  "node": "oracle-world",
  "federationToken": "shared-secret-min-16-chars",
  "namedPeers": [{ "name": "white", "url": "http://10.20.0.7:3456" }]
}
```

**Message routing** (`src/engine/index.ts` line 68-86):
1. Remote `maw hey` reaches `/api/peer/exec` endpoint
2. Engine's transport router routes to local tmux pane
3. Delivery via `sendKeys()`

### 5. **Fleet & Workspace** (`src/core/fleet/`, `src/commands/plugins/team/`)
Multi-agent coordination.

**Fleet**: cluster-wide agent registry, health tracking, worktree layout, nicknames. Stored in `~/.maw/fleet-config.yaml`.

**Teams**: Charter-driven (YAML) multi-agent workspaces with:
- Member list + engine assignments
- Isolated worktrees per member
- Shared prompts delivered via `send-keys`
- Lifecycle: `team up`, `team down`, `team reassign`

**Worktrees**: Git worktrees per team member for parallel task isolation. Tracked in fleet manifest.

### 6. **Configuration** (`src/config.ts`, `maw.config.example.json`)
Central config at `~/.config/maw/maw.config.json` (XDG mode) or `~/.maw/maw.config.json` (legacy).

**Keys**:
- `host` / `port` — bind address + port (default 3456)
- `ghqRoot` — ghq clone root (e.g., `~/Code/github.com`)
- `oracleUrl` — Claude Code instance URL (for Claude-like engine detection)
- `commands` — oracle/engine command templates (default, `*-oracle`, `codex-*`)
- `sessions` — preset session → window mappings
- `env` — environment variables (CLAUDE_CODE_OAUTH_TOKEN, etc.)
- `federation.*` — federation token, named peers, discovery settings
- `autoRestart` — auto-recover crashed agents

### 7. **HTTP API** (`src/api/index.ts`, 40+ route files)
Elysia server on `:3456` (or gateway port). Routes:
- `/api/sessions` — session list, capture, create
- `/api/feed` — event stream (WebSocket at `/ws`)
- `/api/config` — node config + agent map
- `/api/fleet-config` — cluster membership
- `/api/federation/status` — peer connectivity
- `/api/peer/exec` — signed remote command relay
- `/api/plugins/<name>` — auto-mounted plugin APIs
- `/api/team` — team mgmt
- `/api/ask` — message dispatch
- `/api/costs` — token usage aggregation
- `/api/consent` — permission gates
- Static routes: `/` → `maw-ui` React dashboard (served from `~/.maw/ui/dist/` or built inline)

Auth layer:
- `federationAuth` — validates HMAC-SHA256 for cross-node calls
- `fromSigningAuth` — ed25519 signature for peer continuity (Phase 4, #804)
- `trustLoopback` flag — allow unsigned localhost (development)

### 8. **Plugins** (60+ bundled)
**Core sample**:
- `tmux` — pane/window/session operations (split, tile, select)
- `federation` — peer discovery, peer exec, handshake
- `team` — charter loading, member spawn, worktree isolation
- `session` — list, select, switch, watch
- `oracle` — wake oracle, query status, send prompts
- `plugin` — install, list, enable/disable, registry fetch
- `wake` — lifecycle: pre-wake hooks, engine detection, snapshot restore
- `sleep` — graceful shutdown, cleanup

**Lifecycle hooks**:
- `gate` — early veto on events
- `filter` — transform events before broadcast
- `on` — react to events (synchronous)
- `late` — cleanup (last-to-run)
- `wake` / `sleep` / `serve` / `transport` — lifecycle handlers (#1576)

## Runtime & Dependencies

**Runtime**: [Bun 1.3+](https://bun.sh) (TypeScript, ESM, native Bun.serve, built-in SQLite)
- `bun build src/cli.ts --outfile dist/maw --target=bun --minify` → standalone binary
- No Node.js required; Bun brings its own libc, OpenSSL, WebKit

**Key dependencies**:
- **Elysia** — HTTP server with built-in validation, OpenAPI docs
- **@maw-js/sdk** — plugin API + types
- **@eclipse-zenoh/zenoh-ts** — optional high-throughput pub-sub (Zenoh)
- **mqtt** — optional MQTT relay (legacy, WebSocket replaces)
- **@xterm/xterm** — terminal emulation (UI)
- **react 19 + zustand** — UI state + components
- **three.js** — 3D visualization for federation mesh (maw-ui)
- **TypeScript 6.0**, **Vite** — build tools

**Process supervision**: PM2 (`ecosystem.config.cjs`)
- App: `bun src/core/server.ts` (HTTP server)
- Boot: `bun fleet restore --all` (auto-wake oracles on startup)
- Max restarts: 5; restart delay: 3s (fail-fast)

## Deployment

**Single-host** (typical dev/test):
```bash
bun install
maw serve                    # port 3456, Bun only
maw ui install && maw ui     # download React dashboard
```

**Multi-host federation**:
1. Start servers on each host: `maw serve --port 3456`
2. Configure `namedPeers` in `maw.config.json` (shared secret token)
3. Run `maw hey <peer>:<oracle> "msg"` for cross-node messaging
4. Dashboard: `maw ui <peer-name>` points lens at remote host

**Docker** (`docker/Dockerfile`, `docker/entrypoint.sh`):
```bash
docker compose -f docker/compose.yml up
# Entrypoint bootstraps peers.json, runs `maw init --non-interactive`, then exec "$@"
```

**Gateway (Phase 3 Rust)** (`packages/maw-gateway/GATEWAY_CONTRACT.md`):
- TypeScript CLI orchestrates Rust binary on public port (:3456)
- Rust proxies to Bun backend (:3457)
- Rust owns `/api/health`, Bun owns everything else
- Startup: TypeScript reads `maw-gateway serve --port 3456 --backend 3457`
- Readiness: waits for stdout line `listening on :3456`
- Benefits: lower latency for federation, native TLS, tuning

**PM2 production**:
```bash
pm2 start ecosystem.config.cjs
maw update                   # atomic: try install, fallback to rollback binary
```

## Test Coverage (800+ files)

**Suites**:
- `test/isolated/` — unit tests with mocked imports; Bun test + `mock.module()`
- `test/cli/` — CLI dispatch, command parsing, flags
- `test/integration/` — full server, federation handshake, tmux operations
- `test/spec/` — JSON fixture-driven portable specs (for maw-rs port)
- `test/fedtest/` — multi-container federation (Docker Compose)
- `test/security/` — auth, HMAC, peer signing

**CI**: GitHub Actions (`.github/workflows/ci.yml`, `federation-docker.yml`)
- Unit + isolated tests on every PR
- Docker federation smoke test on transport changes
- Coverage gap analysis (600+ LOC untested → report)

## Non-Developer Summary

maw is a CLI that wakes AI agents in tmux windows on one or many computers. You give it commands like `maw wake neo --split` (open oracle side-by-side), `maw hey neo "what are you working on?"` (send a question), and `maw peek neo` (see their screen). The core is a Bun server that polls tmux, broadcasts session state over WebSocket to a React browser dashboard, and relays messages between agents on different machines using signed HTTPS requests. Plugins extend the CLI; a charter YAML can define teams of agents with isolated work folders. Deploy as a single binary, Docker container, or across a cluster with shared-secret federation.

## File Paths Cited

- `src/cli.ts` — entry point, plugin bootstrap
- `src/core/server.ts` — HTTP server startup
- `src/engine/index.ts` — `MawEngine` class, WebSocket coordinator
- `src/api/index.ts` — Elysia router with 40+ subroutes
- `src/plugin/types.ts` — plugin manifest, invoke contract
- `src/commands/plugins/` — 60+ bundled plugins
- `src/core/transport/tmux.ts` — tmux abstraction
- `src/transports/` — federation transports (HTTP, Scout, Zenoh)
- `src/config.ts` — config loading + schema
- `packages/maw-gateway/GATEWAY_CONTRACT.md` — Rust gateway interface
- `packages/sdk/` — public plugin SDK
- `ecosystem.config.cjs` — PM2 production config
- `docker/Dockerfile`, `docker/entrypoint.sh` — container deployment
- `maw.config.example.json` — config template
- `package.json` — workspace + Bun build script
- `llms.txt` — architecture overview for AI readers
- `README.md` — install, CLI reference, federation setup
