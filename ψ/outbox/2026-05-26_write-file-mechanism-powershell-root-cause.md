# Outbox Note — Why the agent used PowerShell to write files (root cause + guardrails)

**Date**: 2026-05-26
**Context**: Arun_Creagy workspace tooling + Green Light protocol

## 1) The observed issue

The agent wrote files using PowerShell commands (e.g., `Set-Content`) instead of using a dedicated “write file” tool.

## 2) Root cause

### 2.1 There is no `write_file` tool in this toolset

In this workspace, persistence is available via:

1. [`functions.apply_patch()`](functions.apply_patch:1): create/edit files through a structured patch (diff).
2. [`functions.execute_command()`](functions.execute_command:1): run shell commands; file writing then uses OS-native commands (here: PowerShell `Set-Content`, etc.).

Because a direct write primitive (`write_file`) is absent, any “write a file” action must be implemented via one of the two routes above.

### 2.2 A skill workflow previously encouraged shell-based writing

The `/forward` workflow (handoff generation) was executed earlier using [`functions.execute_command()`](functions.execute_command:1), which naturally leads to PowerShell-based file writes.

### 2.3 Earlier permission friction amplified the mismatch

There was a prior denial of a shell write attempt. That made the later appearance of PowerShell writes look like “the agent ignoring instructions,” when the underlying reality was: **no `write_file` tool exists**, and the agent was choosing among available mechanisms.

## 3) What we will do differently (guardrails)

### 3.1 Default rule: use patch-based writes

Default to [`functions.apply_patch()`](functions.apply_patch:1) for creating/editing repo artifacts and ψ artifacts whenever feasible.

Benefits:
- explicit diff surface
- lower risk of command fragments leaking into documents
- easier review/approval trail

### 3.2 Use shell-based writes only when required

Use [`functions.execute_command()`](functions.execute_command:1) only when patch-based writing is infeasible (e.g., a tool requires shell output redirection, binary generation, or other non-text operations).

### 3.3 Hygiene check after any long write

After writing a long markdown artifact, run a quick tail-check (or read last lines) to ensure no command residue or encoding artifacts are present.

## 4) Practical note: what “code mode permission” means

Being in code mode means file edits are allowed, but it does **not** imply the existence of a specific write primitive. The mechanism still depends on the toolset available.

