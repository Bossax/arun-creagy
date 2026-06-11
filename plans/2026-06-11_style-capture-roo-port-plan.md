# style-capture → Roo port plan

## 1) Objective
Port the Gemini-side [`style-capture`](.gemini/skills/style-capture/SKILL.md) skill into a Roo-compatible skill package without changing its core behavior: sample-based style extraction, draft-vs-edited refinement, cumulative style-pack maintenance, and master prompt synthesis.

## 2) Source of truth
- Gemini skill: [`.gemini/skills/style-capture/SKILL.md`](.gemini/skills/style-capture/SKILL.md)
- Roo writing baseline: [` .roo/skills/writing-th/SKILL.md`](.roo/skills/writing-th/SKILL.md)
- Roo learn-back companion: [` .roo/skills/writing-th-learn/SKILL.md`](.roo/skills/writing-th-learn/SKILL.md)

## 3) Porting intent
This port should preserve the original skill's learning loop while adapting it to Roo conventions:

- Keep the cumulative **Style-Pack** concept.
- Keep **Sample** and **Refinement** input modes.
- Keep the **structural DNA / linguistic marker / anti-AI shield** extraction logic.
- Replace any Gemini-specific runtime dependencies with Roo-local patterns and file-based artifacts.
- Align outputs with the existing Thai writing workflow where relevant, but keep the skill usable for broader style capture contexts.

## 4) Roo-specific adjustments
1. Replace the Gemini skill execution model with a Roo skill structure that uses local files and explicit plan artifacts.
2. Reframe persistence to a project-local style-pack ledger under `ψ/` or a project plan file, rather than any Gemini-managed state.
3. Keep the master prompt output, but make it deterministic and session-scoped.
4. Ensure the skill does not assume `oracle_learn` or other unavailable Gemini runtime helpers unless a Roo equivalent exists.
5. Reuse the existing `writing-th` guardrails for citation discipline, outline-stop behavior, and no-invented-sources discipline when the skill is used in Thai-report contexts.

## 5) Proposed Roo deliverables
- `SKILL.md` for the Roo skill definition
- A style-pack template or session ledger note if needed
- Optional companion notes under `plans/` describing the extraction workflow and folder conventions

## 6) Migration steps
1. Audit the current Roo skill folder conventions and determine the best home for a new style-capture skill.
2. Draft the Roo `SKILL.md` with the same core phases as the Gemini version.
3. Replace Gemini-only terminology with Roo-native wording and file paths.
4. Define where style-pack artifacts live and how they are updated.
5. Validate the new skill against the existing [`writing-th`](.roo/skills/writing-th/SKILL.md) and [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md) workflow.

## 7) Open design questions
- Should style-capture be a general-purpose writing skill, or should it be narrowed to Thai-first report/article workflows?
- Should cumulative style-pack storage live in `plans/`, `ψ/memory/`, or a project-specific output folder?
- Should the Roo port reuse the learn-back handoff from [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md) or stay independent?

## 8) Approval boundary
This plan is complete when the Roo skill shape, storage location, and update workflow are agreed. Implementation should not start until the final target folder and artifact naming are approved.
