---
name: visual-design
description: Create evidence-led visual-design packages for infographics, rollups, posters, and presentation graphics. Use for research-backed visual communication that needs a reference style, a controlled layout, a full first-draft image, review, and later Canva asset extraction.
---

# Visual design workflow

Turn evidence and requirements into a visual design that can be reviewed, generated, and assembled in Canva. Use the fewest artifacts that make a decision or handoff reliable.

Never create an artifact merely because it may be useful. Every artifact below has one authority, one job, and one consumer.

## Non-negotiable rules

- Keep project decisions in the project folder, never in this skill.
- Start with evidence and the reader's question, not decoration.
- Treat a visual reference as three separate inputs: **illustration style**, **composition**, and **information hierarchy**. Record which inputs are approved; never assume all three.
- Keep final text, data, citations, and complex diagrams editable in Canva.
- Do not let image generation invent claims, labels, numbers, citations, geography, or logos.
- Do not send a workflow history to ChatGPT. Send one current-stage production packet.
- Do not start Stage 5 before the Stage 3 full-rollup draft passes Stage 4 review.

## Project structure

Create one dated project folder:

```text
YYYY-MM-DD_visual-project-name/
└── 00_project/
    ├── project_brief.md
    ├── DESIGN.md
    ├── content_plan.md
    ├── visual_plan.md
    ├── layout_prototype.html       # when layout/copy fit is at risk
    ├── layout_prototype.png        # rendered HTML preview for ChatGPT
    ├── render_layout_prototype.js  # copied renderer utility
    ├── generation_handoff.md
    ├── layout_text_<language>.md
    ├── review_vNN.md               # only after a draft exists
    └── asset_generation_prompts.md # Stage 5 only
```

For a multi-panel project, retain shared artifacts in `00_project/` and add `rollup_01/`, `rollup_02/`, and so on. Each rollup owns its own content plan, visual plan, prototype, handoff, display copy, review, and asset prompts.

## Artifact contract

| Artifact                      | Authority                 | Must contain                                                              | Must not contain                                | Consumer          |
| ----------------------------- | ------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| `project_brief.md`            | scope                     | audience, output, questions, constraints, reference roles                 | research synthesis, prompts, layout             | Stages 1–2        |
| `DESIGN.md`                   | visual language           | reference extraction, palette, typography, illustration rules, exclusions | claims, workflow stages, prompt prose           | Stages 2–5        |
| `content_plan.md`             | message and evidence      | Insight Card, claim IDs, evidence anchors, reader jobs, prohibited claims | layout or image prompt decisions                | Stage 2           |
| `visual_plan.md`              | composition               | reading path, zones, visual roles, editable text zones, risks             | research notes, production prompt               | Stage 3           |
| `layout_prototype.html`       | editable layout           | dimensions, copy capacity, reading order, safe zones                      | final illustration                              | Stage 3 review    |
| `layout_prototype.png`        | visual layout attachment  | browser-rendered preview of the approved HTML                             | generated artwork or design decisions           | ChatGPT Stage 3–4 |
| `layout_text_<language>.md`   | display copy              | final editable titles, labels, captions, source note                      | style or generation instructions                | Canva and Stage 3 |
| `generation_handoff.md`       | current production packet | one tool-facing prompt, attachment list, output boundary, exclusions      | Stage 1–5 workflow or future-stage instructions | ChatGPT Stage 3   |
| `review_vNN.md`               | revision decision         | preserve/change/do-not-change and observable corrections                  | vague taste-only feedback                       | Stage 4           |
| `asset_generation_prompts.md` | ChatGPT asset delegation  | one prompt asking ChatGPT to plan and sequence asset generation            | agent-selected asset list or image prompts      | ChatGPT Stage 5   |

### Authority order

Resolve conflicts in this order:

1. User instruction and approved project brief
2. Content plan for meaning and evidence
3. Visual plan and rendered prototype for composition
4. DESIGN.md for visual language
5. Layout text for displayed wording
6. Generation handoff, which must only restate the approved decisions above

The generation handoff must never introduce a new visual, factual, or workflow decision.

## Stage 0 — Scope and design system

Create only `project_brief.md` and `DESIGN.md`.

1. Clarify audience, output dimensions, language, required questions, source boundary, and constraints.
2. Classify every reference image as style, composition, information hierarchy, or a combination explicitly approved by the user.
3. If a design system is needed, copy or adapt `ψ/lab/visual_design/design-md-template.md` into the project as `DESIGN.md`.
4. Extract only reusable visual rules: palette, typography character, shapes, line weight, depth, texture, icon language, composition tendencies, and exclusions.

**Gate:** Do not research or concept until the reader, physical output, reference role, and style exclusions are clear.

## Stage 1 — Evidence and message

Create only `content_plan.md`. Keep an evidence table inside it; create a separate evidence file only when the evidence cannot remain readable there.

The content plan must contain one **Insight Card**:

1. Reader question
2. Source-specific finding
3. Mechanism
4. Consequence
5. Visual proof
6. Evidence anchors

For each module, record:

`claim ID → evidence anchor → mechanism → reader job → visual role`

Reject a concept if the central finding could be written without opening the sources. State claims that must not be visualized or must be qualified.

**Gate:** Do not choose a visual concept, headline, or production prompt until the Insight Card and all major claim anchors are approved.

## Stage 2 — Composition and layout

Create `visual_plan.md`. Create `layout_prototype.html` when the design is dense, bilingual, physically large, narrow, or otherwise at risk of copy-fit failure. Render the approved HTML as `layout_prototype.png` before any ChatGPT generation.

