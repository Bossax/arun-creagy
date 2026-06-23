# Handoff: NotebookLM MCP clean recovery and session stability

## Context
We updated the Roo-only NotebookLM guardrails and plan files, confirmed the installed runtime already had the browser stability patches, and then exercised the live NotebookLM notebook session.

## What happened
- NotebookLM health initially looked green but the live session kept dying on launch.
- Multiple Chrome/Edge processes were holding the profile unstable.
- Cleanup + fresh auth restored the notebook session.
- The active notebook is [`CRDB TOR 5.5 Climate Risk Articles`](https://notebooklm.google.com/notebook/bb0355f2-1119-4385-b3bc-6b7cfa189296).
- The live session is usable again via the current notebook session.

## Key lesson
`get_health` can show `authenticated: true` while `active_sessions = 0`; the notebook is not queryable until a live browser session exists.

## Useful recovery pattern
1. Close all Chrome and Edge instances.
2. Run `cleanup_data(confirm=true, preserve_library=true)`.
3. Run `setup_auth` and sign in.
4. Verify `active_sessions > 0`.
5. Reuse the live session for follow-up queries.

## Follow-up note
Stealth should remain off for stability in this setup. Use one stable session per notebook when possible.