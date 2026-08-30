---
id: learning_2026-08-30_lesson-check-existing-lexiconpack-rules-for-a-ma
type: learning
title: "Lesson: check existing lexicon/pack rules for a matching underlying principle be"
concepts: [style-capture, writing-th, lexicon, process-correction]
tags: [style-capture, writing-th, lexicon, process-correction]
created: 2026-08-30
indexed_at: 2026-08-30T09:16:35.087Z
updated_at: 2026-08-30T09:16:35.087Z
hash: sha256:96628dd08b82418982645ae01d3427897971b870e23f34cc08374560836ee447
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-30_lesson-check-existing-lexiconpack-rules-for-a-ma
arra_type: learning
arra_concepts: [style-capture, writing-th, lexicon, process-correction]
arra_created: 2026-08-30T09:16:35.087Z
---

# Lesson: check existing lexicon/pack rules for a matching underlying principle be

Lesson: check existing lexicon/pack rules for a matching underlying principle before treating a diff edit as a novel style-capture candidate. On CRDB §4.3 (2026-08-30), a "deliverable version tags dropped (DRD v2, CDM/DMF)" edit was put to Boss as an ambiguous new AskUserQuestion candidate when it was actually an application of an existing internal-artifact-locator rule already in LEXICON_TH.json (previously scoped only to slide/page locators). check_lexicon_conflict.py only does exact substring matching on banned/preferred term text -- it will never surface a match on the underlying principle, so its silence must not be read as "no related rule exists." Fix: before drafting a rationale-gate question, skim STYLE_PACK_TH.md's categorized sections and LEXICON_TH.json reasons (not just term strings) for a matching principle first. Also: when a rationale-gate answer corrects the hypothesis rather than picking an offered option (as happened on a second question this session, about a "passive->positive reframe" that was actually narrower -- "don't restate a self-evident premise as filler"), log the corrected framing in the capture-history file, not the original guess.

---
*Added via Oracle Learn*
