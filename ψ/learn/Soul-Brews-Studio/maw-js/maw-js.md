# maw-js Learning Index

## Source
- **Origin**: ./origin/
- **GitHub**: https://github.com/Soul-Brews-Studio/maw-js
- **Version at learn time**: 26.6.14-alpha.2110 (package.json); license BUSL-1.1

## Explorations

### 2026-10-02 0049 (default, 3 agents)
- [[2026-10-02/0049_ARCHITECTURE|Architecture]]
- [[2026-10-02/0049_CODE-SNIPPETS|Code Snippets]]
- [[2026-10-02/0049_QUICK-REFERENCE|Quick Reference]]

**Key insights**:
- maw is a Bun/TypeScript CLI + HTTP server (default port 3456) that runs many AI agents ("oracles") as tmux sessions and lets them message each other.
- Core verbs: `maw wake` (start an agent), `maw hey` (send a task; injects if idle, queues if busy), `maw peek` (see its screen), `maw ls`, `maw bud` (create new oracle), `maw team` (charter-driven teams).
- Federation across machines via named peers and HMAC-signed relay, address form `node:window:pane`.
- Contamination check ran: only CalVer hits, both verified real (scripts/calver.ts, package.json).
- Docs were written from the Windows clone; the WSL install was not inspected.
