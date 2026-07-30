# Handoff: Brave Search MCP API Key & Process Reset

**Date**: 2026-07-30 11:16

## What We Did
- Tested Brave Search MCP tools (`brave_web_search`, `brave_local_search`), which returned `422 SUBSCRIPTION_TOKEN_INVALID`.
- Inspected active background MCP server processes using PowerShell (`Win32_Process`).
- Discovered that background `node.exe` process (PID 24368) was running with cached old environment key `BSA7DHN4CfiJaL3AynpxOnftTrQsY3h` instead of updated key `BSAeK2DGsRzeGFO1f7d1yrK7IGS2yRE`.
- Executed `/clean-process` skill to terminate all stale background MCP server processes (Node, CMD, PowerShell).

## Pending
- [x] Restart VS Code / Antigravity host to ensure new environment variables (`BRAVE_API_KEY=BSAeK2DGsRzeGFO1f7d1yrK7IGS2yRE`) are inherited by the parent process.
- [x] Re-test Brave Search MCP tools (`brave_web_search`) after VS Code restart to confirm clean authentication.

## Hypotheses for Next Session
- [ ] Hypothesis 1: Upon VS Code restart, the new parent process environment will pass `BSAeK2DGsRzeGFO1f7d1yrK7IGS2yRE` to spawned MCP servers, resolving the 422 authentication error.

## Key Files
- [Brave Web Search Schema](file:///C:/Users/sitth/.gemini/antigravity-cli/mcp/brave-search/brave_web_search.json)
- [Clean Process Skill](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/.agents/skills/clean-process/SKILL.md)
