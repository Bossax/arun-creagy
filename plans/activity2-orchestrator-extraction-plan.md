# Activity 2 — Orchestrator Plan: Per-interview extraction into central `user_use_case_raw`

## Objective

Run a repeatable workflow where **each subtask extracts unaltered use cases** from exactly one interview summary note and **appends/edits a single central markdown file** named `user_use_case_raw` (grouped by the 5 workshop groups).

This plan is designed for [`functions.new_task()`](functions.new_task:1) with `mode=orchestrator`, and then spawning one extraction subtask per agency.

## Central file (single source of truth)

- **File**: [`ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md`](ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md)
- **Sectioning**: The top-level structure is **the 5 groups** (not agencies), per [`ψ/incubate/DCCE/CRDB/inbox_note/2026-05-08-pivot-activity-2-of-the-CRDB-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-05-08-pivot-activity-2-of-the-CRDB-workshop.md:81)

### Group headers (must match exactly)

1. กลุ่มที่ 1 ข้อมูลทางเศรษฐศาตร์และการเงิน
2. กลุ่มที่ 2 ข้อมูลสนับสนุนการวางแผนและนโยบายเชิงพื้นที่
3. กลุ่มที่ 3 ข้อมูลสนับสนุนการปฏิบัติงานเชิงพื้นที่
4. กลุ่มที่ 4 ข้อมูลสนับสนุนกลุ่มเปราะบางและความสามารถในการรับมือปรับตัว
5. กลุ่มที่ 5 ข้อมูลสนับสนุนการตีความข้อมูลและพัฒนาระบบข้อมูล

## Extraction schema (what each subtask must produce)

Each extracted use case becomes one bullet in the relevant group section.

Template:

```md
- Agency: <short agency name>
  - Use case: <unaltered phrasing from interview note, minimal rewriting>
  - Goal: <goal OR pain point>
  - Required data/products: <list>
  - Source anchors: <link(s) to the interview summary file with line numbers if possible>
```

Rules:

- **Unaltered**: prefer verbatim phrases from “Highlighted Key Projects” and “Current Workflow & Data Usage” (per [`ψ/incubate/DCCE/CRDB/inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md:8)).
- **Minimal compression**: do not collapse multiple distinct use cases into one.
- **Single-group assignment**: even if it could belong to multiple groups, pick the most prominent one (per [`ψ/incubate/DCCE/CRDB/inbox_note/2026-05-08-pivot-activity-2-of-the-CRDB-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-05-08-pivot-activity-2-of-the-CRDB-workshop.md:89)).

## Orchestrator workflow (runbook)

### Step 0 — Preflight

1. Ensure the central file exists.
   - If missing, create it with the 5 group headers and an empty placeholder under each.
2. Pick the list of interview notes to process from [`ψ/incubate/DCCE/CRDB/output/Interview summary notes/`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:1).

### Step 1 — Spawn extraction subtasks (one per interview note)

For each agency note, create a subtask with:

- **Input**: exactly one interview summary note.
- **Output target**: update [`ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md`](ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md) directly.
- **Output constraint**: only add bullets under the correct group section(s) using the schema above.

Subtask instruction stub (to paste into [`functions.new_task()`](functions.new_task:1)):

```text
Extract unaltered use cases from <INTERVIEW_NOTE_FILE>.

For each use case:
- capture Use case (verbatim-ish), Goal, Required data/products
- assign exactly one of the 5 groups
- include Source anchors pointing back to <INTERVIEW_NOTE_FILE>.

Write by appending/editing the central file: ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md
Do not create any other files.
```

### Step 2 — Collision control (important if subtasks run in parallel)

Because every subtask edits the same file, apply one of these controls:

- **Serial write policy (preferred)**: only run one extraction subtask at a time; next starts after previous completion.
- **Reservation policy**: orchestrator assigns each subtask a temporary marker block under its target group and only that subtask may edit within the marker.

### Step 3 — Review gate

After 1–2 agencies, pause and review:

- Are bullets concrete (action + info + goal), aligned with workshop definition of “use case” in [`ψ/incubate/DCCE/CRDB/inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md:8)?
- Is grouping intuitive and consistent?
- Is wording still “unaltered” enough?

If not, refine the schema before scaling.

## Definition of done (Phase 1)

- [`ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md`](ψ/incubate/DCCE/CRDB/output/user_use_case_raw.md) contains bullets from all interview summary notes, grouped into the 5 sections, each with goal + required data/products + traceable source anchors.

