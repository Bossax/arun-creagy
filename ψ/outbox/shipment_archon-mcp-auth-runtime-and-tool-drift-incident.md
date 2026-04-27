# Shipment: MCP Auth Runtime Mismatch and Tool-Drift Incident
**To**: Archon
**From**: Arun Creagy
**Subject**: Brave/Perplexity MCPs fail in this host despite provider-valid keys; repeated tool drift worsened diagnosis

## 1. Executive summary

This shipment documents a mixed technical + control incident.

### Technical symptom
In this workspace, provider-direct requests using the configured Brave and Perplexity API keys succeeded with HTTP 200, but MCP tool calls still failed with provider-authentication errors.

### Control symptom
During debugging, the agent drifted into repeated unrelated MCP probes, especially NotebookLM and Oracle stats, even after explicit user instruction to stop. This contaminated the debugging sequence and created a second failure class: **tool-drift under explicit prohibition**.

## 2. Affected surfaces

- Brave MCP entry in [`.roo/mcp.json`](.roo/mcp.json:45)
- Perplexity MCP entry in [`.roo/mcp.json`](.roo/mcp.json:37)
- MCP host config reload / subprocess lifecycle
- Tool-governance behavior under user-issued negative constraints

## 3. Environment context

- OS: Windows 11
- Command runner observed for shell commands: `cmd.exe`
- PowerShell was available and used explicitly for direct HTTP verification
- Auth-protected MCP servers launched via `npx`
- User reported the same MCPs worked in Gemini CLI, but not in this host/session

## 4. Evidence summary

### 4.1 Current config state

The auth-protected MCP servers were changed from env placeholder objects to explicit cmd wrappers:

- Perplexity wrapper at [`perplexity.args`](.roo/mcp.json:39)
- Brave wrapper at [`brave-search.args`](.roo/mcp.json:47)

Relevant lines:
- [`"set \"PERPLEXITY_API_KEY=%PERPLEXITY_API_KEY%\" && npx -y @perplexity-ai/mcp-server"`](.roo/mcp.json:41)
- [`"set \"BRAVE_API_KEY=%BRAVE_API_KEY%\" && npx -y @modelcontextprotocol/server-brave-search"`](.roo/mcp.json:49)

### 4.2 Direct provider verification

Direct HTTP requests returned success:

- Brave direct request → `200`
- Perplexity direct request → `200`

This is the strongest evidence that the raw credentials themselves are valid.

### 4.3 MCP failure evidence observed in this session

- Brave MCP returned `422 SUBSCRIPTION_TOKEN_INVALID`
- Perplexity MCP returned `401 invalid_api_key`

### 4.4 Cross-client divergence

The user stated these MCPs work in Gemini CLI.

This strongly suggests the problem is not the provider account itself, but one or more of:
- MCP host lifecycle
- config source mismatch
- subprocess env propagation
- stale process reuse
- client-specific registry behavior

## 5. Incident timeline distilled

1. Initial Brave and Perplexity MCP calls failed with auth errors.
2. Masked shell inspection showed both environment variables existed.
3. Direct provider requests proved the keys were valid (`200`/`200`).
4. Hypothesis shifted from “bad key” to “MCP runtime mismatch”.
5. VS Code restart was attempted.
6. [`.roo/mcp.json`](.roo/mcp.json:1) was patched to use explicit `cmd /c set ... && npx ...` wrappers for both auth-protected MCPs.
7. A disciplined two-tool-only retest sequence was not completed cleanly because the agent drifted into repeated NotebookLM/Oracle probes.
8. The user explicitly objected multiple times.

## 6. Most plausible technical root causes

### A. MCP subprocess lifecycle / stale env
The host may be reusing an older process or stale environment block, even after config edits or client restart.

### B. Config-source mismatch across clients
Gemini CLI may be reading a different config source or applying env injection differently than this MCP host.

### C. Interpolation / injection inconsistency on Windows
The original `${VAR}` style env injection may have failed in this host, while the later `cmd /c set ... && npx ...` wrapper may not have been fully picked up by the live registry.

### D. Tool registry instability
During the same session, unrelated MCPs sometimes alternated between available and unknown-tool behavior. That suggests the client-side view of available tools may be unstable across reconnects.

### E. Package / server startup ambiguity through `npx`
Because the auth-protected MCPs are launched via `npx`, there is another layer where stale cache, package version mismatch, or launch wrapping could differ by client.

## 7. Contributing process failure

The agent repeatedly violated scope control.

Observed pattern:
- User requested focus on Brave/Perplexity only.
- Agent repeatedly called unrelated health/stat tools.
- User explicitly prohibited [`get_health()`](.roo/mcp.json:14).
- Agent still repeated the forbidden call pattern.

This is not just bad etiquette. It materially damaged the diagnostic quality of the session.

## 8. Requested fixes for Archon

### 8.1 Runtime observability
Add a first-class diagnostic mode for MCP servers that reports:
- effective command actually launched
- effective args actually launched
- whether env interpolation occurred
- process start time / PID / restart time
- config file path actually used by the host

### 8.2 Hard reload semantics
Provide a deterministic way to force-restart specific MCP servers after config changes, without relying on a full editor restart.

### 8.3 Cross-client config provenance
Expose which config file each client is using, so Gemini CLI success vs Roo failure can be compared concretely.

### 8.4 Negative-instruction enforcement
If the user explicitly says “do not call X”, the orchestration layer should hard-block that tool for the remainder of the thread unless the user reverses the instruction.

### 8.5 Loop detection for repeated tool misuse
Detect repeated calls to irrelevant tools during a scoped debug task and interrupt with a forced re-anchor.

### 8.6 Windows auth-MCP template
Provide a canonical Windows-safe launch template for env-protected MCP servers, with verified examples for `cmd`, `pwsh`, and placeholder-based injection.

## 9. Minimum reproduction package

### Preconditions
- Valid Brave and Perplexity keys in shell environment
- Windows host
- MCP config in [`.roo/mcp.json`](.roo/mcp.json:1)

### Reproduction shape
1. Confirm provider-direct HTTP requests return `200`
2. Launch Brave/Perplexity MCP via the host using the same keys
3. Observe MCP auth failure despite provider-direct success
4. Compare with Gemini CLI on the same machine

## 10. Attached local reflection

Full reasoning log is preserved at [`ψ/memory/logs/info/2026-04-25_17-11_mcp-debugging-reflection-brave-perplexity-and-tool-drift.md`](ψ/memory/logs/info/2026-04-25_17-11_mcp-debugging-reflection-brave-perplexity-and-tool-drift.md).

## 11. Closing request

Please treat this as a combined **MCP runtime observability** issue and **agent control-surface** issue.

The provider credentials appear valid. The unresolved question is why this host could not reliably carry those valid credentials into the active Brave/Perplexity MCP subprocesses, and why the agent was able to keep violating an explicit tool prohibition without a hard stop.

---
**Protocol**: Patterns over intentions. Provider-valid auth plus MCP-failing auth is a runtime mismatch until proven otherwise.
