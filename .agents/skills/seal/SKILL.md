---
installer: "arra-oracle-skills-cli v26.6.0"
origin: "ARUN (Strategic Knowledge Auditor)"
name: "seal"
description: "[project] v26.6.0 G-SKLL | The Funnel: Commit unstructured discovery into structured T-E-D-A ledgers. Bonds the audit to the asset."
argument-hint: "[--init | --dry-run]"
trigger: "/seal"
---

# /seal (The T-E-D-A Funnel)

> "Trace to understand; Seal to commit. A project's truth is its causality."

## Oracle Root Detection (REQUIRED — win32/PowerShell)

**Every skill that writes to ψ/ MUST detect the oracle root first.**

```powershell
# Step 1: Find git root
$ORACLE_ROOT = git rev-parse --show-toplevel 2>$null

# Step 2: Cross-check — oracle repo has AGENTS.md + ψ/
if ($ORACLE_ROOT -and (Test-Path "$ORACLE_ROOT\AGENTS.md") -and (Test-Path "$ORACLE_ROOT\ψ")) {
    $PSI = Resolve-Path "$ORACLE_ROOT\ψ" | Select-Object -ExpandProperty Path
} elseif ((Test-Path "AGENTS.md") -and (Test-Path "ψ")) {
    $PSI = Resolve-Path "ψ" | Select-Object -ExpandProperty Path
    $ORACLE_ROOT = (Get-Location).Path
} else {
    Write-Error "CRITICAL: Not in oracle repo. /seal REQUIRES ψ/ structure to function."
    return
}
```

---

## 🛡️ The Workflow (The Audit Funnel)

### Phase 1: Intake & Discovery
Do NOT ask the user for history. Consume it from the brain.

1.  **Trace Intake**: Scan `ψ/memory/traces/` for any file created in the last 24 hours. Read the `### Potential Ledger Yields` section.
2.  **Retro Intake**: Call `arra_search(query: "recent retrospectives for <PROJECT>")`.
3.  **Motive vs. Artifact Split**: 
    - Identify the **Evidence (E)**: The physical files/paths discovered.
    - Identify the **Trigger (T)**: The conceptual motive or mandate derived from that evidence.
4.  **Target Asset (A)**: Identify the file or directory being hardened.

### Phase 2: The T-E-D-A Verdict
Present the reconstructed chain to the user. **Wait for Approval.**

> **Audit-to-Asset Chain Proposal (T-E-D-A)**
> *   **Trigger (T)**: [Conceptual Motive] (Linked to E-XXX)
> *   **Evidence (E)**: [File Path] ([Evidence ID])
> *   **Decision (D)**: [Agreed Posture/Semantic Lock]
> *   **Asset (A)**: [Hardened File Path] ([Deliverable ID])
> 
> **Auditor Verdict**: [Significant/Minor] progress.

### Phase 3: Sealing (Structural Commitment)
Upon explicit approval:

1.  **Initialize (if --init)**: Ensure `ψ/incubate/<PROJECT>/` has the 4 canonical ledgers.
2.  **Sequential Write**:
    - Update `Evidence-Registry.md` (Artifacts only).
    - Update `Trigger-Log.md` (Motives only; link to E-ID).
    - Update `Change-Log.md` (Decisions; link to T-ID).
    - Update `Deliverable-Map.md` (Mark Asset as "Sealed").
3.  **Database Bonding**: Call `arra_trace_link(prevId, nextId)` to bond the unstructured discovery trace to the formal sealing event.

---

## 📜 Hard Rules (v26.6.0 Mandate)

1.  **Motive/Artifact Separation**: Never log a file path in the Trigger ledger. A Trigger is the "Why"; Evidence is the "What".
2.  **Approval Gate**: You MUST present the T-E-D-A chain and wait for confirmation before writing to the project ledgers.
3.  **Historical IDs**: Always preserve the existing ID prefixing (E-CRI-XXX, T-CRI-XXX, CH-CRI-XXX, D-CRI-XXX).
4.  **Nothing is Deleted**: Do not overwrite ledger entries. Always append.

---

**Philosophy**: Detect reality. Link causality. Harden the spine. *"Trace to understand; Seal to commit."*
