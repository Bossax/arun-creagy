---
installer: arra-oracle-skills-cli v1.0.0
origin: Project-local hardened version for Windows/ψ stability.
name: trace
description: '[local] Hardened v1.1.0 | The Lens: Unstructured forensic discovery across the Oracle brain. Maps technical ancestry and generates T-E-D-A hypotheses.'
argument-hint: "<query> [--oracle | --smart | --deep]"
---

# /trace (The Lens)

> "Discover reality. Map the ancestry. Hypothesize the why."

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
    Write-Warning "Not in oracle repo (no GEMINI.md + ψ/). Writing to current directory."
    $PSI = (Get-Location).Path
}
```

---

## 🛡️ The Workflow (The Forensic Lens)

### Step 1: Search Waves (The Engine)
Run discovery using the existing forensic tools. Do NOT skip waves; the value of a trace is in its exhaustive depth.
- **Wave 1 (Oracle)**: `arra_search` (hybrid mode) to find principles and patterns.
- **Wave 2 (Files)**: `grep_search` across `ψ/incubate/`, `ψ/memory/`, and project directories to find orphaned notes.
- **Wave 3 (Sessions)**: Call `python .gemini/skills/trace/scripts/dig.py` to extract raw strings from `session.jsonl` logs.

### Step 2: Logging (The Archive & Database)
1. **Physical Log**: Write the raw findings to `ψ/memory/traces/YYYY-MM-DD/HHMM_[query].md`.
   - Include clickable Windows paths (e.g., `C:/...`).
   - Calculate a **Friction Score** based on the distance between the query and the evidence found.
2. **Database Registration**: You MUST call the `arra_trace` tool with the query and the list of discovered files/sessions.
   - Capture the returned `traceId`.
   - Record this `traceId` in the markdown file header for future bonding.

### Step 3: Synthesis (The T-E-D-A Hypothesis)
Every trace MUST conclude with a **Hypothesis** block. This translates unstructured "mess" into potential project ledgers.

> [!important]
> **Artifact vs. Motive Separation**: Files (PDFs, scripts, notebooks) are **Evidence (E)**. The insight or mandate derived from them is the **Trigger (T)**. Never log a file path as a Trigger.

**Markdown Section Template**:
```markdown
### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: [The conceptual "Why" discovered in the trace]
- **[E] Supporting Evidence**: [File Path A], [File Path B]
- **[D] Potential Decision**: [The strategy/posture this trace seems to validate]
- **[A] Target Asset**: [The file this trace was investigating]
```

---

## 📜 Hard Rules

1. **Lens Only**: Do NOT use `replace` or `write_file` on project ledgers (e.g., `ψ/incubate/`).
2. **Nothing is Deleted**: Every trace generates a new file. Never overwrite old traces.
3. **Zero Trust**: Assume nothing about project history until you see a physical file or a session string.
4. **Handoff Prompt**: Upon completion, you MUST state: *"Trace complete. Findings logged to [Path]. If you wish to formalize these yields into the project ledgers, run `/seal`."*

---

**Philosophy**: Discover reality. Map the ancestry. Hypothesize the why. *"Trace to understand; Seal to commit."*
