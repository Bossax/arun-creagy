# maw-js Quick Reference

**maw** is a CLI for running multiple AI agents (oracles) across machines. Wake agents in tmux windows, send them tasks, watch their screens, and see costs—all from one terminal. Engine-agnostic: drives Claude Code, Codex, Aider, OpenCode.

---

## Install

**One-liner:**
```bash
curl -fsSL https://raw.githubusercontent.com/Soul-Brews-Studio/maw-js/main/install.sh | bash
```

**Manual:**
```bash
bun add -g github:Soul-Brews-Studio/maw-js          # persistent binary
bunx --bun github:Soul-Brews-Studio/maw-js maw ...  # zero-install, one-shot
```

**From source:**
```bash
ghq get Soul-Brews-Studio/maw-js && cd "$(ghq root)/github.com/Soul-Brews-Studio/maw-js"
bun install && bun link
```

**Versioning:** CalVer — `v{yy}.{m}.{d}[-alpha.{HHMM}]` (e.g., `v26.6.14-alpha.2110`).

**Recovery:** If `maw: command not found`, run `bunx -p github:Soul-Brews-Studio/maw-js maw doctor`.

---

## Config

**File:** `~/.config/maw/maw.config.json` (XDG: `$XDG_CONFIG_HOME/maw/maw.config.json` with `MAW_XDG=1`)

**Example:**
```json
{
  "host": "local",
  "port": 3456,
  "ghqRoot": "/home/nat/Code/github.com",
  "oracleUrl": "http://localhost:47779",
  "federationToken": "shared-secret-min-16-chars",
  "namedPeers": [
    { "name": "white", "url": "http://10.20.0.7:3456" }
  ],
  "env": {
    "CLAUDE_CODE_OAUTH_TOKEN": "<your-token>"
  },
  "commands": {
    "default": "claude --dangerously-skip-permissions --continue",
    "codex-*": "codex --dangerously-auto-approve --search"
  },
  "sessions": {
    "nexus": "01-oracles"
  }
}
```

**Key fields:**
- `host` — node identity (e.g., "oracle-world")
- `port` — maw API server port (default 3456)
- `ghqRoot` — where repos are cloned (ghq root)
- `oracleUrl` — Claude Code socket URL (default localhost:47779)
- `federationToken` — HMAC-SHA256 signing key for cross-machine messages (min 16 chars)
- `namedPeers` — remote maw servers for federation
- `commands` — engine selection (default engine, engine patterns)
- `sessions` — default session assignments

**Environment variables:**
- `MAW_XDG=1` — use XDG Base Directory spec paths
- `MAW_HOME` — override config/state root (legacy, use XDG instead)
- `MAW_UI_DIR` — override UI dist location
- `MAW_PLUGINS_DIR` — override plugin directory
- `MAW_CLI=1` — internal; set by CLI entry point

---

## Commands (Core & Standard)

**Core commands** (weight < 10):

| Command | Purpose | Example |
|---------|---------|---------|
| `maw wake <oracle>` | Wake or reuse an oracle, auto-cloning repos | `maw wake neo` |
| `maw ls` | List local live sessions (compact default) | `maw ls -v` (verbose) |
| `maw bring <oracle>` | Bring oracle here (thin alias: `wake --split`) | `maw bring neo --to work:review` |
| `maw hey <oracle> <msg>` | Send immediate message (pane injection or queue) | `maw hey neo "done?"` |
| `maw sleep <oracle>` | Gracefully stop an oracle | `maw sleep neo` |
| `maw tmux <subcommand>` | tmux pane/session tools (peek, attach, kill, zoom) | `maw tmux peek neo` |
| `maw new <name>` | Create plain tmux workspace (no /awaken) | `maw new project-room` |
| `maw snapshots list` | Browse wake recovery snapshots | `maw snapshots show <id>` |
| `maw preflight` | Version, plugins, dead agents, config check | `maw preflight --fix` |

**Standard commands** (weight 10–49):

