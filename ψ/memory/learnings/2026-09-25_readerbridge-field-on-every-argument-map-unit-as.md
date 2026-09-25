---
id: learning_2026-09-25_readerbridge-field-on-every-argument-map-unit-as
type: learning
title: "reader_bridge field on every argument-map unit (assumed_knowledge, opening_link,"
concepts: [writing-th, reader_bridge, editorial-review, cold-reader, self-narration, Thai-institutional-writing]
tags: [writing-th, reader_bridge, editorial-review, cold-reader, self-narration, Thai-institutional-writing]
created: 2026-09-25
indexed_at: 2026-09-25T02:02:13.670Z
updated_at: 2026-09-25T02:02:13.670Z
hash: sha256:184c65dae4b2186b453b12c8627c48048f87f7d14605c36569af993d881dff10
source: "rrr: Arun_Creagy"
arra_id: learning_2026-09-25_readerbridge-field-on-every-argument-map-unit-as
arra_type: learning
arra_concepts: [writing-th, reader_bridge, editorial-review, cold-reader, self-narration, Thai-institutional-writing]
arra_created: 2026-09-25T02:02:13.670Z
---

# reader_bridge field on every argument-map unit (assumed_knowledge, opening_link,

reader_bridge field on every argument-map unit (assumed_knowledge, opening_link, concept_explanation, project_application, transition_to_next) reduces but does not eliminate self-narrating Thai prose. Tested on CRDB §5.1 (25 units, full reader_bridge coverage): cold-reader review still found "หัวข้อนี้จะ..." style meta-commentary and a forecast-then-restate pattern at nearly every subsection boundary. Root cause: the field tells the verbalizer what connective tissue a paragraph needs, but nothing says that tissue must be dissolved into substance rather than stated as a sentence about the document itself. Fix: add an explicit rule that reader_bridge fields shape content/ordering but may never surface as a "this section will..." sentence, plus a lint pattern for "หัวข้อ...จะ/กล่าวถึง/ปิดท้ายด้วย" style meta-commentary. Separately: running a mechanical editorial-rubric review and a fresh cold-reader roleplay review in parallel (no shared context) caught different defects — the mechanical review found a formal number-reconciliation problem, only the cold reader caught the self-narration and a genuine label contradiction (same 40 items called both a quantitative and a methodological gap in different subsections). Neither alone was sufficient.

---
*Added via Oracle Learn*
