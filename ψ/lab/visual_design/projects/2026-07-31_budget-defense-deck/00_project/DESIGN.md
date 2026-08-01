# DESIGN.md — Reference Style Extraction: Minimal Corporate

## 0. Project Metadata

### Project name
`National Climate Adaptation Platform Budget Defense Widescreen Deck`

### Date
`2026-07-31`

### Prepared by
`Antigravity Visual Design System`

### Intended outputs
- [x] 16:9 presentation graphic (4 slides)
- [x] Diagram set
- [x] Mock-up layouts

### Intended audience
`DCCE Director, budget scrutinizers, and ministry-level decision-makers.`

### Primary communication goal
`Establish technical credibility, structural urgency, and data governance integrity to defend the 25M THB budget envelope.`

---

## 1. Visual Vibe & Reference Set

### 1.1 Shared characteristics
- **Minimal Grid**: Strong alignment to vertical and horizontal columns.
- **High-Density Data**: Clear callouts for statistics and indicators.
- **Decoupled Architecture**: Clean division between the dark navigation/visual borders and light cards.
- **Corporate Editorial**: Technical, precise, and professional.

### 1.2 Outlier characteristics
- No illustrations of generic characters, climate clip-art (e.g. melting globes), or decorative abstract circles.

### 1.3 Style synthesis statement
`A high-precision, abstract-geometric corporate system built on a dark Space Indigo to Deep Twilight canvas. The layout uses structured grids, precise line-and-node connectors, modular geometric planes, restrained Honeydew confirmation states, and a single Signal Yellow priority accent. Every visual must explain a system relationship; no decorative climate imagery is permitted.`

---

## 2. Style DNA

### 2.1 Style keywords
`[minimal]`  
`[corporate]`  
`[technical]`  
`[restrained]`  
`[geometric]`  
`[structured]`

### 2.2 Style spectrum
- **Formality**: formal (`5`)
- **Complexity**: balanced (`3`)
- **Geometry**: geometric (`5`)
- **Realism**: abstract/stylized (`2`)
- **Depth**: flat / subtle layering (`2`)
- **Emotional tone**: neutral/analytical (`2`)
- **Information density**: dense (`4`)
- **Decorative intensity**: restrained (`1`)

### 2.3 Core style rule
> Every visual should feel like a high-precision technical schema or system architecture dashboard, never like a casual marketing presentation or generic flat vector cartoon.

---

## 3. Design Principles

### Principle 1 — Function over Decoration
Every shape, border, and line must serve an analytical or navigational purpose (e.g. bounding container, pipeline connector, or data grid).

### Principle 2 — Structured Contrast
Maintain a strict contrast ratio using `--honeydew` for typography against the dark `--space-indigo` / `--deep-twilight` canvas. Use `--vivid-royal` only for active system paths and `--signal-yellow` for one decisive metric or approval marker per slide.

### Principle 3 — Clear Reading Path
Widescreen slides are designed for left-to-right scanning: Title and high-level context on the left, dominant visual/schema in the center-right, and key takeaways/metadata on the far right.

### Principle 4 — Technical Authenticity
All diagrams (CDM structures, BTR flowcharts, and sitemaps) must represent the actual system logic of the CRDB project, ensuring that the visual is technically accurate and auditable.

---

## 4. Composition System

### 4.1 Dominant composition type
- [x] Split comparison (Slide 1)
- [x] Modular grid (Slide 2 & 4)
- [x] Left-to-right pipeline flow (Slide 3)

### 4.2 Main visual anchor
- **Subject type**: System flowcharts, interactive mockups, and database schemas.
- **Recommended size**: 40–55% of the slide area.
- **Placement**: Right or Center-Right.
- **Function**: Explains the technical mechanism and design structure.

### 4.3 Reading path
Slide Title (Top-Left) → Context Brief (Left Column) → Main Technical Visual/Schema (Center-Right) → Key Statistics / Metadata Labels (Right Margin).

### 4.4 Grid (16:9 Widescreen)
- **Columns**: 12-column grid.
- **Outer margin**: 5% on all sides.
- **Gutter**: 2% between blocks.

---

## 5. Shape Language

### 5.1 Dominant shapes
- Rounded rectangles (4px to 6px border radius for modern, clean containers).
- Lines and nodes (connecting database and architecture elements).
- Thin borders.

### 5.2 Edge quality
- **Corner style**: Softly rounded (4px radius).
- **Outline style**: Thin (1px) borders for card containers.
- **Outline color**: `--glaucous` (#7180b9).

### 5.3 Containers
- **Preferred**: Simple structured translucent dark card panels.
- **Avoid**: Decorative badges, speech bubbles, circular highlight rings.

---

## 6. Illustration & Icon System

### 6.1 Illustration mode
- [x] Flat vector / Technical diagrams
- [x] Mock-up interfaces

### 6.2 Icons
- **Icon family**: Clean outline icons with consistent 1.5px stroke weight.
- **Container**: None or square containers with transparent/dark fills and `--glaucous` borders.

### 6.3 Exclusions
- Do not use cartoon drawings, generic clip-art plants/trees, or human figures.
- Do not overlay text directly on generated artwork. Keep text editable.

---

## 7. Color System (Custom Theme)

### 7.1 CSS Custom Properties
```css
:root {
  --space-indigo: #171738ff;  /* Primary dark neutral: main titles, headers, dense body text */
  --deep-twilight: #2e1760ff; /* Secondary dark: sub-headings, panel headers, accent text */
  --vivid-royal: #3423a6ff;   /* Primary accent: metric values, status nodes, active highlights */
  --glaucous: #7180b9ff;      /* UI neutral: card borders, connection lines, axis labels */
  --honeydew: #dff3e4ff;      /* Confirmed state and high-contrast label accent */
  --signal-yellow: #fde74cff; /* Restricted: one decisive priority or approval signal per slide */
}
```

### 7.2 Color Proportion
- **Canvas/Background (`--space-indigo` + `--deep-twilight`)**: 75%
- **Active system paths (`--vivid-royal`)**: 10%
- **Dividers/Borders (`--glaucous`)**: 10%
- **Confirmed states (`--honeydew`)**: 4%
- **Priority accent (`--signal-yellow`)**: 1%

---

## 8. Typography System

### 8.1 Type roles

| Role | Font Family | Weight | Case | Color |
|---|---|---|---|---|
| Main title | Outfit / Inter | Bold (700) | Sentence | `--honeydew` |
| Subtitle | Outfit / Inter | Semi-Bold (600) | Sentence | `--honeydew` |
| Section heading | Inter | Medium (500) | Sentence | `--honeydew` |
| Key number | Outfit / Monospace | Bold (700) | Uppercase | `--signal-yellow` |
| Body text | Inter | Regular (400) | Sentence | `--honeydew` |
| Caption / Lineage | Monospace | Regular (400) | Uppercase | `--glaucous` |

### 8.2 Text inside generated imagery
- All diagrams and schemas generated by subagents must use placeholder containers. Text, labels, and numbers are added later as editable layers.
