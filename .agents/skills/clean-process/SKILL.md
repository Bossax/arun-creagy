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

### Step 1: Detect Active MCP Worker Processes

Run the following command to identify active MCP worker processes (excluding host daemons `agy` and `codex`):

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*')) -and `$_.Name -notmatch 'agy|codex' } | Select-Object ProcessId, Name, CommandLine | Format-Table -AutoSize"
```

### Step 2: Terminate Stale MCP Worker Processes

Safely terminate target MCP server worker processes without killing the host runner (`agy.exe` / `codex.exe`):

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*')) -and `$_.Name -notmatch 'agy|codex' } | ForEach-Object { if (`$_.ProcessId -ne `$PID) { Stop-Process -Id `$_.ProcessId -Force -ErrorAction SilentlyContinue; Write-Host ('Terminated PID: ' + `$_.ProcessId) } }"
```

### Step 3: Verify Process Termination

Confirm that no stale MCP server processes remain:

```powershell
pwsh -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { (`$_.CommandLine -and (`$_.CommandLine -like '*mcp*' -or `$_.CommandLine -like '*brave-search*' -or `$_.CommandLine -like '*perplexity*')) -and `$_.Name -notmatch 'agy|codex' }"
```

### Step 4: (Optional) Detached Host Daemon Restart

If host daemons (`agy`, `codex`) explicitly need to be restarted, **always launch a detached background job with a delay** so the active agent turn finishes cleanly before termination:

```powershell
pwsh -NoProfile -Command "Start-Job -ScriptBlock { Start-Sleep -Seconds 3; Get-CimInstance Win32_Process | Where-Object { `$_.Name -match 'agy|codex' } | ForEach-Object { Stop-Process -Id `$_.ProcessId -Force } }"
```

---

## Output Report

Upon completion, report:
- List of MCP worker PIDs terminated.
- Status confirmation that stale MCP processes were cleaned up.
- Note whether a background job was scheduled for daemon restart if requested.
