---
title: NotebookLM MCP clean recovery and session stability
tags: [notebooklm, mcp, recovery, auth, browser-session, troubleshooting]
created: 2026-06-23
source: session retrospective 2026-06-23
status: current
---

# NotebookLM MCP clean recovery and session stability

NotebookLM MCP can report `authenticated: true` or even show a selected notebook while still lacking a live browser session. If repeated `ask_question` calls fail during `launchPersistentContext`, the likely root cause is stale Chrome/Edge processes or a locked profile, not the notebook content.

## Recovery pattern
1. Close all Chrome and Edge instances.
2. Run `cleanup_data(confirm=true, preserve_library=true)` to clear browser/auth state while preserving the notebook library.
3. Run `setup_auth` and complete sign-in.
4. Verify with `get_health` that `authenticated: true` and at least one active session exists.
5. Reuse the live session for follow-up questions instead of repeatedly reinitializing it.

## Operational lesson
`get_health` is a state check, not a substitute for session validation. If `active_sessions = 0`, the notebook is not currently queryable even when the library and selected notebook are intact.

## Notes
- Disable stealth for this notebooklm setup when prioritizing reliability.
- Prefer one stable session per notebook over repeated browser re-launches.
