---
id: learning_2026-09-22_check-git-logstatus-before-assuming-a-file-sync-b
type: learning
title: "Check git log/status before assuming a file-sync bug: when a tracked file's on-d"
concepts: [git, debugging, file-sync, concurrent-edits, diagnostics]
tags: [git, debugging, file-sync, concurrent-edits, diagnostics]
created: 2026-09-22
indexed_at: 2026-09-22T06:49:45.328Z
updated_at: 2026-09-22T06:49:45.328Z
hash: sha256:0b3097c3b39ecd56ef6f55ec490c6f0c068ba460b2d8699ea65530b4e89c375f
source: "rrr: Arun_Creagy"
arra_id: learning_2026-09-22_check-git-logstatus-before-assuming-a-file-sync-b
arra_type: learning
arra_concepts: [git, debugging, file-sync, concurrent-edits, diagnostics]
arra_created: 2026-09-22T06:49:45.328Z
---

# Check git log/status before assuming a file-sync bug: when a tracked file's on-d

Check git log/status before assuming a file-sync bug: when a tracked file's on-disk content doesn't match what a tool call just wrote, run `git log --oneline -3 -- <path>` and `git diff --stat HEAD -- <path>` before hypothesizing a sync bug or re-applying fixes. In a real session, "reverted" content on a tracked argument-map.json turned out to be the user committing his own direct edits to the same file in parallel with the session's tool-based edits -- discovered only after multiple confused re-reads, when git log should have been the first diagnostic step. Re-applying a guessed fix without first checking history risks clobbering the user's own concurrent edits.

---
*Added via Oracle Learn*
