# Portable Skill Capability Contract

The skills in this project are host-neutral. They live only in `.agents/skills` and
must not require a particular LLM, a provider-owned skill directory, or a provider
planning UI.

## Required capabilities

| Capability | Contract |
| --- | --- |
| Repository | Read Git and workspace state using the host's normal command tools. |
| Oracle | Discover and call the configured Oracle MCP tools. A skill that needs Oracle stops before writing its Oracle-backed artifact when the capability is unavailable. |
| Session history | Query `session_history.py` with an explicit host when known. It returns normalized JSON or a truthful `available: false` result. |
| User interaction | Present normal Markdown results and questions. Do not require a host-specific plan or approval tool. |

## Session-history contract

`scripts/session_history.py` accepts `--host antigravity`, `--host codex`, or
`--host auto`. `auto` only uses the `ORACLE_SKILL_HOST` environment variable;
otherwise it returns `unknown-host` rather than guessing from unrelated folders.

The JSON result always contains `available`, `host`, `sessions`, and `reason`.
Session entries contain `sessionId`, `startedAt`, `endedAt`, `messages`, and
`source`. Missing or malformed data is omitted, never invented.

## Fallback rules

If session history is unavailable, skills may use the active conversation and
repository facts, and must state that fallback. They must not search another host's
session directory. Oracle is not optional for `rrr` or `trace`.
