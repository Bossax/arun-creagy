---
id: learning_2026-07-17_when-synchronizing-files-helper-scripts-like-min
type: learning
title: When synchronizing files, helper scripts (like miner.py), and rules across paral
concepts: [workspace-sync, path-normalization, tool-safety]
tags: [workspace-sync, path-normalization, tool-safety]
created: 2026-07-17
indexed_at: 2026-07-17T04:38:12.396Z
updated_at: 2026-07-17T04:38:12.396Z
hash: sha256:9b6da2760670b262bfdc0b46007c36a77e8fcf18f83e5217cf73a3acd3b51049
source: Oracle Learn
project: bossax/susu_ocean
arra_id: learning_2026-07-17_when-synchronizing-files-helper-scripts-like-min
arra_type: learning
arra_concepts: [workspace-sync, path-normalization, tool-safety]
arra_created: 2026-07-17T04:38:12.396Z
---

# When synchronizing files, helper scripts (like miner.py), and rules across paral

When synchronizing files, helper scripts (like miner.py), and rules across parallel workspaces (such as Arun_Creagy and Susu_Ocean) via the shared Oracle, always verify and normalize local paths (e.g., path patterns matching %USERPROFILE%\.gemini\tmp\<project_name>\chats) to prevent namespace mismatch and file-not-found failures on the target workspace.

---
*Added via Oracle Learn*
