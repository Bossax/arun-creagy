---
title: Hybrid Environment Discipline (Windows 11 / PowerShell / Git Bash / Linux Contai
tags: [hybrid-environment, windows-bash-linux, shell-wrapping, path-translation]
created: 2026-04-12
source: rrr: Arun_Creagy Environment Check
project: github.com/sitth/arun_creagy
---

# Hybrid Environment Discipline (Windows 11 / PowerShell / Git Bash / Linux Contai

Hybrid Environment Discipline (Windows 11 / PowerShell / Git Bash / Linux Container):
- Always use forward slashes (/).
- Wrap Git Bash commands in 'bash -lc' if the primary tool shell is PowerShell.
- Use absolute host paths (e.g., C:/Users/...) to avoid container mapping confusion.
- Perform atomic execution steps rather than complex subshells to prevent PowerShell/Bash escaping conflicts.

---
*Added via Oracle Learn*
