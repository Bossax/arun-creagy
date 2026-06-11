# writing-th → Roo port plan

## 1) Objective
Port the Roo [`writing-th`](.roo/skills/writing-th/SKILL.md) skill into a copy-safe planning note that clarifies how the existing Thai-first workflow should be treated if it needs to be replicated, wrapped, or normalized for another Roo agent or another skill namespace.

## 2) Source of truth
- Roo skill: [`.roo/skills/writing-th/SKILL.md`](.roo/skills/writing-th/SKILL.md)
- Roo companion: [`.roo/skills/writing-th-learn/SKILL.md`](.roo/skills/writing-th-learn/SKILL.md)
- Writing style pack reference: [`plans/foresight-report-writing-style-pack.md`](plans/foresight-report-writing-style-pack.md)

## 3) Porting intent
This plan does not redesign the skill. It documents how to copy or mirror the existing skill cleanly when a Roo agent needs a duplicate or adapted version:

- Preserve the Thai-first report/article drafting flow.
- Preserve MCP-first retrieval and outline-stop behavior.
- Preserve the session style pack summary lifecycle.
- Preserve learn-back delegation to [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md).
- Avoid duplicating guardrails in an incompatible way; keep one authoritative source and one controlled copy target.

## 4) Roo-specific copy strategy
1. Decide whether the target is a literal copy, a renamed variant, or a project-specific fork.
2. Keep the existing [`writing-th`](.roo/skills/writing-th/SKILL.md) as the canonical source unless a new fork is explicitly approved.
3. If a fork is needed, create a separate skill folder with explicit scope boundaries and a distinct style pack path.
4. Reuse the existing skill contract for input handshake, outline-first stop, and draft/edited learn-back.
5. Keep any new files append-only and traceable through `plans/`.

## 5) Proposed Roo deliverables
- A copy/fork decision note
- A target skill folder, if duplication is approved
- A compatibility note showing what changes are allowed versus forbidden
- Optional internal mapping for plan files, style pack files, and session summaries

## 6) Migration steps
1. Confirm whether the task is a copy, fork, or simple reference normalization.
2. Identify the target agent or skill namespace.
3. Verify whether the target should inherit the existing style pack contract unchanged.
4. If needed, create a new skill directory and minimal wrapper docs.
5. Validate that the copied version still points to the correct learn-back companion and style pack references.

## 7) Open design questions
- Is the goal to duplicate [`writing-th`](.roo/skills/writing-th/SKILL.md) verbatim, or to create a renamed variant for another Roo agent?
- Should the copied skill share the same companion [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md), or use a separate learn-back path?
- Should style pack artifacts remain centralized under `plans/` or be duplicated per target project?

## 8) Approval boundary
No implementation should start until the copy model is chosen: literal copy, fork, or wrapper. This plan is only the decision scaffold for that choice.

## 9) Step 1 decision: exact Roo destination
- Roo destination for the writing-th skill remains [`.roo/skills/writing-th/SKILL.md`](.roo/skills/writing-th/SKILL.md).
- Roo destination for the learn-back companion remains [`.roo/skills/writing-th-learn/SKILL.md`](.roo/skills/writing-th-learn/SKILL.md).
- Decision for this step: keep the existing skill pair as the canonical Roo installation and do **not** introduce a duplicate fork folder yet; this is the smallest safe change and has no hidden dependency on style-capture or seal.
