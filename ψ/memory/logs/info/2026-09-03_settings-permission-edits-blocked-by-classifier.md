---
date: 2026-09-03T00:00:00+07:00
type: info
status: raw
significance: important
---

Settings.json permission-rule edits (adding a Bash allowlist entry, e.g. for `python -c` JSON inspection commands) are blocked by the Claude Code auto-mode classifier even with explicit user confirmation in-chat ("do it"). This is a hard environment gate, not something that clears with in-conversation approval. Attempted twice via the `update-config` skill in this session, both denied with "Blocked by classifier." User needs to add such rules directly to `.claude/settings.json` or `settings.local.json` themselves — Claude cannot self-serve this even when explicitly asked to. Workaround for the original need (avoiding repeated approval prompts for read-only `python -c` JSON validation): either the user pastes the allowlist line in manually, or Claude drops python entirely and reads JSON files directly instead.

Logged via /fyi
