---
id: learning_2026-07-22_when-promoting-an-app-from-a-development-folder-in
type: learning
title: When promoting an app from a development folder into an existing deployment repo
concepts: [git, deployment, filesystem-safety, verification, trust-recovery]
tags: [git, deployment, filesystem-safety, verification, trust-recovery]
created: 2026-07-22
indexed_at: 2026-07-22T07:13:45.637Z
updated_at: 2026-07-22T07:13:45.637Z
hash: sha256:559a6db4241f1b691bd54fa75fe5f1e0e2bdcc13b0a6300c1699d80c67640647
source: rrr: CRI v4.2 deploy recovery
project: github.com/bossax/arun_creagy
arra_id: learning_2026-07-22_when-promoting-an-app-from-a-development-folder-in
arra_type: learning
arra_concepts: [git, deployment, filesystem-safety, verification, trust-recovery]
arra_created: 2026-07-22T07:13:45.637Z
---

# When promoting an app from a development folder into an existing deployment repo

When promoting an app from a development folder into an existing deployment repository, never use destructive mirror synchronization unless the deletion set has been explicitly validated. Treat the deployment repo as the system of record: restore the repo first if its Git metadata is damaged, then use a one-way overlay copy that excludes `.git` and runtime artifacts, and finish with a file-count and hash-based source-versus-target verification before declaring the migration complete.

---
*Added via Oracle Learn*
