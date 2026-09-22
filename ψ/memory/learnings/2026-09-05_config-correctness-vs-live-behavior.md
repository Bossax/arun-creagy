---
tags: [infrastructure, verification, mcp, skills, powershell]
---

# A correct config file is not evidence the consuming app reads it

**Pattern**: Twice in one session, a config file with verifiably correct JSON
content was treated as "done" — once for skill discovery (`.agents\skills\`
junctions, which Antigravity's scanner silently skips), once for MCP server
connection (`.gemini\mcp_config.json`, a path Antigravity's official docs never
actually document — the real one is `.agents\mcp_config.json`). Both bugs
shipped invisibly until the human tested the *actual running application* and
reported a concrete symptom ("agy does not see these skills," "oracle mcp does
not connect"). File correctness and file-consumption are separate claims;
verifying the first is not evidence for the second.

A related, structurally identical bug: PowerShell scripts using
`ConvertFrom-Json -AsHashtable` (PowerShell 6+ only) tested successfully every
time because the testing tool always invoked `pwsh` 7 — but every *documented*
invocation said plain `powershell -File`, which resolves to legacy 5.1 on this
machine and hard-fails on that flag. The test environment silently differed
from the real usage environment, and success in one did not transfer to the
other.

**Concepts**: [config-vs-behavior-verification, cross-agent-mcp, test-environment-drift]

**Project**: arun-creagy-oracles / oracle-shared-skills / mcp-servers

**How to apply**: When a fix touches a separate running application's behavior
(another agent's config discovery, another process's runtime), test the actual
live behavior — a real connection, a real discovery scan, the actual documented
invocation command — not just the artifact's correctness. When a subagent's
finding about "where X reads config from" is inferred from a pre-existing
tool's behavior rather than X's own documentation, treat it as an unverified
hypothesis and check the source before building on it.
