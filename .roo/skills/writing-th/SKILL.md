---
name: writing-th
description: Thai-first writing skill (report/article). MCP-first retrieval, style-pack lifecycle, outline-stop, and learn-back via writing-th-learn.
---

# /writing-th [--report | --article]

> Thai-first drafting skill for formal reports and readable articles. This skill is designed to be **Oracle-aligned** and traceable:
> - **MCP-first** retrieval (no Oracle HTTP APIs)
> - **Outline-first stop** (human control boundary)
> - **Session-specific style pack summary** lifecycle
> - **Learn-back** delegated to [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md)
> - **Stage-aware control** — drafting and editing are iterative; do not apply all rules equally at every pass

## When to use

- When the user wants a Thai draft that must match a specific report/article voice.
- When the user provides an **example report** to mimic (terminology + section flow).

## When NOT to use

- If there is no writing goal yet (topic/objective/audience unknown).
- If the task is purely editing an existing Thai document without drafting.

---

## Modes

Exactly one mode flag:

- `--report` — รายงานทางการสำหรับหน่วยงานรัฐ/องค์กร (default if not specified)
- `--article` — บทความอ่านง่าย โครงสร้างชัด จังหวะเล่าเรื่อง

---

## Inputs (minimal handshake)

Ask only for what is missing:

1. **Writing plan path** (markdown) — anchor file where we append outline + session style pack summary.
2. **Example report path** (markdown; optional but recommended) — the style reference for this session.
3. **หัวข้อ + วัตถุประสงค์** — what are we writing and what decision/action should the reader take.
4. **ผู้อ่าน** — target audience.
5. **ความยาวเป้าหมาย** — pages/words.
6. **Constraints** — must-include / must-avoid / deadline.
7. **Ground-truth sources** — only these files/notes are allowed as factual basis.

---

## Writing plan template (recommended)

Use this structure in the writing plan file so `/writing-th` and `/writing-th-learn` can stay traceable and automation-friendly.

```markdown
# Writing Plan — <topic>

## 0) Session metadata
- Date:
- Mode: report|article
- Audience:
- Target length:
- Deadline:

## 1) Ground-truth sources (allowed facts)
- <path>

## 2) Example report (style reference)
- Path: <path>
- Permission to use as style reference: yes|no
- Mimic scope: terminology + section flow (no verbatim copying)

## 3) Output targets
- Draft output folder:
- Filename base:

## 4) Session Style Pack Summary
<!-- append-only: one block per session -->

## 5) Outline approvals
<!-- append-only: outline versions + approvals -->

## 6) Draft/Edited mapping (if names do not conform)
- Draft: <path>
- Edited: <path>
```

Notes:

- Keep this plan **append-only** (Nothing is Deleted).
- The “Permission” line is the explicit guardrail for example-report usage.

---

## Style precedence (important)

This skill uses **layered style**, with two phases:

### Phase A — Before any project session style pack exists

1. **Example report (session reference)** — primary for terminology + section flow, within bounds of the layers below.
2. **Project style brief (if present)** — binding voice/tone/concept framing for this deliverable.
3. **Persistent resonance (safety rails)** — baseline constraints that must not be violated:
   - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)
   - [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md)
4. **Learnings tagged writing-th** — evolving patterns from previous projects/sessions.

### Phase B — After a project session style pack exists

1. **Example report (session reference)** — primary for terminology + section flow, **within the bounds of the layers below**.
2. **Project Session Style Pack file** — project-specific rules that crystallized from human-edited drafts and `/writing-th-learn` patterns (e.g., `plans/<project>-writing-style-pack.md`).
3. **Project style brief (if present)** — binding voice/tone/concept framing for the deliverable.
4. **Persistent resonance (safety rails)** — global constraints for writing and citations.
5. **Learnings tagged writing-th** — additional global patterns.

If example style conflicts with a project Session Style Pack, project style brief, or resonance, **the pack + brief + resonance win**.

---

## Guardrails (Oracle alignment)

### Permission + copying

