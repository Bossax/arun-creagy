---
title: When joining Thai administrative spatial data, prefer using 2-digit/4-digit/6-di
tags: [spatial-analysis, data-engineering, thailand, join-logic]
created: 2026-05-25
source: rrr: CRI App Hardening v1.2.0
---

# When joining Thai administrative spatial data, prefer using 2-digit/4-digit/6-di

When joining Thai administrative spatial data, prefer using 2-digit/4-digit/6-digit DOPA code prefixes for filtering and joining rather than names, as province/district names are frequently corrupted (e.g., Bangkok as '<NA>') or inconsistent. Use 'left' joins to ensure full region boundaries are rendered even for areas with zero/missing impact data.

---
*Added via Oracle Learn*
