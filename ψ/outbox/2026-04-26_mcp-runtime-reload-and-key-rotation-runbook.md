# MCP Runtime Reload and Key Rotation Runbook

**Date**: 2026-04-26  
**Scope**: [`perplexity`](.roo/mcp.json:37), [`brave-search`](.roo/mcp.json:47), and secret handling in [`.roo/mcp.json`](.roo/mcp.json:1)

## 1) What was remediated already

- Removed plaintext key storage from [`.roo/mcp.json`](.roo/mcp.json:1).
- Switched both servers to runtime injection:
  - [`perplexity.command`](.roo/mcp.json:38) = `cmd`
  - [`perplexity.args`](.roo/mcp.json:39) includes `set PERPLEXITY_API_KEY=%PERPLEXITY_API_KEY% && npx -y @perplexity-ai/mcp-server`
  - [`brave-search.command`](.roo/mcp.json:48) = `cmd`
  - [`brave-search.args`](.roo/mcp.json:49) includes `set BRAVE_API_KEY=%BRAVE_API_KEY% && npx -y @modelcontextprotocol/server-brave-search`

## 2) Verified diagnosis evidence

- Env vars present in shell:
  - `PERPLEXITY_API_KEY=present`
  - `BRAVE_API_KEY=present`
- Provider-direct checks succeeded:
  - `PPLX_DIRECT=200`
  - `BRAVE_DIRECT=200`
- MCP tools still failed in this host before process cleanup:
  - Brave: `422 SUBSCRIPTION_TOKEN_INVALID`
  - Perplexity: `401 invalid_api_key`
- Process scan showed multiple stale/redundant MCP-related processes; cleanup was executed.

## 3) Runtime reload/remediation sequence

1. Ensure config is the hardened version in [`.roo/mcp.json`](.roo/mcp.json:1).
2. Kill stale MCP subprocesses (`cmd`, `node`, `npx`) tied to Perplexity/Brave.
3. Restart the MCP client host session (or full IDE if needed).
4. Re-run MCP calls for:
   - `brave_web_search`
   - `perplexity_search` or `perplexity_ask`
5. If failures persist with provider-direct still `200`, treat as host lifecycle/config-source mismatch, not key-format error.

## 4) Mandatory key rotation runbook

Because credentials were historically stored in [`.roo/mcp.json`](.roo/mcp.json:1), rotate both keys now.

### Rotate Perplexity key

1. Create a new key in provider dashboard.
2. Revoke old key immediately.
3. Update environment variable `PERPLEXITY_API_KEY` at OS/user level.
4. Open new terminal and confirm it is loaded.
5. Verify provider-direct request returns `200`.

### Rotate Brave key

1. Create a new key in provider dashboard.
2. Revoke old key immediately.
3. Update environment variable `BRAVE_API_KEY` at OS/user level.
4. Open new terminal and confirm it is loaded.
5. Verify provider-direct request returns `200`.

### Post-rotation validation

1. Restart MCP host/client session.
2. Re-run MCP tool calls for Brave and Perplexity.
3. Confirm both return successful results.
4. Confirm no plaintext secrets exist in [`.roo/mcp.json`](.roo/mcp.json:1) and shipment files under [`ψ/outbox`](ψ/outbox).

## 5) Operational note

If provider-direct remains `200` but MCP still fails after rotation + restart, the remaining fault domain is MCP client runtime lifecycle/config provenance. Escalate with process list, active config file path, and failing tool traces.