- Confirm the example report is **permitted to be used as a style reference**.
- “Mimic” means: **terminology + section flow + rhetorical moves**, NOT verbatim sentence copying.
- If quoting is required, mark it clearly and cite properly.

### Grounding + citations

- **No invented sources**.
- Citations only from user-provided sources or explicitly retrieved via MCP from `ψ/`.

### External vs internal artifacts

- Keep **DCCE/sponsor-facing prose** free from repo-internal links and internal scaffolding.
- If traceability/QA is needed, create a separate internal artifact (map/log) rather than embedding it in main prose.

---

## Workflow

### Step 0 — Identify loop stage before doing anything else

This skill must **not** treat all writing work as one drafting event. Before drafting, revising, or editing, determine the current stage of the writing loop and activate only the relevant rule layer.

Use these stages:

1. **Stage A — Framing / Outline**
   - Goal: define section job, audience action, evidence boundaries, and section sequence.
   - Primary rules: section architecture, outline logic, evidence scope.
   - Defer: sentence polish, lexicon cleanup, micro-diction.

2. **Stage B — First Draft / Content Build**
   - Goal: get the content spine onto the page while preserving source meaning.
   - Primary rules: section job, paragraph payload, actor/product clarity, preservation-first fidelity.
   - Defer: heavy sentence beautification, aggressive compression, lexicon perfection.

3. **Stage C — Structural Revision**
   - Goal: repair drift, split overloaded paragraphs, re-sequence evidence, and clarify section logic.
   - Primary rules: one paragraph one job, evidence-to-action chain, service-package sequence, adoption-test clarity.
   - Defer: low-level word substitution unless it blocks structural clarity.

4. **Stage D — Voice / Sentence Revision**
   - Goal: make the prose sound like authored Thai institutional writing.
   - Primary rules: subject-first sentence shape, active institutional agency when actor is known, anti-translation cleanup, anti-AI phrasing.
   - Defer: broad restructuring unless sentence problems reveal deeper structural defects.

5. **Stage E — Lexicon / Consistency Pass**
   - Goal: normalize terminology and remove banned phrases.
   - Primary rules: project lexicon, approved shorthand, technical anchor discipline, repeated term consistency.
   - Defer: major content changes unless a lexical issue reveals a factual or institutional mismatch.

6. **Stage F — Release Gate**
   - Goal: confirm the section is audience-facing and publishable.
   - Primary rules: no invented sources, no repo-internal leakage, no unresolved placeholders unless explicitly marked, style drift check.

Rule of thumb:

- A smooth sentence that arrives before a complete argument is a drafting failure.
- A lexically compliant paragraph that still lacks a clear job is not draft-ready.
- Early stages optimize **content logic**; late stages optimize **surface control**.

### Step 0 — Decide mode

- If the user does not specify a mode, default to `--report`.

### Step 0b — Ask or infer the stage if needed

If the user says things like:

- “outline”, “plan”, “scaffold” → Stage A
- “draft”, “write section”, “first pass” → Stage B
- “restructure”, “fix flow”, “too hollow”, “section job unclear” → Stage C
- “unnatural Thai”, “sounds AI”, “active voice”, “polish prose” → Stage D
- “check lexicon”, “normalize terms”, “replace wording” → Stage E
- “finalize”, “ready to send”, “release” → Stage F

If the stage is ambiguous, infer the narrowest plausible stage from the user’s request and current artifact state.

### Step 1 — Retrieve memory (MCP-first)

Hard rule: **no Oracle HTTP APIs**.

Use MCP tools to retrieve:

- Resonance:
  - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)
  - [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md)
- Learnings:
  - `ψ/memory/learnings/*writing-th*` and/or relevant tags for the selected mode.

Then read the user-provided example report file (path from the writing plan) to extract:

- preferred terminology (key nouns/verbs)
- section flow (ordering + headings style)
- paragraph rhythm (length, transitions)
- typical summary blocks vs narrative

### Step 2 — Session Style Pack handling

There are two cases:

1. **No project Session Style Pack yet (first drafting phase)**

