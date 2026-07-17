---
id: learning_2026-07-17_under-windows-powershell-pwsh-environment-file
type: learning
title: Under Windows PowerShell (pwsh) environment, file redirection (>) defaults to UT
concepts: [win32, encoding, python-glob, powershell]
tags: [win32, encoding, python-glob, powershell]
created: 2026-07-17
indexed_at: 2026-07-17T03:23:08.613Z
updated_at: 2026-07-17T03:23:08.613Z
hash: sha256:18276a4d8d27b3532f8cddbf6107738bf9c4d5ac7aa335a203d2891811801a28
source: Oracle Learn
project: github.com/bossax/susu_ocean
arra_id: learning_2026-07-17_under-windows-powershell-pwsh-environment-file
arra_type: learning
arra_concepts: [win32, encoding, python-glob, powershell]
arra_created: 2026-07-17T03:23:08.613Z
---

# Under Windows PowerShell (pwsh) environment, file redirection (>) defaults to UT

Under Windows PowerShell (pwsh) environment, file redirection (>) defaults to UTF-16LE encoding. When saving raw outputs from external CLIs (such as nlm), explicitly pipe output using 'Out-File -FilePath <path> -Encoding utf8' to prevent encoding read errors in subsequent node parsing or viewing tools. Additionally, when searching for session logs in Python, standard glob recursively skipping hidden/dot directories (like .system_generated) on Windows must be replaced with os.walk to guarantee traversal.

---
*Added via Oracle Learn*
