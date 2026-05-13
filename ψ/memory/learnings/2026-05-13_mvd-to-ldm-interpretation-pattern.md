---
title: Interpreting Compliance Labels as Logical Models (MVD-to-LDM Pattern)
tags: [architecture, governance, compliance, data-modeling, crdb]
created: 2026-05-13
source: rrr: Arun_Creagy
---

# Interpreting Compliance Labels as Logical Models (MVD-to-LDM Pattern)

## Pattern
When a project is constrained by non-technical compliance labels (e.g., "Minimum Viable Dataset" or "MVD" from a Terms of Reference), treat the label as a **Logical Data Model (LDM)** rather than a flat dataset list.

## Logic
1. **Semantic Shielding**: Use the formal compliance term in executive summaries to maintain alignment with the contract/TOR.
2. **Structural Integrity**: Implement the requirement as a relational schema (e.g., Star Schema, normalized entities) to ensure data integrity and scalability.
3. **Bridge Entities**: Center the model on "Transaction" entities (e.g., a "Disaster Card") that link causal drivers (Scientific CID) to outcomes (Socio-economic Loss).

## Application in CRDB
- **Requirement**: "Draft MVD for climate-related disaster events."
- **Interpretation**: A Logical Data Model mapped to Sendai Framework Targets A-D.
- **Outcome**: A "PDNA-ready" reporting template that maintains referential integrity between hazards and impacts, preventing the creation of technically meaningless flat spreadsheets.

## Lesson
Never implement a "Dataset" requirement literally if it risks creating technical debt. Implement the *Model* that makes the dataset meaningful.
