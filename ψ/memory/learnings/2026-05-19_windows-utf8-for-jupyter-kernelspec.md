# Learning — Windows UTF-8 stdout for Jupyter kernelspec (ψ-safe)

## Problem
Running Jupyter CLI commands on Windows can crash with:

`UnicodeEncodeError: 'charmap' codec can't encode character '\u03c8'...`

This happens when stdout is cp1252 and a path contains `ψ` (or Thai characters). A common trigger is:

- `python -m jupyter kernelspec list`

## Fix / Pattern
Force UTF-8 output before invoking Jupyter:

- PowerShell:
  - `$env:PYTHONIOENCODING='utf-8' ; <venv>\Scripts\python.exe -m jupyter kernelspec list`

Also safe to apply inside Python scripts that print paths:

- `sys.stdout.reconfigure(encoding='utf-8')`

## Why this matters
Without this, tool calls that enumerate kernels or paths can fail in environments that use `ψ/` as a directory prefix (Oracle brain layout).

