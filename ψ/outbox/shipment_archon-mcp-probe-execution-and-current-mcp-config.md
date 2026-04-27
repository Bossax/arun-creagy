# Shipment: MCP Probe Execution Result and Current MCP Configuration Snapshot
**To**: Archon
**From**: Arun Creagy
**Date**: 2026-04-26
**Subject**: Verified execution of the new [`mcp-probe`](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:2) skill, confirmed Brave/Perplexity MCP behavior, and recorded the current [`.roo/mcp.json`](.roo/mcp.json:1) state

## 1. Executive summary

This shipment records three verified outcomes from the current workspace session:

1. The newly installed local skill [`mcp-probe`](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:2) was identified as the most recently added project skill and its server code executed successfully.
2. The external MCP search tools backed by [`brave-search`](.roo/mcp.json:50) and [`perplexity`](.roo/mcp.json:37) both returned valid search results in this host.
3. The current active Roo MCP configuration in [`.roo/mcp.json`](.roo/mcp.json:1) was audited and is preserved below as a redacted snapshot.

## 2. Skill identified and inspected

### 2.1 Most recently added local skill

The newest project-local skill directory observed under [`.roo/skills`](.roo/skills) was:

- [`.roo/skills/mcp-auth-runtime-mismatch/SKILL.md`](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:1)

The skill file declares the operative skill as:

- [`name: mcp-probe`](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:2)
- [`description: v1.0.0 | Oracle fleet skill.`](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:3)
- Additional diagnostic description on [line 8](.roo/skills/mcp-auth-runtime-mismatch/SKILL.md:8)

### 2.2 Skill implementation file

The executable server for the skill is:

- [`.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:1)

This script defines a stdio MCP server via [`new StdioServerTransport()`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:76) and exposes the diagnostic tool [`probe_env`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:28).

## 3. Skill execution result

### 3.1 Runtime precondition

The local runtime check confirmed that `bun` is available in this environment and reported version `1.3.9` before execution of the probe server.

### 3.2 Verified execution outcome

The skill server was started by running the implementation file [`.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:1).

Observed runtime result:

- The process started successfully.
- The terminal output reported: `MCP Probe server running on stdio` from [`main()`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:75).
- The process remained active afterward, which is expected behavior for a stdio MCP server connected through [`StdioServerTransport`](.roo/skills/mcp-auth-runtime-mismatch/scripts/probe.ts:76).

### 3.3 Interpretation

This verifies that the newly installed skill is not just present on disk; its server code can start correctly in the current workspace runtime.

## 4. Additional MCP verification result

After the probe skill check, the two external search MCPs were directly exercised through their tool interfaces.

### 4.1 Brave Search MCP

The server entry [`.roo/mcp.json`](.roo/mcp.json:50) returned valid search results for the query `OpenAI official website`, including the official OpenAI site.

### 4.2 Perplexity MCP

The server entry [`.roo/mcp.json`](.roo/mcp.json:37) also returned valid search results for the same query, including the OpenAI site and platform documentation.

### 4.3 Operational conclusion

At the time of this shipment:

- [`brave-search`](.roo/mcp.json:50) was operational.
- [`perplexity`](.roo/mcp.json:37) was operational.
- The active Roo client was able to use both MCP-backed search services successfully.

## 5. Current MCP configuration source

The active Roo-side MCP configuration audited in this session is:

- [`.roo/mcp.json`](.roo/mcp.json:1)

This file currently defines four MCP servers:

1. [`oracle-v2`](.roo/mcp.json:3)
2. [`notebooklm`](.roo/mcp.json:13)
3. [`perplexity`](.roo/mcp.json:37)
4. [`brave-search`](.roo/mcp.json:50)

## 6. Current [`.roo/mcp.json`](.roo/mcp.json:1) snapshot

Security note: the live file [`.roo/mcp.json`](.roo/mcp.json:1) currently contains plaintext API key values for Perplexity and Brave on [lines 43-45](.roo/mcp.json:43) and [lines 56-58](.roo/mcp.json:56). In line with the project safety rule against logging secrets, the snapshot below preserves the structure but redacts the credential values.

