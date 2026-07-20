# Visual design workflow

Important: image generation will be done in web application, not here. Your job is to run this workflow through step 5. Then, the workflow will be back and forth. 

## Stage 0 — Project intake
create a new folder for. name it with [YYY-MM-DD_visual-project-name].
The artifacts will be saved in this folder.

create DESIGN.md from reference design using [[ψ/lab/visual_design/design-md-template|design-md-template]]

You provide:
- scientific articles, reports, datasets, figures, or reference images
- the main idea you want the audience to understand
- intended audience
- output format
- preferred style or references
- constraints such as language, geographic accuracy, required statistics, and prohibited elements

Artifact: `project_brief.md`
```markdown

# Project Brief

## Working title
Impact of ENSO on rainfall patterns in Thailand

## Core idea
El Niño and La Niña alter atmospheric circulation over the Pacific, producing different rainfall effects across regions of Thailand.

## Intended audience
Policy officers and non-specialist technical stakeholders

## Intended use
Scientific infographic for a presentation

## Format
16:9 landscape

## Required content
- Thailand
- Pacific Ocean
- atmospheric circulation
- rainfall anomaly
- dry and wet regions
- clear contrast between El Niño and La Niña

## Constraints
- No unsupported numerical claims
- Thailand’s geographic outline must remain recognizable
- Avoid overly technical equations
- Use Thai labels in the final layout

## Visual references
- editorial scientific infographic
- flat or semi-3D vector illustration
- central visual metaphor
- limited color palette
```

## Stage 1 — Source review and evidence extraction

The first task is not image generation. It is to inspect the supplied scientific sources and identify what is visually defensible.

The workflow should search the sources for:

- primary scientific claims
- causal mechanisms
- spatial relationships
- temporal changes
- comparisons
- quantities
- uncertainty
- representative examples
- figures that reveal useful visual structures
- statements that should not be visualized because evidence is weak

Artifact: `evidence_map.md`
```markdown
# Evidence Map

## Claim E01
ENSO changes atmospheric circulation across the tropical Pacific.

Source:
S01, Section 3.2, Figure 4

Evidence strength:
Strong

Potential visual:
Pacific cross-section with circulation arrows

Visual caution:
Do not imply that circulation is identical in every ENSO event.

---

## Claim E02
El Niño is generally associated with reduced rainfall over parts of Thailand.

Source:
S01, Table 2
S02, Chapter 4

Evidence strength:
Moderate to strong

Potential visual:
Dry land, reduced cloud cover, warm-color rainfall anomaly

Visual caution:
Regional and seasonal variation must be acknowledged.

---

## Claim E03
La Niña is generally associated with wetter conditions.

Source:
S02, Figure 8

Evidence strength:
Strong

Potential visual:
Rain clouds, higher rainfall, flood-prone areas

Visual caution:
Avoid depicting all of Thailand as uniformly wet.
```

Artifact: `evidence_to_visual_matrix.csv`

|Evidence ID|Claim|Visual form|Priority|Confidence|Source|Must show|Must avoid|
|---|---|---|---|---|---|---|---|
|E01|ENSO alters circulation|arrows and ocean-atmosphere cross-section|High|High|S01|east-west relationship|oversimplified causality|
|E02|rainfall declines in some regions|dry-zone overlay|High|Medium|S01, S02|regional variation|whole-country drought|
|E03|wetter conditions under La Niña|rain overlay|High|High|S02|heavier rainfall|exact values without data|

## Stage 2 — Narrative development

Scientific sources rarely arrive in the order needed for an infographic. The workflow must transform evidence into a visual story.

The narrative should answer:
- What is happening?
- Why is it happening?
- Where does it happen?
- What changes?
- Why does it matter?
- What should the audience remember?

Artifact: `narrative_options.md`
```markdown
# Narrative Options

## Option A — Mechanism-first

1. ENSO begins in the tropical Pacific
2. Ocean temperatures alter atmospheric circulation
3. Circulation changes affect moisture transport
4. Rainfall patterns shift across Thailand
5. Different regions experience different impacts

Strength:
Scientifically explanatory

Weakness:
Requires more technical visual explanation

---

## Option B — Impact-first

1. Thailand experiences unusually dry or wet conditions
2. These conditions are linked to ENSO
3. Pacific Ocean changes affect regional circulation
4. Impacts vary by region and season

Strength:
Immediately relevant to Thai audiences

Weakness:
The mechanism appears later

---

## Option C — Comparison

Left side: El Niño  
Right side: La Niña

Each side shows:
- Pacific conditions
- circulation
- rainfall effect
- regional consequences

Strength:
Easy to compare

Weakness:
May oversimplify neutral and mixed conditions

```


