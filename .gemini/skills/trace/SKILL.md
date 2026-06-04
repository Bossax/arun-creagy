---
installer: arra-oracle-skills-cli v1.0.0
origin: Project-local hardened version for Windows/ψ stability.
name: trace
description: '[local] Hardened v1.0.0 | Windows-stable trace with UTF-8 ψ support and semicolon-delimited PROJECT_DIRS detection. Use to find grounded evidence in transcripts and project memory.'
argument-hint: "<query> [--oracle | --smart | --deep]"
---

# /trace (Hardened)

## Implementation Notes (Windows Fix)
1. **UTF-8 ψ Support**: Explicitly handles the ψ character by resolving absolute Windows paths before execution.
2. **Semicolon Delimiter**: Correctly parses `PROJECT_DIRS` using `;` on Windows.
3. **Shell-Agnostic Paths**: Uses forward slashes internally but converts to backslashes for `Remove-Item` and `New-Item` calls.

## Step 0: Scaffolding
- Calculate absolute paths for `ψ/` to avoid shell encoding errors.
- Ensure `TODAY` and `TIME` are captured for the log filename.

## Step 1: Search Waves
- **Wave 1 (Oracle)**: `arra_search` (hybrid mode).
- **Wave 2 (Files)**: `grep_search` with specific directory inclusion (inbox, memory).
- **Wave 3 (Sessions)**: Call `python .gemini/skills/trace/scripts/dig.py` with `PROJECT_DIRS` correctly set.

## Step 2: Logging
- Writes results to `ψ/memory/traces/YYYY-MM-DD/HHMM_[query].md`.
- Calculates friction score based on source availability.

ARGUMENTS: $ARGUMENTS
