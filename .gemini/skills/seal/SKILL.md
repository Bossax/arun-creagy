---
installer: arra-oracle-skills-cli v26.5.16
origin: ARUN (Strategic Knowledge Auditor)
name: seal
description: '[project] v26.5.16 G-SKLL |Capture project progress by auditing the recent progress on the current issue and proposing the reconstructed progression timeline.'
argument-hint: "[--init | --dry-run]"
trigger: /seal
---

# /seal (The Audit-to-Asset Chain)

> "A project's truth is defined by its causality, not its claims."

## Oracle Root Detection (REQUIRED — win32/PowerShell)

**Every skill that writes to ψ/ MUST detect the oracle root first.**

```powershell
# Step 1: Find git root
$ORACLE_ROOT = git rev-parse --show-toplevel 2>$null

# Step 2: Cross-check — oracle repo has GEMINI.md + ψ/
if ($ORACLE_ROOT -and (Test-Path "$ORACLE_ROOT\GEMINI.md") -and (Test-Path "$ORACLE_ROOT\ψ")) {
    $PSI = Resolve-Path "$ORACLE_ROOT\ψ" | Select-Object -ExpandProperty Path
} elseif ((Test-Path "GEMINI.md") -and (Test-Path "ψ")) {
    $PSI = Resolve-Path "ψ" | Select-Object -ExpandProperty Path
    $ORACLE_ROOT = (Get-Location).Path
} else {
    Write-Error "CRITICAL: Not in oracle repo. /seal REQUIRES ψ/ structure to function."
    return
}
```

---

## 🛡️ The Workflow (Senior Auditor Protocol)

### Phase 1:  Discovery
Do NOT ask the user for the history. Find it yourself in the Oracle Brain.

1.  **Semantic Search**: Call `arra_search(query: "recent retrospectives and handoffs for <PROJECT_NAME>")`.
2.  **Intent Parsing**: Read the content of the last 3-5 discovered files.
    - Extract **Evidence (E)** from `AI Diary` or `Lessons Learned`.
    - Extract **Trigger (T)** from `Next Steps` or `Pending` handoff items.
3.  **Physical Cross-Check**: Run `git log --stat` and `ls -R` to identify the current **Asset (D)** being sealed.

### Phase 2: The Traceability Verdict
Present the reconstructed chain to the user. **Wait for Approval.**

> **Audit-to-Asset Chain Proposal**
> *   **Evidence (E)**: [Text from Retro/Search] ([File Path])
> *   **Trigger (T)**: [Text from Handoff/Search] ([File Path])
> *   **Change (CH)**: [Current Strategic Pivot]
> *   **Asset (D)**: [Target File Path]
> 
> **Auditor Verdict**: [Significant/Minor] progress.
> 
> **Options**:
> 1. **Seal**: Seals the chain as proposed.
> 2. **Trace Escalation**: If this proposal misses the "essence," use the **Trace Skill** (`arra_trace`) to perform a deep forensic dig. This will discover technical ancestry (files, commits, history) from the filesystem directly.
> 3. **Manual Correction**: Correct the E-T-CH-D links manually.

### Phase 2.5: Trace Escalation
If triggered:
- Run the **Trace Skill** (`arra_trace`) on the active asset.
- Analyze the discovered **Dig Points** (files and commits) to find the "hidden" causality.
- Re-propose the chain based on this technical discovery.

### Phase 3: Sealing
Upon approval, perform the following in order:

1.  **Initialize (if --init)**: Copy `.gemini/skills/seal/TEMPLATE.md` to `ψ/incubate/<PROJECT>/` as the 4 canonical ledgers.
2.  **Sequential Write**:
    - Update `Evidence-Registry.md`
    - Update `Trigger-Log.md`
    - Update `Change-Log.md`
    - Update `Deliverable-Map.md` (Mark as "Sealed")
3.  **Oracle Hardening**: Call `arra_trace` to log the Sealing Event as a permanent record.
4.  **Trace Linking**: Call `arra_trace_link` to bond the discovered ancestors to this "Sealing Trace."

---

## 📜 Ledger Structure (T-E-CH-D)

Every project MUST maintain these 4 files in `ψ/incubate/<PROJECT>/`:

| File | Role | Key Columns |
| :--- | :--- | :--- |
| **Evidence-Registry.md** | The Grounding | ID, Artifact, Type, Date, Main Topic, Gap Lens |
| **Trigger-Log.md** | The Motive | ID, Evidence ID, Gap Description, Impact Zone, Deliverable ID |
| **Change-Log.md** | The Design | ID, Trigger ID, Strategic Pivot, Design Commitment, Status |
| **Deliverable-Map.md** | The Result | ID, Name, Pillar, Acceptance Gate, Status (Draft/Sealed) |


---
**Philosophy**: Detect reality. Link causality. Harden the spine. *"A project's truth is defined by its causality, not its claims."*
