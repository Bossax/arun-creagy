---
installer: local
name: seal
description: Capture project progress by reconstructing audit-to-asset causality, proposing the sealed chain, and writing the ledgers only after approval.
argument-hint: "[--init | --dry-run]"
trigger: /seal
---

# /seal (Audit-to-Asset Chain)

> A project's truth is defined by its causality, not its claims.

## Oracle Root Detection (required — Windows / PowerShell)

Every skill that writes to [`ψ/`](ψ/) MUST detect the oracle root first.

```powershell
$ORACLE_ROOT = git rev-parse --show-toplevel 2>$null

if ($ORACLE_ROOT -and (Test-Path "$ORACLE_ROOT\GEMINI.md") -and (Test-Path "$ORACLE_ROOT\ψ")) {
    $PSI = Resolve-Path "$ORACLE_ROOT\ψ" | Select-Object -ExpandProperty Path
} elseif ((Test-Path "GEMINI.md") -and (Test-Path "ψ")) {
    $PSI = Resolve-Path "ψ" | Select-Object -ExpandProperty Path
    $ORACLE_ROOT = (Get-Location).Path
} else {
    Write-Error "CRITICAL: Not in oracle repo. /seal requires the ψ/ structure to function."
    return
}
```

---

## Workflow

### Phase 1 — Discovery

Do not ask the user for history. Reconstruct it from local evidence.

1. Run the local recap flow first for recent context:
   - [`/recap`](../recap/SKILL.md)
2. Read the most recent relevant artifacts from local history:
   - [`ψ/memory/traces/`](ψ/memory/traces/)
   - [`ψ/outbox/`](ψ/outbox/)
   - project notes under [`ψ/incubate/`](ψ/incubate/)
3. Cross-check the active asset with repository history:
   - `git log --stat`
   - `Get-ChildItem -Recurse` on the project area when needed

Extract:

- **Evidence (E)** from retrospective or diary-style notes
- **Trigger (T)** from handoff or pending items
- **Change (CH)** from the current strategic pivot
- **Deliverable (D)** from the target file or artifact

### Phase 2 — Traceability verdict

Present the reconstructed chain to the user and stop for approval.

> **Audit-to-Asset Chain Proposal**
> * **Evidence (E)**: [text] ([file path])
> * **Trigger (T)**: [text] ([file path])
> * **Change (CH)**: [current strategic pivot]
> * **Asset (D)**: [target file path]
>
> **Auditor Verdict**: [significant/minor] progress.
>
> **Options**:
> 1. **Seal** — seal the chain as proposed.
> 2. **Manual correction** — correct the E-T-CH-D links before sealing.

### Phase 3 — Sealing

Only after explicit approval:

1. If `--init`, copy [`TEMPLATE.md`](./TEMPLATE.md) into `ψ/incubate/<PROJECT>/` as the four canonical ledgers.
2. Update the ledgers in order:
   - `Evidence-Registry.md`
   - `Trigger-Log.md`
   - `Change-Log.md`
   - `Deliverable-Map.md`
3. Keep writes append-only and history-preserving.
4. Mark the deliverable as `Sealed` only after the chain is fully written.

---

## Ledger structure (T-E-CH-D)

Every project maintains these 4 files in [`ψ/incubate/<PROJECT>/`](ψ/incubate/):

| File | Role | Key columns |
| :--- | :--- | :--- |
| `Evidence-Registry.md` | Grounding | ID, Artifact, Type, Date, Main Topic, Gap Lens |
| `Trigger-Log.md` | Motive | ID, Evidence ID, Gap Description, Impact Zone, Deliverable ID |
| `Change-Log.md` | Design | ID, Trigger ID, Strategic Pivot, Design Commitment, Status |
| `Deliverable-Map.md` | Result | ID, Name, Pillar, Acceptance Gate, Status |

---

## Guardrails

- Preserve the approval gate before any sealing action.
- Preserve the ledger model and the causality chain.
- Prefer local, file-based discovery and traceability.
- Do not delete history; append and version instead.

---

**Philosophy**: Detect reality. Link causality. Harden the spine.