Artifact: `narrative_selected.md`
```markdown
# Selected Narrative

Narrative type:
Comparison with mechanism

Primary message:
ENSO alters Pacific circulation, producing contrasting but spatially uneven rainfall effects in Thailand.

Reading sequence:
1. Pacific Ocean state
2. Atmospheric circulation
3. Moisture transport
4. Thailand rainfall response
5. Regional impacts
6. Main takeaway
```


Artifact: `message_hierarchy.md`
```markdown
# Message Hierarchy

## Level 1 — Main message
ENSO changes how moisture reaches Thailand.

## Level 2 — Supporting messages
- El Niño often increases dry conditions.
- La Niña often increases rainfall.
- Effects differ by season and region.

## Level 3 — Evidence
- circulation direction
- rainfall anomaly
- regional contrast
- selected quantified values

## Level 4 — Context
Definitions, time period, uncertainty, sources
```



## Stage 3 — Visual concept exploration

Do not generate the final image yet. First create several visual concepts.

Each concept should describe:
- dominant visual metaphor
- composition
- reading direction
- visualized evidence
- information modules
- likely strengths
- scientific risks

Artifact: `visual_concepts.md`
```markdown
# Visual Concepts

## Concept 1 — Pacific-to-Thailand flow

Main visual:
A broad Pacific Ocean band leading toward a raised map of Thailand.

Visual sequence:
Ocean temperature → circulation arrows → clouds → regional rainfall effects

Strength:
Shows geographic relationship clearly

Risk:
Thailand may appear too small

---

## Concept 2 — Split comparison

Left:
El Niño

Right:
La Niña

Center:
Thailand acting as the comparison point

Strength:
Easy comparison

Risk:
May become visually symmetrical but scientifically simplistic

---

## Concept 3 — Atmospheric pathway

Main visual:
A ribbon-like circulation path moving from the Pacific to Thailand.

Strength:
Strong visual narrative

Risk:
Arrows may imply a single direct pathway
```


## Stage 4 — Composition planning

At this stage, the workflow creates a blueprint rather than an illustration.

The blueprint should define:

- canvas ratio
- grid
- title area
- main illustration
- information zones
- labels
- negative space
- charts or diagrams
- footer and sources

Artifact: `layout_spec.md`
```markdown
# Layout Specification

## Canvas
16:9 landscape

## Grid
12 columns
6% outer margin
24 px equivalent gutter

## Zones

### Zone A — Title
Columns 1–5
Top 12% of canvas

### Zone B — Pacific mechanism
Columns 1–7
Middle-left

### Zone C — Thailand
Columns 7–10
Center-right

### Zone D — Regional impacts
Columns 9–12
Upper and lower right

### Zone E — Main takeaway
Bottom center

### Zone F — Sources
Bottom edge
```

Artifact: `wireframe.png`
The wireframe should contain only:
- rectangles
- circles
- arrows
- placeholder icons
- approximate labels
- no detailed illustration

The purpose is to validate hierarchy and reading order.

Artifact: `visual_element_register.md`
```markdown
# Visual Element Register

| ID | Element | Function | Evidence link | Priority |
|---|---|---|---|---|
| V01 | Pacific Ocean | geographic context | E01 | Essential |
| V02 | circulation arrows | mechanism | E01 | Essential |
| V03 | Thailand map | impact location | E02, E03 | Essential |
| V04 | rain clouds | wet condition | E03 | Essential |
| V05 | dry soil | dry condition | E02 | Supporting |
```

## Stage 5 — Prompt package creation

A single prompt is usually insufficient. Use a prompt package composed of several coordinated files.

Artifact: `generation_prompt.md`
It should describe:
- subject
- composition
- visual hierarchy
- illustration style
- palette
- scientific constraints
- negative space
- prohibited errors

```markdown
# Generation Prompt

Create a landscape scientific editorial infographic illustration explaining how ENSO affects rainfall in Thailand.

Composition:
Show the Pacific Ocean across the left and center of the image, with Thailand positioned toward the right. Use atmospheric circulation arrows to connect ocean conditions to rainfall patterns over Thailand. Thailand must remain geographically recognizable.

Visual hierarchy:
The Pacific mechanism is the primary visual. Thailand and regional rainfall effects are secondary focal points. Leave clear negative space at the upper left for a title and along the lower edge for explanatory labels.

Style:
Clean vector and semi-3D editorial scientific illustration. Simplified geometric forms, restrained depth, soft edges, minimal outlines, professional rather than cartoonish.

Palette:
Pale aqua background, muted teal ocean, deep blue circulation elements, warm coral for dry conditions, cool blue for wet conditions.

Scientific constraints:
Do not depict rainfall effects as uniform across Thailand. Do not create a direct straight-line causal arrow from the Pacific to one Thai region. Preserve geographic orientation.

Do not include text.
```


