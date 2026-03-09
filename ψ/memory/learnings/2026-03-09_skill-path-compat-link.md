---
date: 2026-03-09T15:45:00+07:00
type: learning
status: raw
tags:
  - skills
  - cross-agent
  - windows
  - git-bash
  - path-compat
---

# Skill path compatibility link (Roo ↔ Claude)

## Problem

Some skill documentation (and human muscle-memory) assumes skill scripts live under a Claude-style global skills folder, but in this environment the installed skill bundle lives under Roo’s global skills folder.

This caused failures like:

- `bun …/skills/recap/recap-rich.ts` → module not found

Evidence: see recap failure write-up in
[ψ/memory/logs/info/2026-03-09_12-50_recap-skill-path-assumption.md](ψ/memory/logs/info/2026-03-09_12-50_recap-skill-path-assumption.md:1)

## Fix (Option A)

Create a compatibility link so the Claude-style skills folder resolves to the Roo-installed skills folder.

This makes *any* documentation that uses the Claude-style path work immediately, without changing every SKILL doc.

## Status observed on this machine (Windows)

From a Windows `dir` listing, `skills` currently shows as a normal directory (not clearly labeled as a junction/symlink), and there are backup directories present as well.

This still achieves the practical goal (Claude-style path works), but it means we should treat this as **“compatibility achieved”** rather than **“definitely a shared link”** unless `LinkType/Target` confirms a junction/symlink.

## Why we kept running “smoke tests”

In VS Code terminals here, some command runs report an “undefined exit code”, and directory listing output wasn’t reliably coming back (plus `cmd.exe` can drop the terminal into interactive cmd mode if invoked incorrectly). The smoke test was the only objective proof that the original failing invocation now runs end-to-end.

## How to validate

1) Run a known skill script using the Claude-style path.
2) Confirm the output matches expectations (e.g., recap prints the session summary).

Optional (more definitive): use PowerShell to query the item metadata and see whether it’s a real folder, symlink, or junction (LinkType/Target).

## How to undo (important if adding Claude Code later)

If you later add Claude Code and want it to manage its own separate global skills folder, you should remove/relocate the compatibility setup first.

Recommended safe removal (principle: preserve history):

1) Back up whatever is currently at the Claude skills path by renaming it.
2) If it’s a link (junction/symlink), remove the link.
3) Recreate an empty directory for Claude Code to install into.

### Practical undo steps (PowerShell)

PowerShell is the safest for Windows link handling.

- Inspect link type/target:
  - `Get-Item $env:USERPROFILE+'/.claude/skills' | Format-List FullName,Attributes,LinkType,Target`

- Backup then remove (works whether it’s a directory or a link):
  - Rename: `Rename-Item -Path $env:USERPROFILE+'/.claude/skills' -NewName ('skills.bak-manual-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))`
  - Recreate empty folder: `New-Item -ItemType Directory -Path $env:USERPROFILE+'/.claude/skills' | Out-Null`

If it was a junction/symlink, `Rename-Item` will rename the link itself (not the target), which is what you want.

## Risks / gotchas

- **Coupling**: both agents now share the same physical skill bundle (updates from one affect the other).
- **Version collisions**: if Claude Code expects different versions of a skill than Roo has installed, behavior may diverge.

If the Claude skills path is currently a plain directory copy (not a link), then the risk changes to **drift** instead of coupling:

- **Drift**: Roo and Claude skills can silently diverge over time.
