---
id: learning_2026-08-10_when-a-readedit-mismatch-occurs-on-a-file-a-human
type: learning
title: "When a Read/Edit mismatch occurs on a file a human can edit directly (essentiall"
concepts: [file-state-verification, git-diff, tool-trust, debugging]
tags: [file-state-verification, git-diff, tool-trust, debugging]
created: 2026-08-10
indexed_at: 2026-08-10T16:22:18.900Z
updated_at: 2026-08-10T16:22:18.900Z
hash: sha256:2673da5ca3c439e429ced0a9d0997c9d6b9c5afc3506414194bd58dfe20d5cac
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-10_when-a-readedit-mismatch-occurs-on-a-file-a-human
arra_type: learning
arra_concepts: [file-state-verification, git-diff, tool-trust, debugging]
arra_created: 2026-08-10T16:22:18.900Z
---

# When a Read/Edit mismatch occurs on a file a human can edit directly (essentiall

When a Read/Edit mismatch occurs on a file a human can edit directly (essentially always, in this environment), run git status / git diff HEAD -- <file> before concluding a tool malfunctioned or hallucinated content. Reaching for "the tool fabricated this" is a more dramatic explanation than "the file changed on disk since I last read it," but the boring explanation is far more likely and costs one command to check. Never state a tool-failure diagnosis to the user before doing this cheap verification — it avoids building a false narrative on top of an unverified assumption.

---
*Added via Oracle Learn*