| Command | Purpose | Example |
|---------|---------|---------|
| `maw oracle ls` | List oracles across fleet | `maw oracle scan` |
| `maw oracle scan` | Discover oracles on this node | `maw oracle scan --json` |
| `maw oracle fleet` | Show constellation (lineage + status) | `maw oracle about <name>` |
| `maw bud <name>` | Spawn new oracle from template or parent | `maw bud fusion --from neo` |
| `maw team up <team>` | Spawn charter-driven team from YAML | `maw team up my-team --dry-run` |
| `maw team down <team>` | Graceful team shutdown | `maw team down my-team` |
| `maw team bring <team>` | Add oracles to workspace | `maw team create my-team` |
| `maw federation status` | Peer connectivity + latency | `maw fed sync --dry-run` |
| `maw plugin ls` | List installed plugins (tiered) | `maw plugin enable <name>` |
| `maw plugin install <name>` | Install from registry or peer | `maw plugin install fck` |
| `maw ui` | Open federation lens (React SPA) | `maw ui white` (remote lens) |
| `maw ui install` | Download latest maw-ui | `maw ui install --version v1.15.0` |
| `maw config show` | Show loaded config | `maw config validate` |
| `maw fleet ls` | List fleet configs | `maw fleet health` |
| `maw serve [port]` | Start API + UI server | `maw serve 3456` |
| `maw scaffold <name>` | Create oracle repo skeleton (no wake) | `maw scaffold myproject` |
| `maw done <window>` | Auto-save worktree + clean up branch | `maw done neo:0` |

**Vendor plugins** (89+; prefix is command name):
- `maw awaken` — awakening ritual, charter-driven setup
- `maw bud` — oracle spawning (aliased at core)
- `maw doctor` — diagnostics + fixers (XDG migration, stale peers, config)
- `maw discover` — passive agent discovery (Zenoh, mDNS)
- `maw find` — search oracles by name/repo
- `maw follow` — tail oracle stdout/stderr
- `maw inbox` — read/manage message inbox
- `maw messages serve` — message ledger browser UI
- `maw ping` — check peer connectivity
- `maw fck` — command correction plugin
- `maw fleet-ui serve` — fleet dashboard
- `maw pair generate` / `maw pair <url> <code>` — ephemeral handshake for federation
- `maw peers` — federated peer search
- `maw talk-to` — persistent thread-based messaging (MCP)

---

## Top-Level Aliases

