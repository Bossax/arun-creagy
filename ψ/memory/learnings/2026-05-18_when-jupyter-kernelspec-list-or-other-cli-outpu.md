---
title: When `jupyter kernelspec list` (or other CLI output) crashes on Windows with `Un
tags: [windows, encoding, jupyter, python, unicode, workflow]
created: 2026-05-18
source: rrr: Arun_Creagy
---

# When `jupyter kernelspec list` (or other CLI output) crashes on Windows with `Un

When `jupyter kernelspec list` (or other CLI output) crashes on Windows with `UnicodeEncodeError: 'charmap' codec can't encode character '\u03c8'`, force UTF-8 output before invoking the module. Practical options:
- PowerShell: `$env:PYTHONIOENCODING='utf-8' ; <venv>\Scripts\python.exe -m jupyter kernelspec list`
- Or ensure Python prints via `sys.stdout.reconfigure(encoding='utf-8')` in scripts that may print ψ paths.
This avoids cp1252 stdout limitations on Windows terminals and prevents tool failures when paths include ψ or Thai characters.

---
*Added via Oracle Learn*
