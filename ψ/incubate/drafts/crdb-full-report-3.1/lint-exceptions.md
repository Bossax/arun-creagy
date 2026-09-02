# Stage 4 lint exceptions — crdb-full-report-3.1

All 4 blocking items are confined to Table 3 (บัญชีภูมิทัศน์ผลิตภัณฑ์ข้อมูล), which per `verification-notes.md` is copied verbatim from the TOR 5.3.1 source and untouched by the polish pass, per the project's P-procedure (tables are evidence artifacts, not prose subject to lint normalization).

## [PATTERN] 'ไม่ใช่เพียง' × 2

**Location:** Table 3, column 4 ("นัยยะต่อโครงการ"), rows "เว็บไซต์หลักและระบบย่อยของกรม สส." and "ธรรมาภิบาลข้อมูลและการเข้าถึง"

**Why not fixed:** Inside the verbatim table cell copied from source; not prose.

## [LEXICON] 'NCAIF' / 'NCAI' × 4 (approx.)

**Location:** Table 3 cells. Row 1 col 4 carries a pre-existing source typo "NCAI" (missing the F).

**Why not fixed:** Verbatim table content; correcting the source typo would mean editing evidence text, not polish.

## [PATTERN] 'อย่างชัดเจน' × 1

**Location:** Table 3, row "ระบบข้อมูลและผลิตภัณฑ์จากหน่วยงานภายนอก", column 3

**Why not fixed:** Verbatim table content.

## [LEXICON] 'ฉบับ' (as part of 'รายงานฉบับกลาง')

**Location:** Prose, multiple occurrences of the proper document name "รายงานฉบับกลาง" (the Interim Report).

**Why not fixed:** This is a proper document name, not a counting classifier for deliverable items — the lexicon rule targets the latter. An earlier polish pass corrupted this to "รายงานระหว่างกลาง" via the same "ฉบับ→รายการ" swap rule firing on the wrong sense; it was reverted to the correct proper name (see `verification-notes.md` item 1).

**Disposition (all four items):** accepted exceptions, not defects. Carry forward into Stage 5 editorial review.
