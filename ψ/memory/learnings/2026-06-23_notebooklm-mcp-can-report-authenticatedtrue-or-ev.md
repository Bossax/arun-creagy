---
title: NotebookLM MCP can report authenticated=true or even show a selected notebook wh
tags: [notebooklm, mcp, recovery, auth, browser-session, troubleshooting]
created: 2026-06-23
source: session retrospective 2026-06-23
project: github.com/sitth/oracleworkspace
---

# NotebookLM MCP can report authenticated=true or even show a selected notebook wh

NotebookLM MCP can report authenticated=true or even show a selected notebook while still lacking a live browser session. If repeated ask_question calls fail during launchPersistentContext, stale Chrome/Edge processes or a locked profile are the likely root cause, not the notebook content. Recovery pattern: close all Chrome and Edge instances, run cleanup_data(confirm=true, preserve_library=true), run setup_auth, verify authenticated=true and active_sessions > 0, then reuse the live session. Operational lesson: get_health is a state check, not a substitute for session validation. If active_sessions = 0, the notebook is not currently queryable even when the library and selected notebook are intact. Disable stealth for reliability and prefer one stable session per notebook over repeated browser re-launches.

---
*Added via Oracle Learn*
