---
title: When cloning external repositories into a knowledge vault (ψ/learn) for referenc
tags: [git, devops, best-practices]
created: 2026-05-25
source: Oracle Learn
project: github.com/soul-brews-studio/opensource-nat-brain-oracle
---

# When cloning external repositories into a knowledge vault (ψ/learn) for referenc

When cloning external repositories into a knowledge vault (ψ/learn) for reference, always remove the nested .git folder immediately. This prevents Git from tracking it as a 'gitlink' (mode 160000), which often causes 'modified content' friction due to line-ending conversions or local changes that aren't easily staged in the parent repo. Flattening the structure ensures the knowledge is fully versioned and managed by the main repository.

---
*Added via Oracle Learn*
