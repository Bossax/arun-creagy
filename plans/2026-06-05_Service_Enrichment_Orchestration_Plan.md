# Operational Plan: NCAIF Service Enrichment & Forensic Gap Analysis

**Objective**: Transform 32 agency 'Demands' into 7 'Enriched Service Engines' and assess their 'Triple-Audit' readiness.
**Safety Mode**: YOLO (Autonomous with high-fidelity evidence anchors).
**Version**: 1.0 (Workflow Design)

---

## 1. Orchestration Architecture
To prevent "Context Drift" and "Hallucination," the task is split into three discrete agent-led phases.

### Phase A: The Forensic Extraction (Sub-Agent: `codebase_investigator`)
*   **Task**: Re-audit all 18+ sources (interviews, vtt, plans) to extract "Hard Technical Requirements" for every use case.
*   **Operational Detail**: Must capture specific parameters (e.g., "return period," "EA-level," "ISO code," "specific budget law name").
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json` (A flat list of 32+ demand-spec pairs).

### Phase B: The Requirement Synthesis (Sub-Agent: `generalist`)
*   **Task**: "Blend" the inventory into the 7 Services. Identify "Common Core" vs. "Contextual Modules."
*   **Operational Detail**: Grouping demands by service ID and looking for overlapping functional logic.
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Enriched_Service_Specs_v1.0.md`.

### Phase C: The Triple-Audit Readiness Check (Sub-Agent: `codebase_investigator`)
*   **Task**: Compare the "Enriched Specs" against the current "Supply" (Evidence Registry).
*   **Operational Detail**: Score each service (1-5) on Data, Legal, and Technical readiness. Identify the "Blocker of the Week."
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Readiness_Report_v1.0.md`.

---

## 2. Guardrails & Anti-Hallucination Protocol
1.  **Evidence Anchor**: Every claim in the Enriched Specs MUST be tagged with a `[Source ID]`. 
2.  **Logic Gate**: If a sub-agent cannot find a specific parameter (e.g., "What resolution does OTP need?"), it must label it `[DATA_GAP_CRITICAL]` instead of guessing.
3.  **Atomic Handoff**: No tasks are performed in parallel on the same file. Each sub-agent reads from the *Inbox* and writes to the *Incubate/Outbox*.

---

## 3. Immediate Execution Steps

| Step | Action | Responsibility | Status |
| :--- | :--- | :--- | :--- |
| **1** | Spawn `codebase_investigator` to audit sources for "Hard Specs" | Main Agent | **Ready** |
| **2** | Validate `P2_Hard_Dependencies_Inventory.json` against Extraction Matrix | Main Agent | Pending |
| **3** | Spawn `generalist` to "Blend" and draft Enriched Specs | Main Agent | Pending |
| **4** | Conduct final "Readiness Audit" | Main Agent | Pending |

---
**Request for Approval**: Should I initiate **Step 1** (Spawning the Investigator for Forensic Extraction)?
