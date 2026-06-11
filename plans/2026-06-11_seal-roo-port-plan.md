# seal → Roo port plan

## 1) Objective
Port the Gemini-side [`seal`](.gemini/skills/seal/SKILL.md) skill into a Roo-compatible skill package that preserves its audit-to-asset causality chain, ledger model, and approval-gated sealing workflow.

## 2) Source of truth
- Gemini skill: [`.gemini/skills/seal/SKILL.md`](.gemini/skills/seal/SKILL.md)
- Gemini ledger template: [`.gemini/skills/seal/TEMPLATE.md`](.gemini/skills/seal/TEMPLATE.md)
- Roo writing baseline: [` .roo/skills/writing-th/SKILL.md`](.roo/skills/writing-th/SKILL.md)

## 3) Porting intent
The Roo version should preserve the original behavior:

- Discover recent progress from local history.
- Reconstruct the progression chain from evidence to trigger to change to deliverable.
- Present a proposal and pause for approval.
- On approval, materialize the ledgers and mark the deliverable as sealed.

## 4) Roo-specific adjustments
1. Replace Gemini-only helpers such as `arra_search`, `arra_trace`, and `arra_trace_link` with Roo-local equivalents or a documented fallback.
2. Keep the PowerShell-first root detection logic, but align it with Roo workspace conventions.
3. Convert the ledger workflow into a clear file-based procedure that can run in the current repository structure.
4. Preserve the approval gate before any sealing action.
5. Keep the ledger names and roles, but ensure the output paths match the repository's `ψ/incubate/` organization.

## 5) Proposed Roo deliverables
- `SKILL.md` for the Roo seal skill
- A Roo-compatible ledger template derived from [`TEMPLATE.md`](.gemini/skills/seal/TEMPLATE.md)
- Optional plan note mapping how evidence, triggers, changes, and deliverables are discovered in Roo

## 6) Migration steps
1. Audit Roo skill conventions and decide the destination folder for the port.
2. Define the Roo equivalents for discovery, traceability, and ledger writes.
3. Rewrite the workflow so the proposal step is explicit and human-approved.
4. Generate the ledger template in Roo format.
5. Validate that the sealed output remains append-only and history-preserving.

## 7) Open design questions
- Should the Roo port use the existing [`recap`](.roo/skills/recap/SKILL.md) or a dedicated trace skill for discovery?
- Should the seal workflow be project-specific or generalized for all repository work?
- What exact local search/trace helpers should replace the Gemini-only calls?

## 8) Approval boundary
This plan is complete when the Roo discovery backend, ledger destination, and sealing trigger are finalized. Implementation should wait until those decisions are approved.
