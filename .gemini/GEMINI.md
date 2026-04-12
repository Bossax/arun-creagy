# GEMINI.md — Gemini Execution Rules

This file contains environment-specific execution rules for the Gemini CLI. For my central Oracle identity (Arun Creagy), the 5 Principles, and the project's Brain Structure (ψ/), always refer to [CLAUDE.md](./CLAUDE.md).

## Hybrid Environment Discipline
Always adhere to these rules for executing commands in this Windows 11 / PowerShell / Git Bash / Linux environment:

- **Path Hygiene**: Always use forward slashes (`/`) for all file paths and tool calls.
- **Shell Wrapping**: If the primary tool shell is PowerShell, wrap Git Bash commands in `bash -lc` to ensure proper environment loading and path translation.
- **Absolute Paths**: Prefer absolute host paths (e.g., `C:/Users/...`) when interacting with local tools to avoid confusion with container mapping or relative path resolution.
- **Atomic Execution**: Perform atomic execution steps rather than complex subshells or piped commands to prevent PowerShell/Bash escaping conflicts and ensure traceable history.

## Contextual Precedence
- Instructions in this file and `CLAUDE.md` take absolute precedence over general defaults.
- For project-specific plans and analysis, follow the placement rules defined in `CLAUDE.md` (under `ψ/incubate/<Client>/<Project>/output/`).
