# §3.1 Polish Verification Notes

Source: `output/draft_final_report/5.3/5.3.1 ทบทวนและสังเคราะห์....md` (30 KB, pure P — no argument map, no new evidence). Polished via qwen3.6-plus (per Boss's instruction), diffed paragraph-by-paragraph against source before merge, per the §2.2 Lane A lesson that a strict prompt does not guarantee zero drift.

## Corrected before merge (qwen introduced these, reverted to source-faithful wording)

1. **"รายงานฉบับกลาง" (the Interim Report, a proper document name) was corrupted to "รายงานระหว่างกลาง"** in 3 places (สถานการณ์นี้สอดคล้อง.../หลักฐานใน.../เชื่อมโยงกับหลักฐานใน...) — caused by my own prompt's "ฉบับ→รายการ" swap rule firing on a term it wasn't meant for (that rule is for counting deliverable items, not this document's name). Reverted to "รายงานฉบับกลาง" in all 3 spots.
2. **¶ "จากการสังเคราะห์ดังกล่าว..." lost its qualifying clause.** Original explicitly says the work does *not* mean the landscape is fully integrated ("ไม่ใช่การประกาศว่า...ได้รับการบูรณาการสมบูรณ์แล้ว"). Qwen's rewrite deleted that disclaimer and kept only the affirmative half — this phrasing doesn't even match the banned "ไม่ใช่เพียง" pattern (no "เพียง"), so the deletion was unforced. Restored the full original sentence verbatim.
3. **"ภูมิสถานะ" (table-caption sentence) was silently changed to "ภูมิทัศน์"** — not an approved swap. Reverted to "ภูมิสถานะ".
4. **"ถูกจัดวางให้มองเห็นเป็นภูมิทัศน์เดียว" lost the verb "มองเห็น"** in qwen's passive-voice cleanup. Restored "มองเห็น" while keeping the active-ish "ยังไม่มีการจัดวางให้..." phrasing.
5. **"เส้นทางการใช้งานที่ชัดเจน" lost the modifier "ที่ชัดเจน"** (not the banned "อย่างชัดเจน" pattern — a different construction, dropped without authorization). Restored.
6. **"มุ่งเน้น" → "เน้น"** — post-lint fix, redundant prefix per lexicon rule (this one was a legitimate catch, not reverted).

## Accepted lint exceptions (not fixed — documented per precedent)

The Stage 4 mechanical gate still flags 4 items, all inside the table (ตาราง 3), which per the P-procedure is copied verbatim and untouched by the polish pass:
- `ไม่ใช่เพียง` × 2 (table cells, col. 4, rows "เว็บไซต์หลักฯ" and "ธรรมาภิบาลข้อมูลฯ")
- `NCAIF` × 4 (table cells; note row 1 col. 4 has a pre-existing source typo "NCAI" without the F)
- `อย่างชัดเจน` × 1 (table cell, row "ระบบข้อมูลจากหน่วยงานภายนอก", col. 3)
- `ฉบับ` — this is now only the `รายงานฉบับกลาง` proper-name exception described above, not a table match

## Outstanding

- Boss to review this file and `polished-5.3.1.md` before it's merged into the chapter-3 assembly.
- No Stage 2 needed (pure P, no argument map) — once approved, this goes straight to Stage 5 (fresh, non-fork editorial reviewer).
