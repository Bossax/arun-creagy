---
id: learning_2026-07-16_when-building-and-disaggregating-indicators-under
type: learning
title: When building and disaggregating indicators under incomplete data groups (such a
concepts: [demographics, data-disaggregation, indicator-completeness, data-lineage, ui-guards]
tags: [demographics, data-disaggregation, indicator-completeness, data-lineage, ui-guards]
created: 2026-07-16
indexed_at: 2026-07-16T05:17:04.317Z
updated_at: 2026-07-16T05:17:04.317Z
hash: sha256:701d713ac9c0b98d3900515f2958613e7fe4e333948b5b03d57f61664863373c
source: Oracle Learn
project: bossax/arun_creagy
arra_id: learning_2026-07-16_when-building-and-disaggregating-indicators-under
arra_type: learning
arra_concepts: [demographics, data-disaggregation, indicator-completeness, data-lineage, ui-guards]
arra_created: 2026-07-16T05:17:04.317Z
---

# When building and disaggregating indicators under incomplete data groups (such a

When building and disaggregating indicators under incomplete data groups (such as hazards missing financial relief data), keep calculation logic distinct. Rather than skewing composite indexes by imputing default averages or zeros for missing dimensions, restrict calculations to the complete subset and dynamically disable/hide the composite metrics in the user interface. For demographic proxies derived from administrative totals (like converting households to estimated population headcounts), perform disaggregated calculations on-the-fly and output a diagnostic conversion audit log containing granular ratios and fallback level tracking to preserve data lineage.

---
*Added via Oracle Learn*
