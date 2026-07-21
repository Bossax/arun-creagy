# Layout Specification — Roll-up 1

## Panel

Roll-up 1:
What is climate change risk?

Selected concept:
IPCC diagram as museum object.

Design system:
`DESIGN-01.md`

## Canvas

- Physical size: 60 cm × 160 cm.
- Orientation: vertical portrait.
- Safe side margin: 4 cm minimum.
- Top/bottom hardware caution zone: 8 cm minimum.
- Main working area: y = 8–152 cm.
- Grid: 8 columns.
- Outer margin: 6–7%.
- Background: pale climate light grey `#F1F2F3`.

## Layout principle

Lock scientific diagram legibility first. The main IPCC AR6 diagram must remain the dominant visual. All callouts and decorative elements must serve the diagram, not compete with it.

---

# Vertical zones

| Zone | y-position | Height | Function | Notes |
|---|---:|---:|---|---|
| A | 8–22 cm | 14 cm | Header/title | Roll-up marker, title, subtitle |
| B | 24–48 cm | 24 cm | IPCC AR5→AR6 context strip | Compact adaptation of `SRL-image-0.png`; do not insert full tall screenshot |
| C | 50–106 cm | 56 cm | Main IPCC AR6 response-risk diagram | Dominant adapted/inserted `SRL-image-1.png` |
| D | 52–106 cm | integrated | Translation callouts | Placed around Zone C, outside core diagram |
| E | 108–143 cm | 35 cm | Key risks + maladaptation + cascade bridge | Key-risk chips; prominent maladaptation warning; small cascade strip |
| F | 145–152 cm | 7 cm | Source / footer | S03 source, IPCC attribution, DCCE identity area |

Note:
Zone C is intentionally shorter than the initial 62–74 cm target because Zone E now includes both key risks and the emphasized maladaptation callout. If the main diagram becomes unreadable at this scale, Stage 4 should reduce Zone B before reducing Zone C further.

---

# Zone details

## Zone A — Header / title

Purpose:
Identify the panel and set the conceptual question.

Content:

- Small series marker: `01`
- Title: `What is climate change risk?`
- Subtitle: `IPCC AR6 frames risk as an interaction among hazard, exposure, vulnerability, and response.`

Layout:

- `01` marker in upper-left or upper-right.
- Title left-aligned, spanning 6–7 columns.
- Subtitle directly below title.
- Optional thin DCCE dark-green line below header.

Visual constraints:

- No complex illustration in this zone.
- Keep background clean.

## Zone B — IPCC context strip

Purpose:
Show that the IPCC risk framework evolved from AR5’s hazard–exposure–vulnerability model to AR6’s addition of response risk and complexity.

Source image:
`00_input/reference_images/SRL-image-0.png`

Layout:

- Use as compact two-step strip:
  - left mini-panel: AR5 risk graphic;
  - right mini-panel: AR6 additions.
- Use arrow or progression marker between the two panels.
- Caption: `IPCC risk framing evolved from AR5 to AR6.`

Visual constraints:

- Crop/adapt; do not use full screenshot.
- Preserve scientific meaning and category colors.
- Keep labels large enough to read.

## Zone C — Main IPCC AR6 response-risk diagram

Purpose:
Serve as the central scientific anchor.

Source image:
`00_input/reference_images/SRL-image-1.png`

Layout:

- Centered in the panel.
- Occupies approximately 44–48 cm width within safe margins.
- Keep white/pale field around the diagram.
- Preserve category positions:
  - hazard left;
  - vulnerability top;
  - exposure right;
  - response bottom;
  - risk center.

Visual constraints:

- Do not recolor category meanings.
- Do not overlay explanatory body text inside the diagram.
- If redrawn, preserve all relationships.

## Zone D — Translation callouts

Purpose:
Translate IPCC terms into plain language.

Callouts:

1. Risk — potential adverse consequences.
2. Hazard — climate conditions that can cause harm.
3. Exposure — what is in harm’s way.
4. Vulnerability — sensitivity and limited capacity to cope/adapt.
5. Response — decisions that can reduce or create risk.

Layout:

- Position callouts outside the main diagram field.
- Use thin grey connector lines with white circular endpoints.
- Use small category-color chips.
- Keep callout text to one short sentence each.

Visual constraints:

- Avoid crossing connector lines.
- Avoid covering IPCC labels.
- Do not add decorative icons inside the diagram.

## Zone E — Key risks + maladaptation + cascading bridge

Purpose:
Make the risk concept concrete and emphasize that response risk/maladaptation can create more risk.

### E1 — Key risks module

Content:

Header:
`Key risks make risk concrete`

Supporting:
`Potentially severe risks warrant attention because of their magnitude, likelihood and timing, and the ability to respond.`

Icon cards:

- Coastal systems — sea-level rise, waves and storms can affect ecosystems, livelihoods and settlements together.
- Ecosystems — climate conditions beyond tolerance can erode habitats, species and ecosystem services.
- Infrastructure and services — extreme conditions can disrupt water, energy, transport and essential services.
- Health and cultural heritage — climate risks can affect health, living standards and what communities value.
- Food and water security — heat, drought and rainfall variability can undermine reliable food production and water access.

Layout:

- Use five compact two-line icon cards in a 2-row cluster.
- Use subdued icon style based on low-poly reference.
- Keep each explanation to one short sentence; no Thailand place names, statistics or ranking.

Visual caution:
These are illustrative IPCC key-risk domains, not a Thailand risk assessment.

### E2 — Maladaptation warning callout

Content:

Primary:
`Maladaptation warning`

Supporting:
`A response meant to reduce risk can create more risk if it locks in vulnerability, shifts harm, or limits future choices.`

Layout:

- Amber/orange warning panel, visually stronger than normal callouts.
- Attach visually to the response area of Zone C if possible using a connector.
- Use lock-in or forked-path icon.

Visual constraints:

- Emphasize without overpowering the central magenta Risk node.
- Do not imply all adaptation is maladaptive.

### E3 — Cascading-risk bridge

Content:
`Risks can cascade through connected systems.`

Layout:

- Small linked-node strip at bottom of Zone E.
- Treat as a bridge to later roll-ups, not the main story.

## Zone F — Footer / sources

Purpose:
Source attribution and institutional identity.

Content:

- `Source: IPCC AR6 WGI/WGII risk framework extract (S03).`
- `IPCC diagrams inserted/adapted from reference figures in project folder.`
- DCCE logo/identity area if available.

Layout:

- Footer line in DCCE dark green.
- Source text in neutral grey.
- Logo area right-aligned if used.

---

# Text density target

Maximum visible words:
120–160 words.

Priority text:

1. Title.
2. Subtitle.
3. Five term callouts.
4. Maladaptation warning.
5. Key-risk labels.
6. Footer source.

If space is tight:

1. Shorten context strip caption.
2. Reduce cascading-risk bridge.
3. Reduce key-risk labels.
4. Do not reduce main diagram scale unless unavoidable.

---

# Production notes

- Use actual IPCC reference diagrams during layout assembly, not image-generation approximations.
- If the diagrams are redrawn for print clarity, preserve category colors, positions, and relationship logic.
- The generated/background illustration should not contain final labels.
- Final labels and source notes should be added in layout software.
