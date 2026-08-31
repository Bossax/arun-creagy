# Lesson: A patched-environment selftest doesn't prove the real launch path works

**Context**: Built `tools/qwen-mcp/server.py`, an MCP server calling Alibaba DashScope's Qwen models. `DASHSCOPE_API_KEY` was set at Windows User env scope but *after* the current login session began, so it was absent from the live process environment. Ran `--selftest` by manually re-injecting the key via `[System.Environment]::GetEnvironmentVariable(...)` in the same PowerShell call — got a real, successful API response. Wired the server into `.mcp.json`, told Boss to restart Claude Code, and the very first real MCP tool call failed with an opaque error, because Claude Code's MCP-spawned subprocess inherits environment differently than my manual test shell did.

**The lesson**: Confirming "the code works given a value for X" is a different, weaker claim than "the code works in its actual deployment shape." When a selftest patches in something the real launcher won't provide (an env var, a working directory, an auth token from a different source), a green selftest is not evidence the integration works — it's evidence the logic works. The two can and did diverge here without any code being wrong.

**Concepts**: mcp-server, environment-variables, windows-session, testing-methodology, dashscope, qwen

**How to apply**: Before declaring an integration "verified," ask specifically whether the test's setup matches the real invocation's setup — same process-spawn path, same inherited state, same auth source. If they differ, the test needs to either match the real path or the gap needs to be called out explicitly as unverified, not glossed over by a passing selftest.
