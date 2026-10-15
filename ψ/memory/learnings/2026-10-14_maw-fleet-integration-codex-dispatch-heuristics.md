---
id: learning_2026-10-14_maw-fleet-integration-codex-dispatch-heuristics
type: learning
title: "MAW Fleet Integration & Codex Dispatch Heuristics:"
concepts: [rrr, maw, codex, multi-agent-orchestration, snapshot-recovery, command-scoping]
tags: [rrr, maw, codex, multi-agent-orchestration, snapshot-recovery, command-scoping]
created: 2026-10-14
indexed_at: 2026-10-14T10:38:40.190Z
updated_at: 2026-10-14T10:38:40.190Z
hash: sha256:1a55cf560dfe59dbbf74dede6aa3b9f6e955f9f1168d61f134c14044aab207db
source: rrr on 17.37_maw-samart-writer-integration
project: github.com/bossax/arun-creagy
arra_id: learning_2026-10-14_maw-fleet-integration-codex-dispatch-heuristics
arra_type: learning
arra_concepts: [rrr, maw, codex, multi-agent-orchestration, snapshot-recovery, command-scoping]
arra_created: 2026-10-14T10:38:40.190Z
---

# MAW Fleet Integration & Codex Dispatch Heuristics:

MAW Fleet Integration & Codex Dispatch Heuristics:
1. Local Fleet Discovery: MAW scans <ghqRoot>/github.com/local/<name>-oracle containing a ψ/ directory and strips the suffix to establish canonical agent handles.
2. Command Scoping: Per-agent runner commands with full CLI flags (e.g. `codex -m gpt-6.1-sol -c model_reasoning_effort="medium"`) can be mapped directly under `commands` in ~/.config/maw/maw.config.json without affecting global user configurations.
3. Non-Interactive Invocation: MAW snapshots cause `maw ls` and `maw wake` to block on stdin restore prompts; scripted dispatches must pipe `< /dev/null` or ensure snapshot directories are clean.
4. Codex First-Time Traps: New Codex installations in WSL require sync of auth.json from the host and one-time terminal confirmation of folder trust before headless dispatch can execute.

---
*Added via Oracle Learn*
