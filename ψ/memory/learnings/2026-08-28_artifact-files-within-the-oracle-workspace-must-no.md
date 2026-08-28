---
id: learning_2026-08-28_artifact-files-within-the-oracle-workspace-must-no
type: learning
title: "Artifact files within the Oracle workspace must not use `ArtifactMetadata` durin"
concepts: [rrr, writing-th, workflow]
tags: [rrr, writing-th, workflow]
created: 2026-08-28
indexed_at: 2026-08-28T04:04:48.878Z
updated_at: 2026-08-28T04:04:48.878Z
hash: sha256:c77b5b0ee2cb6079b212f6364008c32fb1807971943e63499b8d6a4632ab7514
source: rrr on crdb-exec-summary-2.2-drafting
arra_id: learning_2026-08-28_artifact-files-within-the-oracle-workspace-must-no
arra_type: learning
arra_concepts: [rrr, writing-th, workflow]
arra_created: 2026-08-28T04:04:48.878Z
---

# Artifact files within the Oracle workspace must not use `ArtifactMetadata` durin

Artifact files within the Oracle workspace must not use `ArtifactMetadata` during `write_to_file` to ensure they stay on the filesystem, not the brain directory. Also, `editorial_gate.py verify` strictly requires a non-empty `reviewer` field, even in degraded `self` review mode.

---
*Added via Oracle Learn*
