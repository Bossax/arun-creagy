# §3.2 Merge + Polish Verification Notes

Sources: `crdb-exec-summary-2.2/draft.md` (EX 2.2, methodology/workshop) + `output/draft_final_report/5.3/5.3.2...md` (DFR, interview synthesis). Merged and polished via qwen3.6-plus for lift paragraphs, with the intro and closing bridge composed directly (grounded entirely in the two source paragraphs, no new facts). Per Boss's scope: interview + workshop findings only, MVP/workflow-pattern sections dropped, use-case→service mapping reserved for §3.3.

## Org count resolved: 11, not 12

Investigated a discrepancy where EX 2.2 states "12 หน่วยงาน" but DFR 5.3.2 lists 11 named organizations. Traced to the primary evidence table `2026-03-25-5.3.2-Interview-Coverage-Table.md` (INT-01–INT-11, each with a specific date and Appendix ง anchor), whose own summary states "Total interviews represented... 11." EX 2.2's own evidence-traceability file already flags this and instructs against using any number but 11. Boss confirmed: keep 11.

## Corrected before merge

1. **[E] over-corrected "ไม่ใช่เพียง"**: qwen first tried "และไม่ใช่รายละเอียดทางเทคนิค..." which dropped the "เพียง" (merely) nuance — turning "not merely a technical detail" into "not a technical detail at all." Rewrote manually to avoid the banned string while preserving the comparative meaning: "...มองว่าเป็นข้อกำหนดเชิงการใช้งานที่สำคัญยิ่งกว่ารายละเอียดทางเทคนิคของระบบฐานข้อมูล" (users see this as an operational requirement that matters *more than* a technical detail — same relative-importance claim, no banned scaffold).
2. **[H] clause reorder**: qwen swapped the order of two clauses within one sentence (moved "ต้องการชุดสรุป..." before "ไม่ต้องการเพียงหน้าค้นหา..."). Meaning was preserved but this violates the no-restructuring rule; reverted to original clause order.
3. **[D] full-name repeat**: qwen re-expanded "โครงสร้างข้อมูลฯ" to the full institutional name a second time; since the full name is already given once in the composed intro, this occurrence was shortened to "โครงสร้างข้อมูลฯ".
4. **"ห่วงโซ่" metaphor (banned, project-wide 2026-08-31 rule)**: both the composed intro (drawn from EX's "ห่วงโซ่การใช้ข้อมูล") and paragraph [A] (drawn from DFR's quoted "ห่วงโซ่ข้อมูล") used the banned chain metaphor. Neither is the exempted canonical citation ("ห่วงโซ่คุณค่าข้อมูล" / DCCE Data Value Chain.md), so both were rewritten with plain descriptive language ("เส้นทางการใช้ข้อมูล", "ลำดับขั้นการใช้ข้อมูล").
5. **"ผู้ดูแลข้อมูล" → "บริกรข้อมูล"** (Boss's Data Steward gloss, project-wide) — applied in the composed intro.
6. **"รับผิดชอบ + bare noun/verb" nominalization** (mechanical rule) — fixed 2 occurrences: "รับผิดชอบระบบรายงานภัยพิบัติระดับชาติ" → "รับผิดชอบการรายงานภัยพิบัติระดับชาติ", and "รับผิดชอบสายรายงานเหตุภัยพิบัติ" (×2) → "รับผิดชอบการรายงานเหตุภัยพิบัติ".

## Accepted lint exceptions (not fixed — table content, copied verbatim)

- `NCAIF` × 5 (table cells, ตาราง 4)
- `สินทรัพย์` × 2 (table cells: "สินทรัพย์รายจุด", "พอร์ตสินทรัพย์")
- `ฉบับ` — the `รายงานฉบับกลาง` proper-name exception, same as §3.1 (this document name, not a counting classifier)

## Structural decisions carried out per Boss's scope

- Dropped entirely: DFR's four workflow patterns, all four MVPs, the MVP-phasing paragraph, and the access-constraint paragraph framed around MVP design.
- Kept the 40+ use-case count paragraph (EX) — names the case base and what each case specifies, but stops short of naming or mapping any of the eight services. Appended one bridging sentence pointing to §3.3 for that synthesis (grounded pointer, not new content).
- Table 4 (interview synthesis) carried verbatim from DFR, untouched.

## Outstanding

- Boss to review `polished-5.3.2-merged.md` and this notes file.
- No Stage 2 needed (pure P source material; the merge decisions were Boss-directed rather than argument-map-driven) — once approved, straight to Stage 5 (fresh, non-fork editorial reviewer).