Use the bundled renderer `scripts/render_layout_prototype.js`. Copy it into `00_project/` and run:

```text
node render_layout_prototype.js
```

The prototype HTML must expose its export element as `.rollup`. If Playwright reports a missing browser, install Chromium with `npx playwright install chromium`, then rerun the renderer. Verify that the PNG exists and preserves the intended aspect ratio before treating it as an attachment.

The visual plan must define:

- final dimensions and reading direction;
- one dominant visual anchor;
- zone order and the reader job of each zone;
- visible evidence-bearing forms: comparison, route, map, chain, slots, or diagram;
- exact editable text zones and safe areas;
- palette roles and reference-style rules;
- accessibility, scientific, geographic, and layout risks.

The HTML prototype is the editable source of truth. It must show the intended aspect ratio, real or representative copy, reading order, evidence-bearing scaffold, and reserved text areas. Its browser-rendered PNG is the layout attachment for ChatGPT; it must be an exact render, never a generated reinterpretation.

**Gate:** Do not generate a full draft until the prototype makes the central finding understandable and proves that copy fits the physical format.

## Stage 3 — Full first-draft generation

Create `layout_text_<language>.md` and `generation_handoff.md`.

Stage 3 produces one complete first-draft image of the whole rollup. It is a composition-and-style review draft, not a final Canva asset set.

### ChatGPT production packet

Attach only:

1. `layout_prototype.png` as the **sole visual composition authority**;
2. the copy-paste prompt from `generation_handoff.md`.

Do not attach a style-reference image, project brief, content plan, visual plan, design system, HTML source, or workflow stages. State the approved style rules as text in the handoff. A reference image can dominate a generation even when it is labelled style-only.

### Generation handoff requirements

`generation_handoff.md` must contain exactly:

- output format and physical dimensions;
- rendered-prototype attachment role;
- the current output boundary: **generate one full first draft**;
- a concise composition instruction derived from the prototype;
- one style-lock paragraph derived from `DESIGN.md`;
- visible draft-copy instruction derived from `layout_text_<language>.md`;
- palette and exclusions;
- a direct statement of what not to generate.

It must not mention Stage 1, Stage 2, Stage 4, Stage 5, asset extraction, or future workflows.

### Stage 3 prompt skeleton

```text
Create one complete first-draft [format] at [physical dimensions].

Attachments:
- [rendered prototype PNG]: strict layout, hierarchy, and zone authority.

Reproduce the prototype's reading path, zone proportions, visual anchor, and editable text space. Use this text-only style lock: [one paragraph from DESIGN.md].

Use this visible draft copy: [short title and essential labels from layout_text]. Keep longer copy minimal and leave it editable for Canva.

Use only: [palette].
Do not use: [exclusions].
Output one complete review draft, not isolated assets and not a dashboard of unrelated panels.
```

**Gate:** Review the generated full rollup against the prototype, source-specific finding, style reference, and physical dimensions before extracting assets.

## Stage 4 — Review and revision

Create `review_vNN.md` only when a draft needs revision. This file is the self-contained revision instruction note that ChatGPT uses after the user approves it.

Review in this order:

1. evidence and causal accuracy;
2. visible mechanism and required modules;
3. reading order, scale, copy fit, and physical format;
4. reference-style fidelity;
5. palette, typography, and polish.

Write only observable instructions:

```markdown
# Review — V01

## Preserve
- [specific working zone, shape, or relationship]

## Change
- [observable zone, shape, icon, route, count, palette, or hierarchy correction]

## Do not change
- [locked decision]
```

State the baseline draft filename and end the note with one direct instruction to revise that draft. Do not edit `generation_handoff.md` during Stage 4. After approval, attach only the baseline draft, `layout_prototype.png`, and `review_vNN.md`; use the note itself as the ChatGPT revision prompt.

Reject a draft when it uses generic visual grammar, depends on future copy to explain the mechanism, breaks the prototype's hierarchy, or drifts from the reference style.

**Gate:** Approve the full composition before Canva asset extraction.

## Stage 5 — Canva asset extraction

Create `asset_generation_prompts.md` only after Stage 4 approves the full draft.

Stage 5 does not identify assets, choose their order, or write image prompts. It creates one copy-paste **delegation prompt** that tells ChatGPT to inspect the approved full rollup and do those tasks itself.

Attach the approved full-rollup draft and the Stage 5 prompt to ChatGPT. The prompt must instruct ChatGPT to:

1. identify the minimum reusable illustration assets needed for Canva;
2. return an asset manifest with each asset's role, placement, aspect ratio, background requirement, and the approved visual rules it must retain;
3. write the image-generation prompt for the first asset only;
4. wait for the user to request the next asset, then generate one asset at a time;
5. keep generated assets text-free and prevent new claims, data, labels, citations, or redesign decisions.

`asset_generation_prompts.md` must not contain an asset list invented by this workflow. ChatGPT owns the asset analysis and prompt sequence. Canva receives the generated assets plus `layout_text_<language>.md` for final typography, data, citations, and assembly.

## Final checklist

- Every artifact has an explicit authority and consumer.
- ChatGPT receives only the current-stage packet.
- The full draft is generated in Stage 3.
- ChatGPT receives the browser-rendered prototype PNG, not the HTML source or a style-reference image.
- Stage 4 produces the approved revision instruction note used directly by ChatGPT.
- Full-draft approval happens before asset extraction.
- Canva receives editable copy and approved assets, not a redesigned composition.