- Do **not** create a Session Style Pack file yet.
- Use only:
  - resonance (writing-style-th + citation-style-th),
  - existing learnings tagged `writing-th`,
  - example report(s),
  - project style brief (if any).
- Proceed to Step 3 (Outline) and Step 4 (Draft) using these layers.

2. **Project Session Style Pack exists**

- Load the Session Style Pack file referenced in the writing plan (for example `plans/<project>-writing-style-pack.md`).
- Append a new `Session Style Pack Summary` block into that file (append-only):

  ```markdown
  ## Session Style Pack Summary (YYYY-MM-DD HH:MM)

  ### Primary reference
  - Example report: <path>
  - Project style brief (if any): <path>

  ### Terminology (preferred)
  - ...

  ### Section flow
  - ...

  ### Voice + constraints (safety rails)
  - (from resonance + project brief)

  ### Citations
  - ...

  ### Placeholders
  - [ต้องเติมตัวเลข] / [ต้องเติมแหล่งอ้างอิง] ...
  ```

Notes:

- The summary is **session-scoped** and must not overwrite past summaries.
- This block is a traceable snapshot, not a replacement for the underlying style files.

### Step 3 — Outline first, then STOP (Stage A only)

Produce at least one numbered Thai outline, and optionally two variants if the structure is still ambiguous:

- Variant A: closest to the example flow
- Variant B: closest to the plan/TOR flow (if different)

Append the chosen outline into the writing plan and **STOP** for explicit confirmation.

### Step 4 — Draft (Stage B)

After confirmation:

- Write the draft as a new file (no overwrite).
- Recommended naming:
  - `<topic-slug>-v1-draft.md`
  - If re-drafting: increment version (`v2`, `v3`, ...)

### Step 4b — Stage-aware sanity check before accepting a section

After completing a substantial section, run a sanity check against the active writing style pack (resonance + project style brief if any + Session Style Pack Summary), but apply only the checks relevant to the current stage:

- **Stage B check**
  - section performs one clear job
  - paragraphs carry enough evidence payload
  - no invented sources
  - source meaning preserved

- **Stage C check**
  - each paragraph does one main job
  - section sequence is coherent
  - package / mechanism / adoption-test logic is visible

- **Stage D check**
  - Thai-first wording intact
  - active institutional agency where actor is known
  - no translated English scaffolding
  - anti-AI cleanup without payload loss

- **Stage E check**
  - terminology follows project lexicon
  - department shorthand and technical anchors are consistent
  - banned phrases removed

- **Stage F check**
  - audience-facing prose contains no internal scaffolding
  - placeholders, unresolved claims, and citations are handled appropriately
  - style does not drift away from the approved reference

If any check fails, revise that section under the same style pack before treating it as draft-ready.

### Step 5 — Human edit handshake

Ask the user to:

- Copy the draft and create an edited version.
- Prefer the naming pair for automation:
  - `...-draft.md`
  - `...-edited.md`

If the user wants different filenames, preserve the originals and create a conforming copy pair (Nothing is Deleted).

### Step 6 — Learn-back (delegated)

If an edited version exists, invoke the learning-only companion:

- [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md)

Goal of learn-back:

- extract patterns in word choice + semantic arrangement
- store as `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md`

### Step 6b — Feed stage-specific corrections to [`style-capture`](.roo/skills/style-capture/SKILL.md)

When a human correction reveals a repeated pattern, treat it as a stage-tagged learning event:

- Section architecture lesson → Stage A memory
- Paragraph payload lesson → Stage B/C memory
- Sentence agency or anti-AI lesson → Stage D memory
- Lexicon substitution lesson → Stage E memory

Do **not** flatten all corrections into one undifferentiated style rule list.

---

## /rrr integration (document-only, for now)

This redesign does **not** implement automatic detection in `/rrr` yet.

Intended future behavior:

- When `/rrr` runs, it may detect draft/edited pairs created in the session and invoke [`/writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md).

Reason to keep this separate:

- Avoid coupling retrospective generation to writing-learning extraction until the naming/mapping rules are stable.

