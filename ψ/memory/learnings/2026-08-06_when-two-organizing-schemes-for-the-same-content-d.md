---
id: learning_2026-08-06_when-two-organizing-schemes-for-the-same-content-d
type: learning
title: "When two organizing schemes for the same content don't map 1:1 (e.g. CRDB's inte"
concepts: [folder-restructuring, taxonomy-mapping, git-mv, explicit-tradeoff-surfacing, non-destructive-defaults]
tags: [folder-restructuring, taxonomy-mapping, git-mv, explicit-tradeoff-surfacing, non-destructive-defaults]
created: 2026-08-06
indexed_at: 2026-08-06T03:35:04.367Z
updated_at: 2026-08-06T03:35:04.367Z
hash: sha256:b4a5a49969292569991d5b31ce7b1fa8740c6f322da7343e454189439d0e236c
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-06_when-two-organizing-schemes-for-the-same-content-d
arra_type: learning
arra_concepts: [folder-restructuring, taxonomy-mapping, git-mv, explicit-tradeoff-surfacing, non-destructive-defaults]
arra_created: 2026-08-06T03:35:04.367Z
---

# When two organizing schemes for the same content don't map 1:1 (e.g. CRDB's inte

When two organizing schemes for the same content don't map 1:1 (e.g. CRDB's internal 9-pillar folder taxonomy vs. DCCE's requested 9-item deliverable list, where one item spans four pillar folders), don't default to treating a "restructure" request as a simple rename. Surface the actual shape of the mismatch and let the user choose the execution approach explicitly, since keep-and-index vs. full-physical-merge trade off very differently in risk and cost.

Also: git mv on Windows/Git does not auto-create nested destination parent directories. `git mv old_folder new_parent/new_folder` fails with "fatal: renaming ... No such file or directory" if new_parent/ doesn't exist yet — always mkdir -p the parent first when moving into a new nested path.

---
*Added via Oracle Learn*
