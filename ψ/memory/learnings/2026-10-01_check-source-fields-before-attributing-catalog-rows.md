---
pattern: Before naming an agency as the holder of a dataset from a catalog, read the row's source and notes fields as well as its owner field; if they disagree, treat ownership as unestablished and ask.
date: 2026-10-01
source: rrr: Arun_Creagy
concepts: [data-catalog, provenance, attribution, report-writing, review-receipts]
---

A catalog row can list an agency as owner while its source field names a different project report and its notes say "may come from" several agencies. In a CRDB report section, two rows of this kind (flood duration and depth) were written into a draft as DDPM holdings because the owner column said DDPM. The user asked who held the data, and the rows turned out to be modelled indicators from another project, with a different holder in a later catalog version.

Practical rules that transfer:
- Read owner, source, notes, date range and spatial level together. A date range running to 2100 marks model output, not observed records.
- When a later catalog version removes or reassigns a row, compare versions before reusing names from the older one.
- An independent review receipt binds to a file hash, so batch small fixes (lint words, wording) before asking for review; any edit after a pass forces a new review.
