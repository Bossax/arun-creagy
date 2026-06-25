# Learning: Deep institutional report rewrites need evidence packets before prose

## Context

While rewriting CRDB Sections [`5.3.6`](../../../incubate/DCCE/CRDB/output/final_report/5.3/5.3.6%20ศึกษาและวิเคราะห์ระบบการรายงานสาธารณะภัยของหน่วยงานที่เกี่ยวข้องเทียบกับมาตรฐานสากล%20เพื่อนำมาระบุช่องว่างและนำมาออกแบบร่างมาตราฐานชุดข้อมูลขั้นต่ำ%20และร่างแบบฟอร์มการรายงานความสูญเสียและความเสียหาย%20ที่ตอบโจทย์การรวบรวมข้อมูลผลกระทบจากภัยพิบัติ.md) and [`5.3.7`](../../../incubate/DCCE/CRDB/output/final_report/5.3/5.3.7%20นำร่างมาตรฐานชุดข้อมูลขั้นต่ำ%20สำหรับเหตุการณ์ด้านสภาพภูมิอากาศมาทดลองรวบรวมข้อมูลตามมาตรฐานกำหนด%20โดยคัดเลือกการรวบรวมข้อมูลจากเหตุการณ์ที่เกิดขึ้นในอดีต.md), the first draft failed because it was conceptually reasonable but not evidence-sharp enough. The fix was to stop redrafting directly and instead build focused extraction artifacts for PDNA, standards, interoperability, DDPM context, and paragraph-level source-to-claim matrices.

## Pattern

For report sections that must survive expert review, use an evidence-packet workflow before rewriting:

1. split the weak section into evidence domains,
2. extract each domain into a focused note,
3. build a source-to-claim matrix for each section,
4. only then rewrite the final prose.

## Why it matters

Generic prose often comes from skipping the layer between source reading and sentence writing. When named frameworks, institutional workflow, and design logic must all appear precisely, the missing layer is usually not "better wording" but "better claim control." Evidence packets make the rewrite auditable and keep each paragraph tied to a specific source burden.

## Practical rule

When a human says a report section lacks depth, do not immediately expand the prose. First ask which evidence dimensions are underdeveloped, then create one extraction artifact per dimension, plus a paragraph-oriented claim matrix.

## Caution

Mode drift increases confusion during complex rewrites. If the job is multi-step evidence coordination ending in prose, the governing mode should be [`orchestrator`](orchestrator:1) even if the final act is writing.
