---
title: Learning: Atomic execution and ledger edit discipline
tags: [process, atomic-execution, governance, markdown, tables, traceability]
created: 2026-05-07
source: rrr: c:/Users/sitth/OracleWorkspace/Arun_Creagy
project: github.com/local/arun_creagy
---

# Learning: Atomic execution and ledger edit discipline

Learning: Atomic execution and ledger edit discipline

When updating CRDB ledgers (Evidence / Trigger / Change / Deliverable), treat the workflow itself as a governance control surface:

1) Explicit green-light boundaries
- Approval is required not only for the content decision (e.g., “make sitemap v4”), but for each ledger write.
- Enforce “one ledger at a time” to keep changes auditable.

2) Atomic execution
- Keep each shell command to ≤ 2 independent operations.
- Avoid large command blocks and chaining across multiple ledgers.

3) Markdown table updates (deterministic)
- Build a complete new table block in a tmp file and use replace-md-table.ts to replace the entire table block under an anchor.
- Prefer writing tmp files via patching rather than ad-hoc shell scripting.

4) Rule files are runtime constraints
- Treat .roo/rules/* and Thinking Companion mandates as non-negotiable. If execution pressure conflicts, stop and re-plan.

---
*Added via Oracle Learn*
