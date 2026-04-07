# CRI–CBI Integration Plan

Purpose: academically robust approach to incorporate the Capacity-Based Index (CBI) into the existing CRI Phase 2 methodology and the capacity tagging dictionary, without collapsing the SES + governance design into a simple ranking.

This plan is structured in two main tracks:
1. Analyze the CBI approach from the perspective of the CRI Phase 2 core methodology.
2. Design a second version of the capacity tagging dictionary that uses CBI indicators as baseline proxies where appropriate and introduces new indicator concepts where justified.

---

## Track 1 – Analyze the CBI approach against CRI Phase 2 methodology

### Step 1.1 – Reconstruct the implicit CBI design decisions

- Extract and summarize the CBI design from:
  - [`ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md)
  - [`ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-Thailand_CBI_Report-AI-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-Thailand_CBI_Report-AI-generated-P-Tik.md)
- For CBI, document explicitly:
  - Conceptual frame: 3 pillars × 2 dimensions, capacity definitions, scope (77 provinces, secondary data).
  - Indicator selection filters: measurability, data sources, units, positive/negative direction.
  - Mathematical structure: normalization, weighting, aggregation to a single CBI score and 4 capacity levels.
  - Policy and communication goals: how DCCE intends to use the national ranking and pillar scores.

### Step 1.2 – Align and contrast with CRI Phase 2 methodology

- Use [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md) as the reference.
- Build a structured comparison table with axes such as:
  - Conceptual stance: SES lens, governance and process emphasis, educational goals.
  - Measurement stance: baseline versus target metrics, two-speed design, data-richness overlay.
  - Product stance: profile plus gap report versus composite ranking.
  - Data sources and feasibility: reliance on LPA, Sustainable City, DDPM, MOPH, NSO, NESDC, etc.
  - Risk and defensibility: treatment of proxies, explicitness about limitations.
- Identify where CBI is clearly compatible (e.g. pillars, asset versus process split, admin-data-first) and where it diverges (e.g. equal weighting, single-score ranking, asset bias).

### Step 1.3 – Map CBI indicators into the SES and governance lens

- For each of the 22 CBI indicators (CA1–TP3):
  - Classify under Coping, Adaptive, Transformative and Asset versus Process.
  - Identify the primary governance function (e.g. finance, planning, DRM operations, zoning, participation, innovation).
  - Interpret where the indicator sits in SES terms (system components, agents, institutions, feedbacks, cross-scale issues).
- Produce a short narrative for each pillar summarizing how the 22 indicators collectively represent, and fail to represent, SES-consistent capacity.

### Step 1.4 – Define academic criteria for “acceptable integration”

- Based on [`ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md`](ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md) and its cited frameworks:
  - Codify criteria for indicators and indices to be considered academically robust under the CRI Phase 2 design, for example:
    - Alignment with process- and governance-oriented definitions of capacity.
    - Explicit baseline versus target distinction and an upgrade path.
    - Transparent treatment of data quality and missingness.
    - Avoidance of misleading precision in composite scores when proxies are weak.
    - Compatibility with SES thinking and cross-project coherence (CRI, CRDB, BTR).
- Use these criteria as the “accept or modify” filter for any proposed CBI integration in Track 2.

---

## Track 2 – Design a CBI-aware tagging dictionary (v2)

### Step 2.1 – Create a CBI–dictionary crosswalk

- Start from the existing long-list in [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md).
- For each CBI indicator (CA1–TP3):
  - Determine whether it maps cleanly onto an existing indicator concept (e.g. emergency planning, drills, adaptation plans, zoning, innovation, participation).
  - Note where it partially overlaps but introduces a distinct emphasis (e.g. shelters and emergency medical personnel as explicit coping assets, green buffers as ecosystem-related transformative asset).
  - Flag where no existing concept captures the essence of the CBI indicator and SES lens suggests it is substantively important.

### Step 2.2 – Define CBI usage types for the dictionary

