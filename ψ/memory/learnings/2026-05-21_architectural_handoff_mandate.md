---
title: The "Zero-Discovery" Mandate in Strategic Data Procurement
tags: [governance, procurement, architecture, handoff]
created: 2026-05-21
source: rrr: Arun_Creagy
---

# The "Zero-Discovery" Mandate: Bridging the Strategic-Technical Gap

In large-scale public sector data projects (e.g., the 25M THB DCCE Climate Risk Database), the most common failure mode is the **"Discovery Trap"**. This occurs when a technical contractor spends the first 12-18 months of a project "studying the domain," effectively rediscovering logic that the internal organization already knows. This leads to "Expert Drift," where the final system's logic (how a risk score is calculated) is owned by the vendor rather than the agency.

### Key Pattern: The Architectural Shield
To mitigate this, the "Strategic Audit" phase must produce a **Mandatory Inception Package** (The 8 Pillars) that acts as a technical shield.

1.  **Logical Anchor**: The organization must provide a hardened **Conceptual Data Model (CDM)** and **Business Glossary** *before* the procurement begins.
2.  **Zero-Discovery Clause**: The Terms of Reference (TOR) must contractually prohibit the contractor from conducting a new discovery phase. They are mandated to implement the provided models.
3.  **Role Separation**:
    *   **Strategic Architect**: Defines the "What" and "Why" (Logic Rules, Semantic Layer).
    *   **System Integrator**: Defines the "How" (Physical Database, ETL Code, API Layer).
4.  **Governance Handoff**: Internal stewardship must be established (e.g., the Nid Memo) to ensure internal domain experts have the authority to audit the contractor's code against the provided logic rules.

### Success Criterion
"Execution" in the strategic phase is measured by the **Physical Portability** of the output. If the output is a Word doc, it is a suggestion. If the output is a **SQL Schema (Pillar 1)** and a **Logic Test-Suite (Pillar 3)**, it is a **Mandate**.