| Alias | Expands to | Purpose |
|-------|-----------|---------|
| `a` | `attach` | Attach to tmux (+ `--shell` for repo shell) |
| `kill` | `tmux kill` | Kill pane/session |
| `split` | `split` | Split pane & attach |
| `open` | `tmux open` | Show hidden panes (join-pane) |
| `close` | `tmux close` | Hide panes (break-pane, don't kill) |
| `t` | `team` | Team operations |
| `layout` | direct → `cmdLayout` | Apply tmux layout preset |
| `zoom` | `tmux zoom` | Toggle pane zoom |
| `panes` | `tmux ls --all --verbose` | List all panes across sessions |
| `tile` | `tile` | Tile current window or spawn N panes tiled |
| `b` | `bring` | Short form of bring |
| `scaffold` | `bud --scaffold-only` | Skeleton only, no wake |
| `awake` | direct → `cmdAwake` | Start oracle process (no /awaken) |
| `work` | direct → `wake --work .` | Wake using repo identity from cwd |
| `promote` | direct → `cmdPromote` | Promote command to standard plugins |
| `wtf` | direct → `cmdTeamWtf` | Team drift read-only doctor |

---

## HTTP API (Server on `:3456` default)

**v1 Core Quartet** (federation lens + external clients):

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `GET /api/config` | GET | Node identity + agents map + peers (no fan-out) |
| `GET /api/fleet-config` | GET | Raw `fleet/*.json` (includes `budded_from` lineage) |
| `GET /api/feed` | GET | Live event stream (messages, state changes) |
| `GET /api/federation/status` | GET | Peer reachability + latency |

**Federation & Relay:**

| Endpoint | Purpose |
|----------|---------|
| `POST /api/peer/exec` | Signed command relay between nodes |
| `POST /api/proxy/*` | HTTP relay for mixed-content peers |

**Agent Status & Messages:**

| Endpoint | Purpose |
|----------|---------|
| `GET /api/status` | All agent statuses + summary |
| `GET /api/status/:oracle` | Single agent status + pending count |
| `POST /api/status` | Report status change (from hooks) |
| `GET /api/queue` | All queued messages |
| `GET /api/queue/:oracle` | Pending messages for oracle |
| `POST /api/request` | Submit request → get correlationId |
| `GET /api/request/:correlationId` | Poll for reply |
| `POST /api/reply/:correlationId` | Oracle submits reply |

**Query params:**
- `/api/config?raw=1` — unmasked config (local only)
- `/api/feed?limit=200` — max 200, default from config
- `/api/feed?oracle=<name>` — filter to single oracle

**UI:**
- `GET /federation_2d.html` — maw-ui React lens (default, `maw ui install` downloads it)

---

## Fleet & Multi-Machine

**Federation** enables message passing across nodes with HMAC-SHA256 signing.

**Named peers** in config:
```json
"namedPeers": [
  { "name": "white", "url": "http://10.20.0.7:3456" },
  { "name": "clinic-nat", "url": "http://10.20.0.1:3457" }
]
```

**Canonical addressing:**
```bash
maw hey white:neo "hello"      # node:window form
maw hey white:neo:3 "hello"    # node:window:tmux-pane-number (specific pane)
maw peek white:neo             # see remote pane
maw ping                        # check peer connectivity
```

**Peer handshake** (federation setup):
```bash
maw pair generate              # get 6-char ephemeral code
maw pair <remote-url> <code>   # complete handshake on remote
```

**Federation discovery** (passive):
```bash
maw discover ls                # list discovered peers (Zenoh, mDNS)
```

**Federated listing:**
```bash
maw ls --federation            # local + peer inventory
maw ls --federation --node white  # filter by node
```

**UI:**
```bash
maw ui                         # local lens on localhost:3456/federation_2d.html
maw ui white                   # lens pointed at white's backend
maw ui --tunnel 10.20.0.16     # SSH tunnel + lens URL
```

---

## tmux Integration

**maw** manages tmux windows directly. Each oracle is a tmux session with named windows.

**Session naming:** `<numeric-slot>-<oracle-name>` (e.g., `01-neo`, `02-hermes`)

**Window targeting:**
```bash
maw wake neo:0                 # specific tmux window number
maw wake neo --split           # create new split pane
maw wake neo --tab             # create new window (tab)
maw wake neo --name myslot     # create/reuse named worktree
```

**pane commands:**
```bash
maw tmux peek neo              # read pane screen
maw tmux attach neo            # join pane to current window
maw tmux kill neo              # kill pane/session
maw tmux zoom neo              # toggle zoom on pane
maw tmux pipe <target> <cmd>   # run shell command in remote pane
maw tmux sync <targets>        # synchronize-panes across windows
maw layout <preset>            # apply tmux layout (even-horizontal, main-vertical, tiled, etc.)
```

**Layout presets:**
- `even-horizontal` — split windows horizontally
- `even-vertical` — split windows vertically
- `main-horizontal` — main pane top, others stacked below
- `main-vertical` — main pane left, others stacked right
- `tiled` — all panes equal size
- `reset` (alias) → `main-vertical`

---

## WSL & tmux

**maw** works in WSL2 with native tmux. No special setup required beyond:

1. Ensure `tmux` is installed in WSL: `sudo apt install tmux`
2. maw detects WSL automatically via `uname -o` (outputs "GNU/Linux" in WSL)
3. File paths use Unix-style; config paths follow XDG spec
4. Remote pane operations (peek, send-keys) use SSH tunnels if crossing host boundaries

**Cross-WSL federation:**
```bash
# WSL1: maw serve 3456
# WSL2: maw hey wsl1:neo "message"
#       (requires wsl1's IP in namedPeers)
```

**Performance note:** Local single-host operations (tmux attach, sendKeys) are fast. Cross-WSL federation adds HTTP round-trip latency; prefer local tmux commands when on same machine.

---

## First 10 Minutes: Start & Send Task

**1. Start the server:**
```bash
maw serve
# Running on http://localhost:3456
# UI: http://localhost:3456/federation_2d.html (if maw-ui installed)
```

**2. List existing agents:**
```bash
maw ls
# Output: compact session summary (or maw ls -v for verbose)
```

**3. Discover available oracles:**
```bash
maw oracle scan
# Output: oracles on this node (repo paths, status)
```

**4. Wake a second agent (or create one):**
```bash
# Option A: Wake existing oracle
maw wake neo --split
# Starts tmux session 01-neo, attaches side-by-side

# Option B: Clone + wake in one
maw wake https://github.com/Soul-Brews-Studio/some-oracle

# Option C: Spawn fresh oracle
maw bud myagent --root
# Creates myagent-oracle repo, wakes it
```

**5. Send it a task:**
```bash
# Immediate message (pane injection if awake, queue if busy)
maw hey neo "analyze the codebase"

# Queue-only (no pane injection)
maw hey neo "fix issue #42" --inbox

# Federated (across machines)
maw hey white:neo "status check"
```

**6. Watch the screen:**
```bash
maw peek neo
# Displays neo's pane content

maw peek neo:1
# Specific tmux window number

# Tail output continuously
maw follow neo
```

**7. Check queue/inbox:**
```bash
# See pending messages
maw ls neo         # status + pending count
maw inbox show neo # read inbox file

# Team messages
maw hey team:myteam "everyone check PR #100"
```

**8. Stop gracefully:**
```bash
maw sleep neo
# Graceful shutdown (trigger /sleep if agent supports it)

maw done neo:0
# Stronger: auto-save + clean branch
```

**9. Check federation:**
```bash
maw federation status    # peer connectivity
maw ls --federation      # all nodes' agents
```

**10. View the lens (if UI installed):**
```bash
maw ui install           # download maw-ui
# Then open http://localhost:3456/federation_2d.html
```

---

## Config Variables Cheat Sheet

| Variable | Type | Default | Purpose |
|----------|------|---------|---------|
| `node` | string | (required) | Node identity in federation |
| `port` | number | 3456 | maw API server port |
| `host` | string | "local" | Host label in config/API |
| `ghqRoot` | string | (inferred) | ghq repository root |
| `oracleUrl` | string | localhost:47779 | Claude Code socket |
| `federationToken` | string | (empty) | HMAC signing key (min 16 chars) |
| `namedPeers` | array | [] | Remote maw servers `[{name, url}]` |
| `commands.default` | string | (none) | Default engine command |
| `commands.<pattern>` | string | (none) | Engine pattern rules |
| `sessions.<name>` | string | (none) | Default session slot |
| `env.<VAR>` | string | (none) | Environment variables for agents |

---

## Plugin Ecosystem

**89+ vendored plugins** cover oracles, messaging, federation, discovery, UI, and diagnostics.

**Install/manage:**
```bash
maw plugin ls                  # list tiered plugins
maw plugin install <name>      # registry or peer source
maw plugin enable <name>       # enable disabled plugin
maw plugin disable <name>      # disable without uninstalling
maw <plugin> serve             # run plugin-owned browser/process UI
```

**Tier system:**
- **Core** (weight < 10): wake, tmux, cli, preflight
- **Standard** (10–49): oracle, federation, fleet, team, config
- **Extra** (50+): experimental, optional features

**Peer plugin discovery:**
```bash
maw peers search <query>
maw plugin install @peer <oracle-name>/<plugin>
```

---

## Troubleshooting

**maw not found after install:**
```bash
bunx -p github:Soul-Brews-Studio/maw-js maw doctor
# or reinstall: bun add -g github:Soul-Brews-Studio/maw-js
```

**Stale peer discovery:**
```bash
maw fleet doctor --stale
# Diagnoses & fixes orphaned peer entries
```

**XDG migration (new installs):**
```bash
MAW_XDG=1 maw doctor xdg --migrate
# Copies legacy ~/.config/maw to XDG spec paths
```

**Config validation:**
```bash
maw config validate
maw preflight --fix
```

**Federation handshake failure:**
```bash
# Check peer connectivity
maw ping
# Review federation status
maw federation status --verify
# Regenerate pair code if needed
maw pair generate
```

---

## Key Files & Directories

**Config:** `~/.config/maw/maw.config.json` (XDG: `$XDG_CONFIG_HOME/maw/`)

**State:** `~/.local/share/maw/` (XDG: `$XDG_DATA_HOME/maw/`)
- `agents/` — oracle processes
- `fleet/` — session configs
- `inbox/` — message files

**Plugins:** `~/.local/share/maw/plugins/` (bundled + installed registry/peer)

**UI:** `~/.local/share/maw/ui/dist/` (maw-ui React build)

**Logs:** `~/.local/state/maw/logs/` (event audit, errors)

---

## Version & Support

- **CalVer versioning:** `v26.6.14-alpha.2110` (year.month.day-alpha.HHMM)
- **Runtime:** Bun 1.3+
- **License:** BUSL-1.1 (Business Source Use License)
- **Repository:** https://github.com/Soul-Brews-Studio/maw-js
- **Issues/Docs:** https://github.com/Soul-Brews-Studio/maw-js/docs
- **UI repo:** https://github.com/Soul-Brews-Studio/maw-ui
