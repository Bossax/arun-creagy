# Visual design workflow

Use this workflow to turn supplied evidence, requirements, and visual references into a defensible visual-design package. Image generation and final layout happen in the user's chosen design application; prepare the materials needed for those steps here.

Keep the workflow proportional. Create only the artifacts that help the current project; combine them when the work is simple. Keep project-specific decisions in the project folder, never in this skill.

## Stage 0 — Intake and setup

Create a dated project folder named `YYYY-MM-DD_visual-project-name`. Record the brief, source inventory, constraints, and references. If there is a visual system to follow, create or select a project-level `DESIGN.md` from the available design references.

Clarify:

- audience and intended use
- format, dimensions, language, and production constraints
- central idea and required content
- source boundary and claim sensitivity
- visual references, brand rules, and prohibited elements

Suggested artifacts:

- `project_brief.md`
- `source_inventory.md`
- `DESIGN.md`
- `reference_images/`

## Stage 1 — Content and evidence plan

Review supplied sources before deciding what to show. Extract defensible claims, mechanisms, comparisons, spatial or temporal relationships, key quantities, uncertainty, and useful source figures. Identify claims that should not be visualized.

Turn the evidence into a concise content plan that states:

- primary message and audience takeaway
- message hierarchy and reading sequence
- selected claims, sources, and confidence
- draft display text or text limits
- required context, caveats, and prohibited inferences

### Reader-value gate — mandatory before Stage 2

Do not choose a visual concept, draft a headline, or write layout copy until the content plan contains an **Insight Card** with all six fields below:

1. **Reader question:** the question this single panel answers.
2. **Source-specific finding:** a relationship, contrast, exception, distribution, status condition, or quantified pattern that requires the supplied sources.
3. **Mechanism:** why the finding happens or why it matters.
4. **Consequence:** what it changes for a place, group, system, risk, or decision.
5. **Visual proof:** the one comparison, sequence, map, chain, or diagram that makes the finding visible.
6. **Evidence anchor:** source ID plus table, section, page, figure, or extract location.

Apply this rejection test: if the central finding could be written accurately without opening the supplied sources, it is too generic. Return to the evidence and find a more discriminating claim, or state that the source does not support an informative panel yet.

Use one primary thesis per panel. Supporting facts must explain, qualify, contrast, or prove that thesis; they cannot become a catalogue of sectors, hazards, agencies, definitions, or activities.

For every proposed content module, record:

`evidence → mechanism → reader consequence → visual role`

Remove a module if it only restates a familiar definition, repeats the title, decorates empty space, or lists facts without changing the reader's understanding.

Suggested artifacts:

- `content_plan.md`
- `evidence_map.md` or `evidence_to_visual_matrix.csv` when traceability matters

## Stage 2 — Visual plan

Choose a visual concept that best supports the approved Insight Card, message, and evidence. Define composition, hierarchy, visual elements, reference-image use, style, palette, and the space required for final text. Use a simple wireframe when hierarchy or layout needs validation.

The visual plan should make clear:

- dominant visual and reading direction
- what each visual element communicates
- which supplied figures or images are reproduced, adapted, or used only for style
- scientific, geographic, data, or accessibility risks
- what must remain editable or be added outside image generation
- the reader job of every major zone: establish the finding, explain the mechanism, show the contrast, locate the consequence, or test the response

Do not use a familiar visual grammar—a cycle, map, chain, matrix, timeline, or icon set—unless it makes the source-specific finding easier to understand. A generic process diagram without a source-specific tension is not an acceptable concept.

Suggested artifacts:

- `visual_plan.md`
- `wireframe.png` or `wireframe.md`
- `visual_element_register.md` when a design has many elements

## Stage 3 — Generation or layout handoff

Prepare one handoff that a designer, layout artist, or image-generation tool can use without reopening the research. Separate visual-generation instructions from final typesetting and data labels when accuracy matters.

Include:

- required attachments and their role
- composition and style instruction
- prompt and avoid list, if generating imagery
- dimensions, output requirements, and reserved text areas
- final display text, source notes, and editable-data requirements

When final display language is known, create the editable layout copy at this stage as a separate companion file for each language, for example `layout_text_th.md` for Thai. Create it alongside `generation_handoff.md`, not as a later iteration artifact. Keep it text-only and include every title, label, badge, caption, caveat, and source note needed by the layout.

Make the source-specific finding visible in the title, subhead, or first visual read; never hide it in a footer or source note. Write labels that answer a concrete question—where, for whom, compared with what, through which mechanism, or proven by which evidence. Preserve the source's status language such as complete, ongoing, uneven, local, projected, or not systematically measured.

Suggested artifact:

- `generation_handoff.md`
- `layout_text_<language>.md` when final display copy is required

## Stage 4 — Review and revision

Treat early outputs as composition prototypes. Review them against the evidence, hierarchy, format, and design system before polishing style. Write targeted revision requests that state what to preserve, change, and not change.

Resolve these first:

- factual and geographic accuracy
- causal or data interpretation
- hierarchy and reading order
- scale, legibility, and space for text
- required format and accessibility constraints

Run an anti-generic content review before accepting a revision:

- Could the same panel be produced from general background knowledge rather than these sources?
- Does the title announce only a topic, rather than state a finding or question with a consequential answer?
- Does each major zone have an evidence anchor and a reader job?
- Do the facts show a mechanism, contrast, affected group, or decision consequence—not merely that something exists?
- Is a list of sectors, projects, or institutions standing in for insight?
- Would removing the exact evidence anchors leave the panel's meaning essentially unchanged?

If any answer is yes, revise the content architecture before refining graphics, illustration, or typography.

Suggested artifacts:

- `review_v01.md`
- `revision_v01_to_v02.md`
- `content_manifest.csv` when final text is extensive or controlled

## Stage 5 — Final production package

Validate the final output at its intended size and medium. Deliver the agreed master, export formats, and concise source notes. Preserve editable assets when possible.

Suggested artifacts:

- final master and exports
- `source_notes.md`
- final `content_manifest.csv`, if used

## Principles

- Start with evidence and audience, not decoration.
- Earn the reader's attention with a source-specific insight, mechanism, and consequence; broad generic information is not a substitute for a thesis.
- Make the visual hierarchy match the message hierarchy.
- Do not let generated imagery introduce claims, text, data, or geography that cannot be verified.
- Use reference images deliberately: distinguish content reference, compositional reference, and style reference.
- Keep final typography, numbers, citations, and complex diagrams editable whenever possible.
- Use the smallest useful set of files. Add detail only when it reduces risk or improves handoff quality.
