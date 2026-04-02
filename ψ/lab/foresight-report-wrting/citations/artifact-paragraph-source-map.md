# Foresight 2590 – Artifact Paragraph → Source Map (Template)

> Map artifact paragraphs and local reference numbers to canonical `SRC_ID`s.

Use this file to document how evidence artifacts support later report claims.

## Table 1 – Artifact registry (optional but recommended)

Assign a stable `ART_ID` to each artifact file involved in evidence and drafting.

| ART_ID | Artifact_Title | Artifact_File_Path | Artifact_Type | Notes |
|--------|----------------|--------------------|---------------|-------|
| ART-EXAMPLE-CH2-ROUND1 | Chapter 2 – Round 1 draft | ψ/lab/foresight-report-wrting/artifacts/2026-03-29_ch2-round1-draft.md | draft | Example placeholder row; extend with real artifacts. |
| ART-VULN-SBP-ANALYSIS | Child and Youth Vulnerability in Thailand’s Southern Border Provinces | ψ/lab/foresight-report-wrting/artifacts/Child and Youth Vulnerability in Thailand’s Southern Border Provinces.md | memo | Deep-research analytical memo on conflict, identity, institutional trust, and youth vulnerability in the southern border provinces. |
| ART-CH1-DRAFT2-OPENING | Chapter 1 Draft 2 – Opening and scope subsections | ψ/lab/foresight-report-wrting/artifacts/2026-04-02_ch1-draft2-working-assembly.md | draft | Working assembly file for Chapter 1 Draft 2; contains includes for subsections 1.1–1.4. |
| ART-CH3-DRAFT2 | Chapter 3 Draft 2 – Future images and scenarios | ψ/lab/foresight-report-wrting/artifacts/2026-04-02_ch3-draft2-working-assembly.md | draft | Working assembly file for Chapter 3 Draft 2; references subsections 3.1–3.4. |
| ART-CH4-DRAFT2 | Chapter 4 Draft 2 – Strategy and pathway | ψ/lab/foresight-report-wrting/artifacts/2026-04-02_ch4-draft2-working-assembly.md | draft | Working assembly file for Chapter 4 Draft 2; aggregates subsections 4.1–4.8. |

## Table 2 – Artifact paragraph → local ref → source

Fine-grained mapping of artifact paragraphs (or blocks) to both local reference numbers and canonical `SRC_ID`s.

