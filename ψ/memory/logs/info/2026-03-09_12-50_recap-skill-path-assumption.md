---
date: 2026-03-09T12:50:00+07:00
type: info
status: raw
significance: interesting
---

## Observation

Running the recap command failed because it attempted to load the recap script from a Claude Code global skill directory path, which does not exist in this Roo agent environment.

## Evidence

- Terminal output included: `error: Module not found "C:/Users/sitth/.claude/skills/recap/recap-rich.ts"`

## Hypotheses (ranked)

1) **Legacy path assumption**: recap skill docs/scripts were originally authored for Claude Code and later reused; the skill-home path is hardcoded to a Claude-specific default.
2) **Skill-home discovery gap**: the runtime should locate the installed skill bundle (Roo vs Claude) via an environment variable or a config file, but the workflow doesn’t.

## Suggested next steps

- Identify the actual skill installation home used by Roo on this machine.
- Add a compatibility layer (env var / fallback path resolution) so recap works across agents.
- If reproducible, open an issue in the upstream skills repo with:
  - the exact failing command
  - the error message
  - the expected behavior (agent-agnostic path resolution)
  - OS/shell details (Windows + Git Bash)

Logged via /fyi

