---
id: learning_2026-09-30_when-wiring-newly-introduced-shared-skills-into-co
type: learning
title: "When wiring newly introduced shared skills into consumer projects on Windows: (1"
concepts: [rrr, shared-skills, junction, git-submodule, powershell]
tags: [rrr, shared-skills, junction, git-submodule, powershell]
created: 2026-09-30
indexed_at: 2026-09-30T04:31:14.426Z
updated_at: 2026-09-30T04:31:14.426Z
hash: sha256:18af37239857d5a51b5f45ab4cf407be0db76ea9ea30d217abb859bedad7b078
source: rrr on sync-oracle-shared-skills-v1.4.0
arra_id: learning_2026-09-30_when-wiring-newly-introduced-shared-skills-into-co
arra_type: learning
arra_concepts: [rrr, shared-skills, junction, git-submodule, powershell]
arra_created: 2026-09-30T04:31:14.426Z
---

# When wiring newly introduced shared skills into consumer projects on Windows: (1

When wiring newly introduced shared skills into consumer projects on Windows: (1) New-Item -ItemType Junction strictly requires an absolute path for -Target, unlike symlinks which accept relative paths. (2) Because .agents/skills/ acts as a physical mirror for scanner compatibility (Antigravity/Codex), newly added shared skills must be appended to the consumer repository's .gitignore to prevent untracked mirror copies from polluting git status. (3) Run sync-skills.ps1 and sync-global-agents.ps1 immediately after fast-forwarding the submodule to maintain lockstep parity across all agent scan paths.

---
*Added via Oracle Learn*