- Introduce a typology to categorize the role of each CBI indicator in the v2 dictionary:
  - Type A – **Baseline proxy for existing concept**: CBI indicator is one operationalization of a concept already present in the dictionary; use it as a preferred or example baseline proxy.
  - Type B – **New indicator concept warranted**: CBI indicator reveals a relevant capacity dimension that is not yet represented in the conceptual long-list but fits the SES and 3-pillar asset versus process frame; define a new indicator concept anchored in literature.
  - Type C – **Supplementary or contextual only**: CBI indicator is useful for descriptive context or validation but should not be part of the core tagging dictionary (e.g. because it duplicates fiscal wealth or introduces too much asset bias).
- For each CBI indicator, assign a type with a short justification referencing Track 1 criteria.

### Step 2.3 – Draft the capacity tagging dictionary v2 structure

- Clone the structure of [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md) into a v2 file (for example [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md)).
- For each indicator concept in v2:
  - Update or add the **Baseline proxy** column to reference CBI indicators where they are Type A or Type B, including units and data sources.
  - Retain or refine **Target (process-quality)** metrics based on the original dictionary and SES literature; do not collapse Target into CBI’s baseline design.
  - Adjust **data-richness/confidence** scores in light of the CBI metadata (collection frequency, level, current data status, limitations).
  - Document whether a CBI indicator is required, optional, or one of several possible proxies for that concept.

### Step 2.4 – Introduce new indicator concepts for CBI Type B

- For each CBI indicator marked Type B in Step 2.2:
  - Draft a new indicator concept entry with:
    - Concept definition in SES and governance terms.
    - Baseline proxy anchored in CBI (with metadata from the manual).
    - Target metric that moves beyond simple presence or quantity toward process quality or structural change.
    - Capacity tier, governance function, and evidence anchors (including external literature where available).
  - Ensure the new concepts preserve the 3-pillar and asset versus process structure and do not over-extend the index into unrelated domains.

### Step 2.5 – Academic justification and documentation

- Create a short methodological note (for example [`ψ/incubate/DCCE/CRI/output/CRI_CBI_Bridging_Method_Note.md`](ψ/incubate/DCCE/CRI/output/CRI_CBI_Bridging_Method_Note.md)) that explains:
  - The derivation of tagging dictionary indicator concepts from urban resilience frameworks (summarizing [`CRI_Urban_Resilience_Frameworks_Analysis.md`](ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md)).
  - How and why CBI indicators have been integrated as Baseline proxies or new concepts.
  - How the two-speed measurement stance and data-richness overlay remain intact despite using CBI.
  - Which CBI choices are accepted, which are modified, and which are deliberately excluded, with reasoning.
- This note becomes the primary academic reference to defend the integration in reports, hearings, and future peer review.

### Step 2.6 – Validation and iteration loop

- Run an internal validation pass using one or two provinces:
  - Tag indicators with the v2 dictionary using CBI-based Baseline proxies where defined.
  - Compare resulting capacity profiles to pure CBI pillar scores and to CRI conceptual expectations.
- Check for:
  - Over-dominance of asset indicators in any pillar.
  - Loss of important process signals originally in the dictionary.
  - Any contradictions with SES framing or Phase 2 educational goals.
- Adjust the v2 dictionary and bridging note based on findings, then lock the version for use in implementation modes.

---

## Workplan Checklist

- [ ] Track 1: CBI design reconstruction and comparison table
- [ ] Track 1: SES and governance mapping for all 22 CBI indicators
- [ ] Track 1: Academic criteria for acceptable CBI integration defined
- [ ] Track 2: CBI–dictionary crosswalk with Type A, B, C classification
- [ ] Track 2: Draft of tagging dictionary v2 structure with CBI-aware Baseline proxies
- [ ] Track 2: New indicator concepts authored for CBI Type B indicators
- [ ] Track 2: Bridging methodological note drafted and linked to evidence
- [ ] Track 2: Validation on pilot provinces and final adjustment of v2 dictionary

