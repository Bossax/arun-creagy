---
id: learning_2026-08-13_explicit-target-priority-gate-for-user-reference
type: learning
title: "# Explicit Target Priority Gate for User-Referenced Paths"
concepts: [search, source-fidelity, user-pointer, template-discovery]
tags: [search, source-fidelity, user-pointer, template-discovery]
created: 2026-08-13
indexed_at: 2026-08-13T09:46:28.093Z
updated_at: 2026-08-13T09:46:28.093Z
hash: sha256:e903a0e294ce42bc97985ae4c7d29d6e96c38f8dcb7027f8bca4331051342759
source: User Correction / Learn Slash Command
arra_id: learning_2026-08-13_explicit-target-priority-gate-for-user-reference
arra_type: learning
arra_concepts: [search, source-fidelity, user-pointer, template-discovery]
arra_created: 2026-08-13T09:46:28.093Z
---

# # Explicit Target Priority Gate for User-Referenced Paths

# Explicit Target Priority Gate for User-Referenced Paths

Whenever the user explicitly mentions a file, folder, or path (e.g., @path, ψ/memory/, or explicit folder names) as a source, template, or reference:

1. Mandatory First Search: Inspect and read from the user-specified location BEFORE searching other project directories or synthesizing from unmentioned files.
2. Exhaust User-Specified Target: If a template or reference is expected in the specified directory, run targeted file discovery (grep_search, list_dir, view_file) inside that exact directory structure before looking elsewhere.
3. Transparent Fallback: If the specified target does not contain the needed file, explicitly inform the user of the finding before falling back to alternative project paths.

---
*Added via Oracle Learn*
