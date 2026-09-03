# Stage 4 lint exceptions — crdb-full-report-3.1 (Post-Polish)

Following the 2026-09-03 Two-Way Precision Polish pass, Table 3 has been fully regularized:
- `ไม่ใช่เพียง` × 2 has been eliminated (rephrased using formal Thai comparative structures).
- `NCAIF` / `NCAI` × 4 has been replaced with the canonical short form `โครงสร้างข้อมูลฯ`.
- `อย่างชัดเจน` × 1 has been eliminated.

The only remaining mechanical lint item is:

## [LEXICON] 'ฉบับ' (as part of 'รายงานฉบับกลาง')

**Location:** Prose (paragraphs 17, 19, 33), multiple occurrences of the proper document name "รายงานฉบับกลาง" (the Interim Report).

**Why not fixed:**
- This is an immutable contractual proper noun mandated by `writing-contract.json` (Line 14: *"ห้ามใช้คำว่า 'ฉบับ' แทนคำว่า 'รายการ' เมื่อเป็นส่วนหนึ่งของชื่อเอกสาร ('รายงานฉบับกลาง' เป็นชื่อเฉพาะ ห้ามแก้เป็น 'รายงานระหว่างกลาง' หรือรูปแบบอื่น)"*).
- The lexicon rule `"ฉบับ" -> "รายการ"` was created specifically to eliminate `ฉบับ` as a counting classifier for deliverables, not to corrupt proper document titles.

**Disposition:** Contractually protected proper noun exception, not a defect. Ready for Stage 5 editorial review.
