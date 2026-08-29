---
id: learning_2026-08-29_retrospective-on-writing-th-v61-harness-style-ca
type: learning
title: "Retrospective on Writing-TH v6.1 Harness, Style-Capture Smart Diff, and Structur"
concepts: [rrr, writing-th, style-capture, structural-rules, smart-diff]
tags: [rrr, writing-th, style-capture, structural-rules, smart-diff]
created: 2026-08-29
indexed_at: 2026-08-29T10:02:43.576Z
updated_at: 2026-08-29T10:02:43.576Z
hash: sha256:01c71dcecfb99c8fa2dd917040d2166dd46a7fc2765fc9cbf1b7239b5acb9dc5
source: rrr on 17.02_writing-th-v6-style-capture-and-structural-rules
arra_id: learning_2026-08-29_retrospective-on-writing-th-v61-harness-style-ca
arra_type: learning
arra_concepts: [rrr, writing-th, style-capture, structural-rules, smart-diff]
arra_created: 2026-08-29T10:02:43.576Z
---

# Retrospective on Writing-TH v6.1 Harness, Style-Capture Smart Diff, and Structur

Retrospective on Writing-TH v6.1 Harness, Style-Capture Smart Diff, and Structural Rules Store (2026-08-29):
1. Smart Diff Resolution: Replaced fragile single 'git diff' in style-capture with a 3-tier resolution ladder (Working copy -> Git commit history -> Sibling baseline).
2. Structural Rules Store (L4/L5): Created STRUCTURAL_RULES_TH.json and validate_structural_rules.py for macro-structural document archetypes (4-question deliverable tables, parallel framework enumeration, finding-to-design bridges).
3. Layered Miss Register: Upgraded miss_register.db and register.py to track candidates by layer (lexical, regex, structural).
4. Stage 1 Integration: Wired th-argument-mapper to read STRUCTURAL_RULES_TH.json during argument-map.json construction.

---
*Added via Oracle Learn*
