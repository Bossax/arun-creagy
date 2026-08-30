---
id: learning_2026-08-30_lesson-2026-08-30-a-prose-instruction-marked-m
type: learning
title: "Lesson (2026-08-30): a prose instruction marked \"MANDATORY\"/\"CRITICAL\" inside a"
concepts: [style-capture, writing-th, skill-architecture, rationale-gate, forcing-function]
tags: [style-capture, writing-th, skill-architecture, rationale-gate, forcing-function]
created: 2026-08-30
indexed_at: 2026-08-30T08:16:32.985Z
updated_at: 2026-08-30T08:16:32.985Z
hash: sha256:070a77b90c4544e330fc1bb085d0f6d70dbc5e8b34e1fd8751605783083a7b82
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-30_lesson-2026-08-30-a-prose-instruction-marked-m
arra_type: learning
arra_concepts: [style-capture, writing-th, skill-architecture, rationale-gate, forcing-function]
arra_created: 2026-08-30T08:16:32.985Z
---

# Lesson (2026-08-30): a prose instruction marked \"MANDATORY\"/\"CRITICAL\" inside a

Lesson (2026-08-30): a prose instruction marked "MANDATORY"/"CRITICAL" inside a skill file is not a forcing function -- it competes with everything else in context and loses under load. In a live /style-capture run on CRDB §4.1, the "zero-drop lexical scan" was skipped despite being labeled mandatory (only paragraph-level cuts caught, word-level swaps missed until the user asked directly). Separately, three patterns got promoted into STYLE_PACK_TH.md on inferred rationale rather than asked rationale -- one was the user filling in a domain fact (risked teaching future drafts to fabricate detail, violating writing-th's no-fabricated-sources rule), one was a one-off scope decision misclassified as a reusable pattern. This repeated a third time even during the planning phase for the fix, showing "act on inference instead of pausing to ask" is a default that reasserts itself unless something external interrupts it.

Fix implemented: diff_word_table.py (computed word-diff table replaces "scan by eye"), a rationale-gate `status` column in register.py (mechanical/confirmed_generalizable/one_off/content_correction) gating promotion independently of sighting count, a required AskUserQuestion step (SKILL.md step 4c) before any non-mechanical promotion, and check_lexicon_conflict.py/check_term_propagation.py for a related instance (a new lexicon entry silently conflicted with a pre-existing mapping for the same concept).

Generalizable takeaway: any skill step whose failure mode is "the agent skips/guesses under load" needs a script producing something concrete to react to, not stronger wording. Careful inference from a diff cannot recover intent that was never in the diff -- that risk needs asking to be required, not inference to be more careful.

---
*Added via Oracle Learn*