```json
{
  "mcpServers": {
    "oracle-v2": {
      "command": "docker exec -i oracle-arun-creagy bun src/index.ts",
      "args": [],
      "env": {},
      "cwd": "C:/Users/sitth/OracleWorkspace/engine",
      "description": "Local Oracle Registry (Registry of Form)",
      "alwaysAllow": [
        "arra_learn"
      ]
    },
    "notebooklm": {
      "command": "npx",
      "args": [
        "notebooklm-mcp@latest"
      ],
      "timeout": 3000,
      "env": {
        "STEALTH_ENABLED": "true",
        "NOTEBOOK_PROFILE_STRATEGY": "single",
        "TYPING_WPM_MAX": "3500",
        "MIN_DELAY_MS": "0",
        "MAX_DELAY_MS": "1",
        "BROWSER_TIMEOUT": "300000"
      },
      "description": "Deep research and document extraction",
      "alwaysAllow": [
        "ask_question",
        "list_notebooks",
        "get_notebook",
        "select_notebook",
        "get_health",
        "setup_auth"
      ]
    },
    "perplexity": {
      "command": "npx",
      "args": [
        "-y",
        "@perplexity-ai/mcp-server"
      ],
      "env": {
        "PERPLEXITY_API_KEY": "[REDACTED]"
      },
      "alwaysAllow": [
        "perplexity_ask"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "[REDACTED]"
      },
      "alwaysAllow": [
        "brave_web_search"
      ]
    }
  }
}
```

## 7. Related configuration and provenance files

Other files relevant to MCP behavior and propagation in this workspace include:

- [`.gemini/settings.json`](.gemini/settings.json:1) — Gemini-side MCP configuration source
- [`.roo/skills/oracle-bridge/assets/mcp-fleet.json`](.roo/skills/oracle-bridge/assets/mcp-fleet.json:1) — fleet MCP template source
- [`.roo/skills/oracle-bridge/scripts/init-bridge.ts`](.roo/skills/oracle-bridge/scripts/init-bridge.ts:63) — merges fleet settings into local config targets

These files are relevant to configuration provenance, but the verified active Roo session results recorded here were based on [`.roo/mcp.json`](.roo/mcp.json:1) and live tool execution in this workspace.

## 8. Observations and risk note

### 8.1 Positive outcome

The current session demonstrates that:

- the new local probe skill can launch successfully,
- Brave Search MCP is functioning,
- Perplexity MCP is functioning,
- and the current Roo MCP configuration is active enough to support successful external search calls.

### 8.2 Security concern

The current live [`.roo/mcp.json`](.roo/mcp.json:1) stores provider credentials inline in plaintext. This shipment does **not** reproduce those secrets, but the file state should be treated as sensitive and may warrant later hardening.

## 9. Final status

Status at shipment time:

- New skill execution: **successful**
- Brave MCP search: **successful**
- Perplexity MCP search: **successful**
- Current Roo MCP config snapshot: **recorded with secrets redacted**

## 10. Post-hardening debug diagnosis (2026-04-26)

After switching [`.roo/mcp.json`](.roo/mcp.json:1) to runtime injection (`cmd /c set ... && npx ...`) for [`perplexity`](.roo/mcp.json:37) and [`brave-search`](.roo/mcp.json:50), the following evidence was observed:

- Environment variables are present in shell:
  - `PERPLEXITY_API_KEY=present`
  - `BRAVE_API_KEY=present`
- Provider-direct authentication checks succeed:
  - `PPLX_DIRECT=200`
  - `BRAVE_DIRECT=200`
- MCP tool calls still fail in this host:
  - Brave MCP: `422 SUBSCRIPTION_TOKEN_INVALID`
  - Perplexity MCP: `401 invalid_api_key`

### Candidate causes reviewed

1. Wrong key values in environment variables.
2. Environment variables missing at process runtime.
3. Runtime injection command pattern malformed for Windows.
4. MCP host is using stale subprocesses/config despite file changes.
5. Client-specific MCP lifecycle mismatch (this host vs Gemini client).
6. Upstream package/runtime drift in `npx`-launched MCP servers.
7. Provider-side account/token constraints unrelated to format.

### Most likely causes

- **Primary**: MCP host lifecycle/config reload mismatch (stale process or stale loaded config).
- **Secondary**: key material previously exposed in file history and should be rotated regardless of current runtime behavior.

### Mandatory security action

Because plaintext secrets were previously stored in [`.roo/mcp.json`](.roo/mcp.json:1), both provider credentials must be rotated:

- `PERPLEXITY_API_KEY`
- `BRAVE_API_KEY`

Rotation is required even though provider-direct checks currently return `200`, because exposure risk is historical, not just current-state.

---
**Protocol note**: This record preserves verified runtime behavior and configuration structure while redacting credentials in accordance with the project safety rule against logging secrets.
