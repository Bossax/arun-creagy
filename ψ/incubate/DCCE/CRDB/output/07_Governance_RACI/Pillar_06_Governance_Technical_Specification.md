# Technical Specification: Pillar 6 - Governance Operating Model (RACI) + Division Buy-in Execution Plan

## 0. Purpose (DAMA-aligned, time- and resource-bounded)

Pillar 6 is not only a role chart. It is the **execution plan** to secure division-wide buy-in so governance does not become stale shelfware.

Given limited time and resources, the objective is to **close the major pitfalls** of stale governance by locking:

1. **Decision rights** (who can approve what)
2. **Operational cadence** (when decisions happen)
3. **Minimum viable artifacts** (what must exist so work is repeatable)
4. **Escalation + conflict resolution** (how stalemates are resolved)
5. **Traceability** (what was decided, when, by whom)

This aligns with the project’s “architectural baseline before implementation” stance: [`ψ/incubate/DCCE/CRDB/inbox_source/The Enterprise Data System Development Lifecycle.md`](ψ/incubate/DCCE/CRDB/inbox_source/The%20Enterprise%20Data%20System%20Development%20Lifecycle.md:64).

## 1. Technical Requirements

### 1.1 Artifact set (minimum viable governance package)

*   **Primary Artifact A**: Stewardship RACI Matrix (who owns what)
    * **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv)
*   **Primary Artifact B**: Governance Buy-in Execution Plan (how governance runs)
    * **File Type**: Markdown (.md) + optional spreadsheet annex
*   **Primary Artifact C**: Decision Log (traceability spine)
    * **File Type**: Markdown (.md) or spreadsheet

### 1.2 Mandatory schema — RACI matrix

*   **`Data_Domain_ID`**: Identifier for the domain (aligned to Pillar 1 subject areas).
*   **`Steward_Role`**: The DCCE sub-division/position responsible for day-to-day authoring/verifying.
*   **`Approval_Authority`**: The executive role required for formal ratification.
*   **`Consulted_Agencies`**: External stakeholders involved (as-needed).
*   **`Technical_Custodian`**: Entity responsible for system operations (future implementer / contractor).

### 1.3 Mandatory schema — execution plan (buy-in mechanics)

The execution plan must define:

*   **Operating cadence**:
    * Weekly/biweekly **Steward Review** (working-level)
    * Monthly **Division Governance Review** (approval + escalations)
*   **Decision categories** (minimum set), mapped to the 5 gates (Pillar 5):
    * G1 classification / rail assignment
    * G2 metadata minima exceptions
    * G3 endorsement authority + “recommended baseline” decisions
    * G4 canonical boundary + crosswalk ownership
    * G5 revision/maturity labels for event/impact records
*   **Onboarding workflow** for each steward role:
    * required reading (what to know)
    * the first 3 decisions they must complete (to avoid “no-op stewardship”)
*   **Escalation path**:
    * what triggers escalation (e.g., Contested reference set in Pillar 7)
    * timebox + who decides when timebox expires
*   **Handoff contract** to Project B:
    * which governance artifacts become contractual acceptance criteria for implementation.

## 2. Verification Criteria

*   **Authority alignment**: 100% of “Accountable” roles must be assigned to DCCE division-level leadership to ensure institutional sovereignty.
*   **Domain coverage**: The RACI must cover all Pillars and at minimum the CDM’s logical domains.
*   **Execution realism**: The execution plan must specify a cadence and named meeting owners. If cadence is missing, governance is considered non-operational.
*   **Decision traceability**: Every governance decision category must have a Decision Log entry template (date, decision, rationale, approver, affected artifacts).
*   **Integration with Pillar 4/7**:
    * Pillar 4 uses `Feasibility_Posture` per row and must have an escalation rule when posture stays `Unknown` beyond a defined timebox: [`ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_04_Interface_Map_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_04_Interface_Map_Technical_Specification.md:28)
    * Pillar 7 uses `Reference_Status` per entity and must have a resolution workflow for `Contested`: [`ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_07_Ref_Data_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_07_Ref_Data_Technical_Specification.md:26)

## 3. Implementation Constraints

*   **No-shelfware rule**: If governance cannot be executed with current resourcing, the plan must reduce scope rather than invent roles/cadence that will not run.
*   **Separation of concerns**:
    * Pillar 5 defines governance semantics (G1–G5 meanings).
    * Pillar 6 defines who decides + how decisions are made operationally.
*   **Procurement shield**: The implementation contractor must adopt the Pillar 6 decision rights + workflow as contractual non-negotiables.
*   **Avoid overclaim**: Pillar 6 defines *workflows and decision rights*; it does not assume the existence of fully implemented automation until Project B.
