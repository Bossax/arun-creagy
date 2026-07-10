# BTR-to-Sitemap Structural Gap Analysis Plan
**Date**: 2026-07-10  
**Status**: PROPOSED PLAN  
**Objective**: Shift the compliance audit direction from "what sitemap nodes are empty" (Content Gaps) to "what A-BTR compliance topics lack dedicated pages on the portal" (Sitemap Structural Gaps), recommending new nodes to support national reporting and public education.

---

## 1. Objectives & Compliance Focus

The primary goal is to ensure the **NCAIF Sitemap** has dedicated, explicit landing zones for all core reporting agendas of the UNFCCC A-BTR guidelines. 

This analysis will identify **Sitemap Structural Gaps** where critical BTR topics are currently forced into general category sections:
1. **Institutional Governance & Interagency Coordination**: (Section 1) National committees, division of labor, subnational coordination, and stakeholder engagement.
2. **Inclusive Adaptation & Local Wisdom**: (Section 3) Gender integration, traditional/indigenous knowledge, and human rights safeguards.
3. **Systemic Barriers & International Support**: (Section 3) The 4 thematic barriers (Data, Institutional, Financial, M&E) and tracking of technology transfer, capacity building, and domestic/international funding.
4. **Long-Term Slow-Onset Threats**: (Section 5) Averting/minimizing slow-onset losses (salinity, sea-level rise, subsidence) vs. sudden-onset disasters.

---

## 2. Proposed Workflow & Execution Steps

### Step 1: Mapping Granularity Analysis (BTR $\rightarrow$ Sitemap)
* **Action**: Analyze the existing mappings in `requirement_sitemap_link` in `a_btr_dissection.db`.
* **Logic**: Classify mapped requirements based on *specificity*:
  * **Strongly Mapped**: Linked to a specific leaf node containing explicit content directives (e.g. `3.2.4` for Loss & Damage).
  * **Weakly Mapped**: Forced into a generic category header or unrelated page because no specific page exists.
* **Metric**: Count the number of `MUST` and `SHOULD` requirements that are "weakly mapped" under each theme.

### Step 2: Identify Missing Sitemap Nodes (Structural Gaps)
* **Action**: Compile a list of compliance subtopics that have a high density of BTR requirements but lack dedicated leaf nodes.
* **Recommendations**: Draft specific structural recommendations for new sitemap nodes.

### Step 3: Document Findings & Propose Sitemap v8.0
* **Action**: Overwrite [`a_btr_to_sitemap_gap_analysis.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/a_btr_to_sitemap_gap_analysis.md) to:
  1. Highlight BTR compliance topics that are unrepresented or crammed.
  2. List proposed additions to the sitemap menu hierarchy.
  3. Include a revised **NCAIF Detailed Sitemap v8.0** containing the newly integrated compliance nodes.

---

## 3. Verification Rules & Success Criteria

* **Thematic Alignment**: 100% of the 379 A-BTR requirements must map to an explicit, contextually appropriate leaf node (not a generic header).
* **Governance Gate**: Dedicated pages must be provided for GESI (Gender Equality & Social Inclusion), institutional governance structures, support needed vs. received, and slow-onset hazards.
