---
name: clean-process
description: Terminate stale background agent daemons (agy, codex) and MCP server processes (node, python, bun, npx) when MCP configurations or environment variables are updated. Use when user says "clean process", "kill mcp", "reset mcp processes", or after updating mcp_config.json/env vars.
trigger: /clean-process
---

# /clean-process - Reset & Terminate Stale Agent Daemons (agy, codex) & MCP Background Processes

Terminate background agent daemons (`agy`, `codex`) and stale MCP server processes (Node, Python, Bun, NPX) to ensure new configuration changes and environment variables take effect on re-spawn.

## When to Use

Use this skill when:
- MCP configuration (`mcp_config.json` or `mcp.json`) has been updated.
- Environment variables for MCP servers (e.g., `BRAVE_API_KEY`, `PERPLEXITY_API_KEY`) have been added or updated.
- An MCP tool returns `422`, `401`, or authentication errors due to cached daemon / sub-process states.
- User requests "clean process", "kill mcp", "kill daemon", or "reset mcp".

---

## Execution Workflow (Windows / PowerShell)

### Step 1: Detect Active Daemons & MCP Processes

Run the following command to identify active daemon (`agy`, `codex`) and MCP worker processes:

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { `$_.Name -match 'agy|codex' -or (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*' -or `$_.CommandLine -like '*codex*' -or `$_.CommandLine -like '*agy*')) } | Select-Object ProcessId, Name, CommandLine | Format-Table -AutoSize"
```

### Step 2: Terminate Target Processes

Terminate any identified stale background daemons and MCP worker processes:

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { `$_.Name -match 'agy|codex' -or (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*' -or `$_.CommandLine -like '*codex*' -or `$_.CommandLine -like '*agy*')) } | ForEach-Object { Stop-Process -Id `$_.ProcessId -Force; Write-Host ('Terminated PID: ' + `$_.ProcessId) }"
```

### Step 3: Verify Process Termination

Confirm that no stale processes remain:

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { `$_.Name -match 'agy|codex' -or (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*' -or `$_.CommandLine -like '*codex*' -or `$_.CommandLine -like '*agy*')) }"
```

---

## Output Report

Upon completion, report:
- List of PIDs terminated (including `agy` and `codex` daemons if active).
- Status confirmation that stale processes and daemons were cleaned up.
- Recommendation to re-trigger the agent prompt so daemons re-spawn with freshly inherited environment variables.
