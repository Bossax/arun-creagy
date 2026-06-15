---
title: Pattern: When transforming workbook-derived datasets into analytical products, s
tags: [cri, normalization, lineage, trust, data-pipeline, notebook, html-explainer, workflow]
created: 2026-06-15
source: Oracle Learn
project: github.com/sitth/arun_creagy
---

# Pattern: When transforming workbook-derived datasets into analytical products, s

Pattern: When transforming workbook-derived datasets into analytical products, success depends on building a full trust chain, not just runnable code. The required chain is: Bronze extraction -> Silver normalization -> lineage documentation -> executable notebook -> visual HTML explainer. A key operational lesson is to separate and report four states explicitly: planned, patched, executed, and verified. If those states are blurred, the human is forced to audit whether work actually happened, which creates avoidable trust friction.

Specific learning from the CRI workbook bundle:
- Mixed-grain sources should not be prematurely flattened into a fake unified model. Population aggregates, proxy economic-loss tables, and partial heatwave coverage need explicit labeling instead of silent normalization.
- Province lookup bridge tables such as `province_code_lookup.csv` are worth materializing when the canonical geography spine is not operationally convenient for a specific workflow.
- Demonstration notebooks should clearly distinguish core score components from companion metrics. Example: heat mortality can be visualized without being included in the CRI score.
- Human-facing explanation layers matter as much as the data transforms themselves. A notebook plus an HTML explainer made the workflow legible in a way raw scripts and CSVs did not.

Generalizable lesson:
In complex analytical pipeline work, never claim completion at the level of "done" alone. Always say whether an artifact is only planned, patched in source, executed, or fully verified with outputs.

---
*Added via Oracle Learn*
