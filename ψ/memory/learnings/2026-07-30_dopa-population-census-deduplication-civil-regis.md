---
id: learning_2026-07-30_dopa-population-census-deduplication-civil-regis
type: learning
title: DOPA Population Census Deduplication & Civil Registration Multi-Office Reconcili
concepts: [dopa, census, deduplication, data_lineage, civil_registration, mutual_exclusivity]
tags: [dopa, census, deduplication, data_lineage, civil_registration, mutual_exclusivity]
created: 2026-07-30
indexed_at: 2026-07-30T17:04:22.275Z
updated_at: 2026-07-30T17:04:22.275Z
hash: sha256:93b207f3342c56ba6a060feae20935ab19e61547e292fa1a771ed8fbba5ff785
source: Session Retrospective v4.3 Release Audit
project: github.com/bossax/arun_creagy
arra_id: learning_2026-07-30_dopa-population-census-deduplication-civil-regis
arra_type: learning
arra_concepts: [dopa, census, deduplication, data_lineage, civil_registration, mutual_exclusivity]
arra_created: 2026-07-30T17:04:22.275Z
---

# DOPA Population Census Deduplication & Civil Registration Multi-Office Reconcili

DOPA Population Census Deduplication & Civil Registration Multi-Office Reconciliation Logic: In DOPA population census files (pop67.csv), multiple rows exist for a single 6-digit subdistrict (ตำบล) when residents are split across District Offices (สำนักทะเบียนอำเภอ...) and Local Municipal Offices (สำนักทะเบียนท้องถิ่นเทศบาล...). Because DOPA enforces strict unique 13-digit National ID primary key constraints in house books (ทร.14), populations across registry offices are 100% mutually exclusive partitions (empirically proven: national leaf sum matches DOPA row 0 to the exact single person 65,951,210). Never use drop_duplicates() or discard municipal rows; always perform groupby(['year_be', 'province_code', 'subdistrict_code']).agg({'population_total': 'sum', 'household_total': 'sum'}) to yield true 100% subdistrict totals.

---
*Added via Oracle Learn*
