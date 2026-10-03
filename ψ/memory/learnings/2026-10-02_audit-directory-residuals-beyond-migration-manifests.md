---
pattern: When retiring or migrating a project workspace based on a peer agent's handoff manifest, always perform a directory-level diff (Disk Files minus Manifest Files) to identify and handle orphaned build artifacts, unindexed virtual environments, and local scratchpad data before declaring the retirement complete.
date: 2026-10-02
source: rrr: Arun_Creagy (00.35_cri-workspace-retirement-and-archiving)
concepts: [rrr, workspace-migration, retirement-manifest, directory-audit, git-hygiene, build-artifacts]
---

A migration manifest delivered by another repository or peer agent represents only what that agent crawled, ingested, and certified as knowledge artifacts. It rarely accounts for uncommitted development overhead, virtual environments (`.venv`), bundled distribution builds (`dist/`, PyInstaller `_internal/`), or temporary upload directories (`.tmp.driveupload/`).

In the CRI workspace retirement, executing an 897-row certified manifest deleted all targeted documents with zero hash mismatches, yet left behind 36,929 files and over 2.3 GB of unmanaged build bloat in `data_system/`.

Practical rules that transfer:
- Never equate processing a migration manifest with emptying a working directory. Always verify `Get-ChildItem -Recurse -File` counts before and after.
- Isolate and purge untracked build overhead (`.venv`, `node_modules`, `dist/`) first before executing document-level retirement scripts.
- In Git, deleting files from the working tree does not shrink `.git/` packfiles. Aggressive garbage collection (`git gc --aggressive`) optimizes delta compression, but true repository shrinkage requires history rewriting (`git-filter-repo`) when large binaries have been committed in the past.
