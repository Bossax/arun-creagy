---
title: When a project is constrained by non-technical compliance labels (e.g., "Minimum
tags: [architecture, governance, compliance, data-modeling, crdb]
created: 2026-05-13
source: rrr: Arun_Creagy
project: github.com/sitth/arun_creagy
---

# When a project is constrained by non-technical compliance labels (e.g., "Minimum

When a project is constrained by non-technical compliance labels (e.g., "Minimum Viable Dataset" or "MVD" from a Terms of Reference), treat the label as a Logical Data Model (LDM) rather than a flat dataset list. This "Semantic Shielding" ensures structural integrity while maintaining alignment with the contract. Implement the requirement as a relational schema (e.g., Star Schema, normalized entities) centered on "Transaction" entities (e.g., a "Disaster Card") that link causal drivers (Scientific CID) to outcomes (Socio-economic Loss). Outcome: A "PDNA-ready" reporting template that maintains referential integrity, preventing the creation of technically meaningless flat spreadsheets.

---
*Added via Oracle Learn*
