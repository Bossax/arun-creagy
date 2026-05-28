# Plan: CRI Phase 2 Asset (Stock) Indicator Extraction

## 1. Background & Motivation
The Climate Resilience Index (CRI) is evolving from a pure Institutional Readiness (Governance/"Software") framework to a more holistic model that incorporates physical, natural, and social stocks ("Hardware"). 

This plan defines the workflow for extracting asset-based resilience indicators from a curated literature batch using NotebookLM. It explicitly operationalizes the Social-Ecological-Technological Systems (SETS) framework and the "Hardware/Software" metaphor:
- **Assets ($A$) / Hardware:** The structural floor or "Potential Energy" ($P$) of a city (e.g., seawalls, hospital beds, green space, social networks).
- **Governance ($G$) / Software:** The activation logic that turns potential energy into realized service flows ($S$).
- **Lock-in Risk:** High asset stocks without adaptive governance can lead to maladaptive "lock-in" (e.g., rigid infrastructure cited by Markolf et al., 2018).

## 2. Scope & Constraints
This extraction workflow adheres strictly to the "NotebookLM Extraction Discipline" previously established:
1. **NotebookLM is for Extraction Only:** It must not harmonize, deduplicate, or synthesize a final taxonomy.
2. **Source Fidelity (Fail-Fast):** NotebookLM must be restricted to small, explicitly named source packets. It must fail and report missing sources rather than substituting thematic literature.
3. **Structured Output:** All outputs must be flat JSON arrays adhering to a strict schema.
4. **Local Harmonization:** All integration, quality control, and dimensional tagging happen locally in the repo.

## 3. The Asset-Specific Extraction Schema
To capture the "Potential Energy" logic and SETS categorization, NotebookLM will be instructed to output rows in the following JSON format:

```json
[
  {
    "row_kind": "stock_indicator_candidate",
    "source_id_reference": "Short source title",
    "quoted_or_close_paraphrase": "Direct evidence from the text",
    "candidate_asset_label": "Source-backed label (e.g., 'Urban Tree Canopy')",
    "sets_domain": "Social | Ecological | Technological | not explicit",
    "capacity_category": "Coping | Adaptive | Transformative | not explicit",
    "potential_energy_description": "How this asset provides foundational resilience",
    "activation_hint": "Any mentioned governance, plan, or process needed to utilize this asset (The 'Software' link)",
    "lock_in_risk_if_mentioned": "Any mention of rigidity or maladaptation",
    "citation": "(Author, Year, Page/Section)"
  }
]
```

## 4. Staged Extraction Batches
The literature will be processed in focused batches to ensure high-fidelity extraction.

### Batch AS-1: Foundational SETS & Lock-in Concepts
*   **Focus:** Top-level taxonomy of urban physical/social assets and definitions of infrastructural lock-in vs. adaptive capacity.
*   **Target Sources:** 
    *   Markolf et al. (2018) or its proxy summaries.
    *   SETS framework conceptual papers (e.g., Grimm et al., 2018; Muñoz-Erickson et al., 2021).
    *   Consensus.ai synthesis report (`2026-04-22-Taxonomic Inventory...md`).

### Batch AS-2: Physical & Ecological Stocks (Hardware)
*   **Focus:** Granular infrastructural and natural capital stocks (e.g., drainage capacity, grid redundancy, mangrove width, green space accessibility).
*   **Target Sources:** 
    *   Feldmeyer et al. (2019)
    *   Zeng et al. (2022)
    *   IPCC AR6 relevant chapters/annexes on physical adaptation.

### Batch AS-3: Socio-Economic Stocks (Human/Financial Capital)
*   **Focus:** Produced capital, economic buffers, human health baseline, and social network strength.
*   **Target Sources:**
    *   IMF Capital Stock Database Manuals/Reports.
    *   World Bank Changing Wealth of Nations (CWON) excerpts.
    *   Social capital frameworks (e.g., Chang et al., 2021).

## 5. Standard Prompt Template
This prompt will be used for all AS-batches, adjusting only the named source packet.

``` 
You are assisting with extraction for the CRI capacity tagging dictionary. 
Your specific task is to extract "Hardware" (Asset/Stock) indicators. 
In our framework, Assets represent "Potential Energy" — the physical, natural, or social structures that provide a foundation for resilience.

Check if these exact source titles are present in the notebook:
- [SOURCE 1]
- [SOURCE 2]

If any are missing, stop and return only: {"error": "missing_sources", "missing": [list missing titles]}

Otherwise, extract up to 20 raw rows from ONLY these sources. Focus on:
1. Specific examples of Technological (Physical), Ecological (Natural), or Social assets/stocks.
2. How these assets provide foundational resilience (Potential Energy).
3. Any hints in the text about what plans, rules, or governance (Software) are needed to activate these assets.
4. Any mentions of "lock-in", rigidity, or maladaptation related to static infrastructure.

Requirements:
1. Return a flat JSON array output.
2. One row per source statement.
3. Keep duplicates/competing labels across sources; do NOT harmonize.
4. Fields must be source-near; use "not explicit" if the source doesn't support a field.
5. Provide a reference list at the end.

[Insert JSON Schema Here]
```

## 6. Local Processing & Verification
1. **Save Raw Outputs:** Save NotebookLM responses verbatim to `ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/responses/`.
2. **Flatten & QC:** Ensure JSON validity and check that the `activation_hint` effectively captures the link between the Asset (Hardware) and Governance (Software).
3. **Register Integration:** Integrate validated rows into `ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/synthesis/asset_indicator_register.md`.
4. **Final Synthesis:** Cross-reference the resulting asset register against the existing Institutional Readiness v1.1 dictionary to identify $M = A - G$ (Mismatch) pairs.