| ART_ID | ART_PAR_ID | Location_Anchor | Evidence_Summary | LOC_REF_Label | SRC_IDs | Evidence_Mode | Status | Notes |
|--------|------------|-----------------|------------------|---------------|--------|---------------|--------|-------|
| ART-EXAMPLE-CH2-ROUND1 | CH2-P05 | Opening paragraph on access and trust | Summarizes how access barriers erode trust in institutions. | 1 | SRC-EXAMPLE-TH-LAW-EDU-2542 | summary-of-source | todo | Example row; replace with project-specific entries. |
| ART-VULN-SBP-ANALYSIS | VULN-P-MECHANISMS | Section “Mechanisms Linking Insecurity and Declining Institutional Trust” | Summarizes mechanisms linking conflict, security measures, language and procedural barriers to service avoidance and institutional distrust among children, youth, and caregivers. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Paragraph cluster around mechanisms of trust erosion and feedback loops; primary evidence anchor for chapter 2 signals-intro claims. |
| ART-CH1-DRAFT2-OPENING | CH1-P01-OPENING2590 | Opening vision for child and youth lives in 2590 in the southern border provinces | Describes desired future life conditions for children and youth in the three southern border provinces in 2590, grounded in existing vulnerability and context evidence; contains placeholders where quantitative evidence will be added later. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 1.1 opening; evidence adequacy to be reviewed once more sources are linked. |
| ART-CH1-DRAFT2-OPENING | CH1-P02-OBJECTIVES | Formal list of report objectives | Presents a structured list of the foresight report’s objectives for children and youth in the three southern border provinces. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 1.2; some objectives may later draw on additional policy and programme documentation. |
| ART-CH3-DRAFT2 | CH3-P01-HOWTO-SCENARIOS | Opening subsection on how to read the scenarios | Explains the role of scenarios in the report and proposes shared questions for comparing the four worlds. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 3.1; additional mapping to quantitative and legal sources to be added later. |
| ART-CH3-DRAFT2 | CH3-P02-BASELINE | Baseline future narrative | Describes the baseline 2590 future if current trends in learning pathways, household economy, digital access, and trust continue without major structural change. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 3.2; evidence adequacy to be reviewed once more sources are registered. |
| ART-CH3-DRAFT2 | CH3-P03-MATRIX-INDICATORS | Scenario axes and indicator set | Defines the two main uncertainty axes and an indicator set that separates belonging/identity-security from economic uses of identity. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 3.3; will later draw on additional economic and education policy sources once registered. |
| ART-CH3-DRAFT2 | CH3-P04-SCEN-1-4 | Scenario narratives 1–4 | Summarizes the four scenarios using shared indicators, highlighting how structural conditions shape child and youth lives. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 scenario narratives; further evidence links to be added for specific mechanisms. |
| ART-CH3-DRAFT2 | CH3-P05-DESIRABLE | Desirable future vision and conditions | Sets out the desirable future vision and minimum system conditions for 2590 against which scenarios will be compared in Chapter 4. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 3.4; normative anchor for later strategic backcasting. |
| ART-CH4-DRAFT2 | CH4-P01-MANDATE | Chapter 4 mandate and design principles opening | Sets out the role of Chapter 4 in translating the desirable future into strategic pathways and leverage points for children and youth in the southern border provinces. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 4.1; additional legal and programme sources to be added once registered. |
| ART-CH4-DRAFT2 | CH4-P02-PATHWAY | Strategic pathway and Three Horizons narrative | Describes the backcasting logic and Three Horizons framing used to organise near-term, transitional, and long-term strategic actions toward 2590. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 4.2; will later be cross-checked against foresight methodology sources. |
| ART-CH4-DRAFT2 | CH4-P03-PORTFOLIO | Portfolio-of-actions framing | Explains the four types of actions (Quick Wins, Transitional, Transformational, Preventive & Protective) and how they interact to support child and youth futures under uncertainty. | none | SRC-MEMO-VULN-SBP-2026 | synthesis | draft | Draft 2 subsection 4.4; evidence adequacy to be reviewed once economic and governance sources are registered. |



**Column guidance**

- `ART_ID` – From the artifact registry above.
- `ART_PAR_ID` – Stable paragraph/block ID within the artifact, e.g. `CH1-P03`, `SCEN-A-P02`, `BOX1-P01`.
- `Location_Anchor` – Short description or heading text to help humans find the paragraph quickly.
- `Evidence_Summary` – One sentence on what the paragraph is asserting or describing.
- `LOC_REF_Label` – Local reference identifier used inside the artifact, e.g. `1`, `2`, `a`, `b`, or `none`.
- `SRC_IDs` – Comma- or semicolon-separated list of canonical source IDs from `citation-registry.md`.
- `Evidence_Mode` – e.g. `direct-quote`, `paraphrase`, `synthesis`, `mixed`.
- `Status` – e.g. `todo`, `draft`, `checked`, `disputed`.
- `Notes` – Optional clarifications.

## Table 3 – Local reference legend per artifact (optional)

If some artifacts carry their own local numbering scheme (e.g. `[1]`, `[2]`, `[3]` at the end), this table links those numbers to `SRC_ID`s once for reuse.

| ART_ID | LOC_REF_Label | LOC_REF_Description | SRC_IDs | Notes |
|--------|---------------|---------------------|--------|-------|
| ART-EXAMPLE-CH2-ROUND1 | 1 | Example local reference for conflict report | SRC-EXAMPLE-TH-LAW-EDU-2542 | Replace with actual mapping for artifacts that use local numbering. |

