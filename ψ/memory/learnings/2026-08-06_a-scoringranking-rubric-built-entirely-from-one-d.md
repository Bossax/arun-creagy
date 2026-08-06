---
id: learning_2026-08-06_a-scoringranking-rubric-built-entirely-from-one-d
type: learning
title: "A scoring/ranking rubric built entirely from one data source's own metadata is n"
concepts: [evidence-grounding, scoring-methodology, rubric-design, crdb]
tags: [evidence-grounding, scoring-methodology, rubric-design, crdb]
created: 2026-08-06
indexed_at: 2026-08-06T15:26:22.122Z
updated_at: 2026-08-06T15:26:22.122Z
hash: sha256:93ea4d7f34b05e1cf4da919ca16ba08babbba986745aecef87242e4432908f02
source: "rrr: crdb-wp2-scoring-rubric-rejected-and-rebuilt"
arra_id: learning_2026-08-06_a-scoringranking-rubric-built-entirely-from-one-d
arra_type: learning
arra_concepts: [evidence-grounding, scoring-methodology, rubric-design, crdb]
arra_created: 2026-08-06T15:26:22.122Z
---

# A scoring/ranking rubric built entirely from one data source's own metadata is n

A scoring/ranking rubric built entirely from one data source's own metadata is not independent evidence — it's the source re-describing itself. In CRDB WP2, a 5-criterion rubric for ranking 260 catalog rows (sector tags, hazard-count, geo coverage, data maturity, service linkage) collapsed under scrutiny: every criterion either read the catalog's own tags back as "importance," or relied on a service report (D-043) that named no concrete datasets at all. One criterion was actively backwards (treated national/coarse coverage as more valuable, when the source document explicitly asked for finer sub-district granularity). The fix was finding genuinely independent evidence — concrete, quotable demand statements in a different document — and scoring against that instead. Rule of thumb: before proposing a scoring method, check whether any criterion just restates the object being scored in different words. If a domain expert asks "how do you know" about several criteria in a row, treat it as a signal the whole approach needs re-grounding, not that each criterion needs a slightly better defense.

---
*Added via Oracle Learn*
