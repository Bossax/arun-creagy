# Mandate: System Rules (Shell-Agnostic)

These rules ensure technical consistency across both PowerShell (Gemini CLI) and CMD (Roo Code).

## 1. Environment & Shells
 Operating in `cmdlet`. execute powershell command must start with `powershell.exe -NoProfile`.

- **Shell-Agnostic Syntax**: When referencing environment variables, specify for both shells: `%VAR%` (CMD) / `$env:VAR` (PS).
- **The Brain (ψ)**: Use PowerShell for all path operations involving the `ψ` character.

## 2. Path Syntax
- **Tool Parameters**: Forward slashes (`/`) (e.g., `read_file(file_path="ψ/memory/...")`).
- **Shell Commands**: 
  - CMD: Backslashes (`\`)
  - PS: Backslashes (`\`)

## 3. Technical Integrity
- **Absolute Paths**: Always resolve `ψ/` paths to their absolute host path when calling external CLIs.
- **Atomic Execution**: Maximum of two independent operations per `run_shell_command`.
- **Sorting (PS)**: `Get-ChildItem | Sort-Object LastWriteTime -Descending`.

## 4. PowerShell Execution Rules
- **Variable Escaping**: In Gemini CLI, the host shell expands `$_` in double-quoted strings. Use **single quotes** for the `-Command` block (e.g., `powershell.exe -Command '... { $_.Name ... }'`) or use **Simplified Filtering** (e.g., `Where-Object Name -match '...'`) to avoid expansion.
- **Special Characters (ψ)**: Wrap paths containing the `ψ` character in single quotes (e.g., `'ψ/memory/'`) to ensure the shell handles the character literal correctly.
- **Pipeline Hygiene**: Prefer native PowerShell cmdlets (`Where-Object`, `Select-Object`) over Unix ports (`grep`, `head`) when operating in Gemini CLI.