Artifact: `negative_prompt.md`

```markdown
# Avoid

- inaccurate Thailand outline
- generic globe icon
- photorealism
- glossy 3D rendering
- heavy black outlines
- excessive decorative bubbles
- unreadable small text
- uniform weather across all of Thailand
- distorted map proportions
- random scientific symbols
- unsupported charts
```

Artifact: `generation_parameters.md`
```markdown
# Generation Parameters

Aspect ratio: 16:9
Output mode: illustration without text
Background: light
Style mode: editorial scientific vector
Required empty areas:
- top-left title zone
- bottom caption zone
```

## Stage 6 — First generation

The first image should be treated as a **composition prototype**, not a final image.

The purpose of iteration 1 is to evaluate:

- major composition
- relative scale
- focal point
- scientific concept
- suitability for later labels
- consistency with the design system

Artifact: `revision_request_v01.md`
```markdown
# Revision Request — Version 01 to Version 02

Preserve:
- overall landscape composition
- pale aqua background
- Pacific-to-Thailand reading direction
- current illustration style

Change:
- correct the geographic outline of Thailand
- move Thailand 8% toward the left
- show heavier rain in northeastern Thailand
- show drier conditions in the southwest
- replace the single direct circulation arrow with a broader curved atmospheric pathway
- reduce decorative bubbles by approximately half

Do not change:
- canvas ratio
- title space
- general palette
```
## Stage 7 — Structural revision

Iteration 2 should resolve composition and scientific structure.


Artifact: `comparison_v01_v02.md`

```markdown
# Version Comparison

| Criterion | V01 | V02 | Status |
|---|---|---|---|
| Thailand shape | Poor | Good | Resolved |
| Regional rainfall | Uniform | Differentiated | Resolved |
| Circulation accuracy | Weak | Acceptable | Improved |
| Visual balance | Strong | Strong | Preserved |
| Negative space | Adequate | Reduced | Needs correction |
```

**Revision gate**
Do not proceed to decorative refinement until these are acceptable:
- composition
- geographic accuracy
- scientific mechanism
- information hierarchy
- major scale relationships
- required empty space

## Stage 8 — Detail and style refinement

Only after the structure is stable should the workflow refine:

- shapes
- line weight
- texture
- shading
- icon consistency
- palette
- small environmental details
- visual transitions

 Artifact: `style_review.md`
```markdown
# Style Review

## Design.md compliance

Illustration mode:
Compliant

Palette:
Accent coral is too saturated

Line style:
Mostly consistent

Depth:
Appropriate, but Thailand shadow is too strong

Texture:
Ocean texture is slightly distracting

Typography space:
Sufficient
```



## Stage 9 — Text and data integration

Image generation should generally produce the illustration without final text. Text, numbers, captions, and source notes should be added in a controlled layout tool.

This avoids:
- misspelled labels
- incorrect numbers
- inconsistent typography
- unusable small text
- unsupported claims introduced by the image model

Artifact: `content_manifest.csv`

|Content ID|Text|Type|Source|Location|Max length|
|---|---|---|---|---|---|
|T01|ENSO and rainfall in Thailand|Title|Project brief|top-left|45 chars|
|T02|El Niño often reduces rainfall...|Key statement|E02|lower-left|80 chars|
|T03|La Niña often increases rainfall...|Key statement|E03|lower-right|80 chars|


## Artifact structure
```markdown
/project-name
│
├── 00_input
│   ├── scientific_sources/
│   ├── reference_images/
│   └── project_brief.md
│
├── 01_research
│   ├── source_inventory.md
│   ├── evidence_map.md
│   └── evidence_to_visual_matrix.csv
│
├── 02_narrative
│   ├── narrative_options.md
│   ├── narrative_selected.md
│   └── message_hierarchy.md
│
├── 03_concept
│   ├── visual_concepts.md
│   ├── concept_scorecard.csv
│   └── selected_concept.md
│
├── 04_layout
│   ├── layout_spec.md
│   ├── wireframe.png
│   └── visual_element_register.md
│
├── 05_generation
│   ├── generation_prompt.md
│   ├── negative_prompt.md
│   └── generation_parameters.md
│
├── 06_iterations
│   ├── draft_v01.png
│   ├── critique_v01.md
│   ├── revision_request_v01.md
│   ├── draft_v02.png
│   ├── critique_v02.md
│   ├── revision_request_v02.md
│   └── draft_v03.png
│
├── 07_content
│   ├── content_manifest.csv
│   └── infographic_with_text.png
└── 08_final
    ├── infographic_master.svg
    ├── infographic_print.pdf
    ├── infographic_presentation.png
    ├── infographic_web.webp
    └── source_notes.md
```