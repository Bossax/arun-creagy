---
id: learning_2026-07-22_when-working-with-thai-demographic-data-dopa-su
type: learning
title: When working with Thai demographic data (DOPA), subdistrict codes (Tambon) are o
concepts: [data-cleaning, data-lineage, join-fanout, normalization, demographics]
tags: [data-cleaning, data-lineage, join-fanout, normalization, demographics]
created: 2026-07-22
indexed_at: 2026-07-22T13:57:11.414Z
updated_at: 2026-07-22T13:57:11.414Z
hash: sha256:ca2c1c2e24c9baa200d098e1953a7d3fac32db3a38557237d54d1e9ff696751a
source: Arun
arra_id: learning_2026-07-22_when-working-with-thai-demographic-data-dopa-su
arra_type: learning
arra_concepts: [data-cleaning, data-lineage, join-fanout, normalization, demographics]
arra_created: 2026-07-22T13:57:11.414Z
---

# When working with Thai demographic data (DOPA), subdistrict codes (Tambon) are o

When working with Thai demographic data (DOPA), subdistrict codes (Tambon) are often split into separate records for different administrative authorities (e.g. Municipality/เทศบาล vs. SAO/อบต.) in a single subdistrict. If merged directly with hazard statistics, it creates a join fan-out, multiplying metrics in aggregations. The core pattern to prevent this is implementing a strict consolidation step: group and sum both population and household counts by `(subdistrict_code, year_be)` at the very beginning of the pipeline (both in the silver generation script and the exporter merges).

---
*Added via Oracle Learn*
