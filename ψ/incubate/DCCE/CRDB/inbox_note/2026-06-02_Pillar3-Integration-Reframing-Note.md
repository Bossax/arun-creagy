# Strategic Enhancement Note: Reframing Pillar 3 (Data Inventory)

**Date**: 2026-06-02
**Context**: Post-hardening of Pillar 2 (Use Cases) and Pillar 5 (CDM)
**Target**: Pillar 3 (Baseline Data Inventory & Information Product Inventory)

## 1. The Core Realization
Pillar 3 is currently designed as a "flat ledger" to satisfy TOR requirements. However, following the hardening of the functional baseline (Pillar 2) and the logical data model (Pillar 5), Pillar 3 must be reframed. 

A flat list of datasets is not actionable for a System Integrator. Pillar 3 must become a **"Dependency Roadmap"**—a Source-to-Target mapping that tells the Integrator exactly *which* data builds *which* entity to satisfy *which* use case.

## 2. Proposed Structural Enhancements (For Future Implementation)

When we return to harden Pillar 3, we should implement the following structural additions to the inventory schemas:

### A. The "Inventory-to-Entity" Mapping (Integrator Usability)
*   **Action**: Add a `CDM_Entity_Link` field to the Baseline Data Inventory.
*   **Purpose**: Every dataset must specify which Pillar 5 Entity it populates (e.g., TMD Rainfall data is an implementation of the `HAZARD_EVENT` entity). This converts a static list into an executable data pipeline map.

### B. The "Priority-by-Use-Case" Matrix (DCCE Usability)
*   **Action**: Add a `Use_Case_Criticality` field mapping back to UC-01 through UC-10.
*   **Purpose**: If a dataset supports a Phase 1 MVP (like UC-01 or UC-02), it is Tier 1 priority for DCCE data acquisition. If it supports a deferred use case (UC-06), it is Tier 3.

### C. Shift from "Measurement" to "Enforceable Requirements"
*   **Action**: Rather than attempting to measure Data Quality (DQ) now, define the **Minimum Quality Bars** as Acceptance Criteria for the integrator.
*   **Example**: "To satisfy UC-02, the Tambon population dataset must have 100% coverage of all 7,255 spatial units."

## 3. The "Zero-Discovery" Data Audit Buckets
To provide a clear status view to DCCE management, Pillar 3 should categorize all data into three readiness states:

1.  **Green (Ready)**: Validated source + Mapped to CDM + Supports Phase 1 Use Case.
2.  **Yellow (Acquisition Gap)**: Known source but assumed/unvalidated + Mapped to CDM + Supports Phase 1 Use Case (Signals an urgent need for an MOU or inter-agency request).
3.  **Red (Roadmap)**: Mapped to a Phase 2 or Deferred Use Case.

## 4. Next Steps
When Pillar 3 is opened for hardening, use this note to update the `Pillar_03_DataInventory_DQ_Technical_Specification.md` and enforce these relational columns in the resulting CSV templates.