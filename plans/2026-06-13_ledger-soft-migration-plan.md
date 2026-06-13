# Soft Migration Plan: Transitioning to T-E-D-A

## Objective
Transition the existing CRI project ledgers from the legacy T-E-CH-D framework to the strict T-E-D-A (Trigger, Evidence, Decision, Asset) ontology. 

## Strategy: Frictionless Continuity
**We will NOT rename files or rewrite historical IDs.** Doing so would break hundreds of cross-references in the Oracle knowledge base and markdown files. Instead, we will perform an "in-place upgrade" of the headers, instructional metadata, and cognitive rules inside the existing files.

---

## Execution Steps

### 1. `CRI-Evidence-Registry.md` (The Artifacts)
*   **Current State**: Already aligned with the new ontology.
*   **Migration Action**: 
    *   Update the instructional header to explicitly state: *"This ledger holds physical artifacts ONLY. It does not hold motivations or triggers."*
*   **ID Format**: Remains `E-CRI-XXX`.

### 2. `CRI-Trigger-Log.md` (The Motives)
*   **Current State**: Sometimes conflates files with motives.
*   **Migration Action**:
    *   Change column header `Origin / source` &rarr; `Motive / Insight`.
    *   Update the instructional header: *"Never log a file path here. A Trigger is the kinetic realization or external mandate that forces a change. Link the Trigger to the files in the Evidence Registry."*
*   **ID Format**: Remains `T-CRI-XXX`.

### 3. `CRI-Change-Log.md` (The Decisions)
*   **Current State**: Describes actions ("Changes").
*   **Migration Action**:
    *   Update title to `# CRI Decision & Change Log`.
    *   Change column header `Change summary` &rarr; `Strategic Decision / Pivot`.
    *   Update the instructional header: *"This ledger represents the Semantic Lock. It records agreed-upon technical or strategic postures (Decisions), not just isolated actions."*
*   **ID Format**: Remains `CH-CRI-XXX` (to preserve historical links, treated cognitively as "Choice/Decision").

### 4. `CRI-Deliverable-Map.md` (The Assets)
*   **Current State**: Tracks corporate "Deliverables".
*   **Migration Action**:
    *   Update title to `# CRI Asset & Deliverable Map`.
    *   Update the instructional header: *"An Asset is the hardened physical reality of a decision (e.g., `app.py`, a hardened `.md` methodology file). Use this to track the final instantiation of the T-E-D-A chain."*
*   **ID Format**: Remains `D-CRI-XXX`.

---

## Post-Migration Impact

1.  **Zero Broken Links**: All existing references in `ψ/incubate/`, `ψ/memory/traces/`, and `ψ/memory/retrospectives/` remain completely intact.
2.  **Oracle Upgrade**: When the `/seal` skill parses these ledgers in the future, it will read the new instructional headers and automatically enforce the strict artifact/motive separation.
3.  **Human Clarity**: The ledgers will clearly guide human readers to distinguish between *why* something happened (Trigger) and *what* file proves it (Evidence).
