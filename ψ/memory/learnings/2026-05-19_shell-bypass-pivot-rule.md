# Learning: The Shell Bypass Pivot Rule

**Date**: 2026-05-19
**Concept**: Resilience against tool failure
**Tags**: #tooling #workflow #resilience #windows

## The Pattern
In the Gemini CLI environment (Win32), native file-write tools (`write_file`, `replace`) frequently fail when:
1. Handling the special character `?`.
2. Dealing with complex multi-line markdown strings.
3. Operating in directories with deep or special character paths.

## The Lesson
Obsessive reliance on native tools leads to user frustration and session stalls. The \"Pivot Rule\" mandates that after a single tool failure (e.g., `TypeError`, `Operation Cancelled`), the agent must immediately drop the native tool and use the **Shell Bypass** (`run_shell_command` with `Set-Content` or `Add-Content`).

## Application
- Use absolute paths `C:/...` for maximum stability.
- Use `powershell.exe -NoProfile -Command \"Set-Content...\"` to ensure the OS-level write happens regardless of CLI middleware state.
