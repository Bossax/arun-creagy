# Collaborative Writing Plan: TOR 5.5 Climate Risk Articles

This document establishes the official collaborative framework and operational blueprint for the Human-in-the-Loop (HITL) execution of **TOR 5.5** (Climate Risk and Adaptation Articles). It integrates **NotebookLM MCP verification guardrails**, the **`writing-th`** strategic drafting pipeline, and the iterative **`style-capture`** engine.

---

## 🎯 0. Pre-Start Gate: List Finalization & Style Calibration

Before creating directories or starting Phase 1 (Core Extraction) for any article, we must clear this two-part gate:

### A. Finalizing the Article List
*   **Action**: Check and lock the current 10 selected studies at [TOR5.5_Articles_Summary_Table.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/TOR5.5_Articles_Summary_Table.md).
*   **Rule**: Any replacements, updates, or metadata changes to the candidate studies must be finalized at this gate. Once approved, the target list is locked.

### B. Style Calibration & Requirement Feeding
*   **Action**: The human expert feeds:
    1.  **Gold-Standard Samples**: Example articles or reports representing the target voice, length, and style.
    2.  **Writing Requirements**: Guidelines for target audience (public-friendly), specific formatting constraints, or official terminology.
*   **AI Process**: The agent processes these inputs via the **`style-capture`** engine to build the initial `STYLE_PACK_TOR5.5-Articles.md` in `ψ/memory/style/`. This establishes the baseline lexicon and formatting rules *before* we draft the first article.

---

## 📂 1. Directory & Artifact Architecture

To keep the work organized and prevent context drift, each of the 10 selected papers will have its own dedicated subdirectory under the output folder:

`C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRDB\output\TOR5.5_article_and_infoghraphic\`

### Subdirectories for the 10 Articles:
1. `ART01_CMIP6_Water_Crop/` - CMIP6 crop yield & water footprint (Arunrat et al., 2021)
2. `ART02_ChaoPhraya_Rice_Adaptation/` - Lower Chao Phraya rice adaptation (Vilavan et al., 2024)
3. `ART03_PLOS_Infectious_Diseases/` - Projections of 9 infectious disease risks (PLOS NTD, 2024)
4. `ART04_ENSO_Precipitation_Northeast/` - ENSO & precipitation variability in Northeast Thailand
5. `ART05_Coastal_Erosion_Southern/` - Hard vs. soft defense structures (PMC, 2022)
6. `ART06_Species_Protected_Areas/` - Wildlife & plant climate migration (PMC, 2018)
7. `ART07_Urban_Heat_Stress_Bangkok/` - Urban heat stress and human health in Bangkok
8. `ART08_Tourism_Risk_GIZ/` - Tourism sector risk assessment (Griffith Univ / GIZ, 2018)
9. `ART09_BMR_UrbanSprawl_Floods/` - Sprawl vs. rainfall flood risk in BMR (J Flood Risk Manag, 2024)
10. `ART10_WIM_ExCom_Sea_Level_Rise/` - WIM ExCom sea level rise

### Core Files per Directory:
*   `01_Raw_Extraction.md` — All risks, trends, and qualitative concepts pulled from the source.
*   `02_Decision_Log.md` — Human selections (KEEP/DISCARD) and storytelling connection guide.
*   `03_Verified_Facts.md` — Target-bound metrics, numbers, and exact page/table citations.
*   `04_Final_Draft.md` — Persuasive Thai article (~2 A4 pages) + structured infographic text copy.

---

## 🔄 2. The 4-Phase Operational Workflow

For each article, we will move sequentially through these phases:

```
    [Source Document]
            │
            ▼  (notebooklm-rules Preflight check on source titles)
┌───────────────────────┐
│ Phase 1: Extract      │ ──> Generates: `01_Raw_Extraction.md`
└───────────────────────┘
            │
            ▼
┌───────────────────────┐
│ Phase 2: Decide       │ ──> Read: `02_Decision_Log.md` (Human inputs Storytelling Angle)
└───────────────────────┘
            │
            ▼  (Surgical, targeted query using NotebookLM MCP)
┌───────────────────────┐
│ Phase 3: Verify       │ ──> Generates: `03_Verified_Facts.md` (Cite exact pages/tables)
└───────────────────────┘
            │
            ▼  (Stage 0: Load Style-Pack & Lexicon)
               (Stage 3: Apply Causal Chaining for persuasive Thai flow)
┌───────────────────────┐
│ Phase 4: Draft        │ ──> Generates: `04_Final_Draft.md` (Article + Graphic Copy)
└───────────────────────┘
```

### ✍️ Phase 4 Execution Rule: Produce the Final Draft from Phases 1–3

Phase 4 is the stage that produces the actual final public-facing draft in `04_Final_Draft.md`.

Before drafting, the AI must treat the outputs of the earlier phases as the complete working input set:
- `01_Raw_Extraction.md` provides the structured evidence inventory and topic map.
- `02_Decision_Log.md` provides the human-selected narrative direction, priorities, and framing intent.
- `03_Verified_Facts.md` provides the exact numbers, page anchors, table references, and verified claims that are allowed into the final prose.
- `STYLE_PACK_TOR5.5-Articles.md` provides the active voice, lexicon, anti-AI constraints, and any style-capture updates already learned from prior edits.

The AI must then generate `04_Final_Draft.md` by doing all of the following inside Phase 4:
1. **Load the current style pack first** and preserve any human-edited framing already propagated there.
2. **Use only verified facts** from `03_Verified_Facts.md` for numerical claims, scenario comparisons, citations, and technical assertions.
3. **Use `01_Raw_Extraction.md` only as contextual support** for qualitative structure, issue grouping, and concept framing when those points have already been verified or do not require exact numeric citation.
4. **Use `02_Decision_Log.md` as the narrative contract** for the opening hook, body flow, article emphasis, and adaptation takeaway.
5. **Write the full final article and infographic copy directly into `04_Final_Draft.md`** without reverting to a generic baseline voice or bypassing the human-selected framing.

If evidence gaps are still discovered during drafting, the AI must stop and return to Phase 3 rather than inventing connective facts inside Phase 4.

### 🔍 Phase 1 Execution Protocol: Adaptive Topic-First Exploration

To prevent confirmation bias and ensure high-recall extraction, the AI must not use static, pre-canned queries. Instead, Phase 1 must be executed using a three-step progressive feedback loop.

#### 🔄 Execution Modes: Automated MCP vs. Hybrid Manual-Paste Loop
To prevent context congestion, save AI token budget, and handle browser-session locks or timeouts, Phase 1 can be executed in two modes:
1. **Automated MCP Mode**: The AI agent manages the browser session and executes Step 1–3 queries sequentially, appending outputs to `raw-copy.md`.
2. **Hybrid Manual-Paste Mode (Recommended)**: 
   - **Step A**: The AI automatically creates or updates the `raw-copy.md` file in the target article directory, prepopulated with the exact, custom queries for that paper (Step 1A - 1E) to facilitate the human's copy-paste workflow.
   - **Step B**: The human runs these pre-filled queries in the NotebookLM Web UI and pastes the raw responses directly below each query block in `raw-copy.md`.
   - **Step C**: The AI reads `raw-copy.md` to synthesize the canonical `01_Raw_Extraction.md` JSON.

#### 📥 Raw Extraction Persistence Rule
All new NotebookLM extraction output must be persisted first in `raw-copy.md` inside the target article directory.

- `raw-copy.md` is the canonical landing zone for **verbatim NotebookLM output** before any local synthesis, flattening, or promotion into other artifacts.
- If additional retrieval is needed after Phase 2 because the decision log, edited draft, or narrative blueprint reveals evidence gaps, the AI must **update `raw-copy.md` with a new query block packet** rather than bypassing the file.
- The human then pastes the new NotebookLM responses directly under those newly added query blocks in the same `raw-copy.md` file.
- The AI may then use the expanded `raw-copy.md` to enrich `01_Raw_Extraction.md` if the material remains extraction-grade, or to construct `03_Verified_Facts.md` when the retrieval is targeted, citation-bound, and being used as formal verification.

#### 🔁 Phase 3 Query Refresh Rule
When entering Phase 3 or any Phase-2.5 / language-first gap-retrieval pass, the AI must inspect the current `02_Decision_Log.md`, edited draft, and `01_Raw_Extraction.md` to identify missing details.

- The AI must then **update `raw-copy.md` to append a dedicated Phase 3 query packet** only for those missing details before any new NotebookLM run occurs.
- Phase 3 retrieval is a **delta-only pass**, not a restart of Phase 1. The AI must avoid re-querying material that is already adequately captured in `01_Raw_Extraction.md` unless the missing need is an exact citation anchor, exact number, exact comparison, or a more precise formulation explicitly required by the decision log or the edited draft.
- These Phase 3 packets should be narrow, source-bound, and extraction-only, focused only on unresolved items such as exact definitions, table-level metrics, figure interpretation, methodological detail, limitations, citation anchors, or mechanism explanations that are still missing.
- The AI must not place fresh NotebookLM output only in chat or only in a temporary note; the new retrieval must be captured under the new Phase 3 query blocks in `raw-copy.md` first.
- This rule applies even when the retrieval is triggered by a richer drafting need rather than by the formal verification file itself.

#### 🎯 Phase 3 Relevance Filter
Before appending any new Phase 3 query block, the AI must explicitly test each candidate query against three filters:

1. **Already Captured Filter**
   - Is the needed content already present in `01_Raw_Extraction.md` with sufficient clarity for the current article?
   - If yes, do not query it again.

2. **Decision-Log Relevance Filter**
   - Is the missing detail required to support a `KEEP` issue, the chosen narrative direction, or a stated narrative blueprint in `02_Decision_Log.md`?
   - If no, do not query it.

3. **Draft-Gap Filter**
   - Is the missing detail explicitly needed to resolve a placeholder, sharpen a causal explanation, support a numeric claim, or complete an argument in the current draft or edited draft?
   - If no, do not query it.

Only queries that survive all three filters should be appended to `raw-copy.md`.

This hybrid pattern acts as the primary recovery and token optimization path for all agents working on this project.

1. **Step 1: Structural Mapping & Topic Discovery**
   - *Action*: Query NotebookLM with a packet of 5 atomic queries to map the paper's outline, variables, tables, figures, and hypothesis.
   - *Standard Query Pack*:
     - **Step 1A (Outline)**:
       `"For the source document \"[Exact Source Title]\": Extract and list the full section outline of the paper. If the document is not found or the title is ambiguous, report that explicitly."`
     - **Step 1B (Variables)**:
       `"For the source document \"[Exact Source Title]\": Identify and list the primary variables, metrics, or qualitative concepts discussed in each section (e.g., climate parameters, agricultural indicators, socioeconomic variables, health/environmental indices)."`
     - **Step 1C (Tables)**:
       `"For the source document \"[Exact Source Title]\": Extract and list only the tables mentioned, along with their exact titles/captions and their analytical focus. Do not summarize or harmonize."`
     - **Step 1D (Figures)**:
       `"For the source document \"[Exact Source Title]\": Extract and list only the figures mentioned, along with their exact titles/captions and their analytical focus. Do not summarize or harmonize."`
     - **Step 1E (Hypothesis & Labels)**:
       `"For the source document \"[Exact Source Title]\": Extract only the core research hypothesis plus named study areas, climate hazards, target variables, and geographical labels. Do not summarize or harmonize."`
2. **Step 2: Adaptive Deepening (Dynamic Branching)**
   - *Action*: Formulate subsequent queries dynamically based on the structure, tables, and variables discovered in Step 1.
   - *Query Guidelines*:
     - **For Agricultural & Biophysical Papers (e.g., ART01, ART02, ART04, ART05, ART06)**:
       - **Step 2A (Sensitivities & Thresholds)**: `"For the source document \"[Exact Source Title]\": Extract specific crop yield sensitivities, crop-water footprints, or climate parameter thresholds (e.g., temperature ranges, rainfall deficits) across different regions, seasons, or scenarios."`
       - **Step 2B (Geographical & District Variations)**: `"For the source document \"[Exact Source Title]\": Extract specific district-level or regional differences in climate vulnerability and adaptation responses mentioned in the paper (e.g., Central Plains vs. Northeast)."`
     - **For Public Health & Social Impact Papers (e.g., ART03, ART07, ART08, ART09, ART10)**:
       - **Step 2A (Statistical Relationships & Odds Ratios)**: `"For the source document \"[Exact Source Title]\": Extract the specific statistical findings, correlation coefficients, or Odds Ratios (ORs) showing the associations between climate exposures (e.g., heat stress, flooding) and specific daily activity or health domains (e.g., sleeping, commuting, working)."`
       - **Step 2B (Socioeconomic Vulnerability & Cascading Impacts)**: `"For the source document \"[Exact Source Title]\": Detail the cascading effects of climate hazards on public health outcomes (e.g., life satisfaction, mental health, disease risk) and identify which specific demographic or socioeconomic groups are most vulnerable."`
     - **Step 2C (Infrastructure & Adaptive Capacity)**: `"For the source document \"[Exact Source Title]\": Extract specific findings related to how infrastructure (e.g., air-conditioning, public transport, green open spaces) or behavioral patterns moderate the impacts of the hazard."`
3. **Step 3: Synthesis & Gap Sweep**
   - *Action*: Target limitations, source data gaps, model parameters, and uncertainties to ensure the public narrative is scientifically grounded.
   - *Standard Query Pack*:
      - **Step 3A (Limitations & Data Gaps)**: `"For the source document \"[Exact Source Title]\": What are the explicit limitations, sample limitations, source data uncertainties, or model parameters (e.g., self-reported bias, lack of baseline data, simulation constraints) that the authors warn about in their discussion or conclusion?"`
      - **Step 3B (Author Recommendations & Adaptation Policies)**: `"For the source document \"[Exact Source Title]\": What concrete adaptation strategies, policy recommendations, or future research directions do the authors propose to address the identified risks?"`

### ✅ Phase 3 Required Outputs

Phase 3 must result in a **complete verification package** for the target article. It is not just a query stage. It must produce all of the following outcomes before the article can move cleanly into Phase 4:

1. **Delta-gap assessment completed**
   - The AI must inspect `01_Raw_Extraction.md`, `02_Decision_Log.md`, the current draft or edited draft, and the active style state.
   - The AI must identify only the still-missing factual, methodological, comparison, citation, or mechanism gaps required for the chosen article direction.

2. **`raw-copy.md` updated when gaps exist**
   - If gaps remain, the AI must append a narrow, source-bound, extraction-only Phase 3 query packet to `raw-copy.md`.
   - These queries must target only what is missing from the earlier extraction and what is required by the decision log and the active draft.

3. **Raw NotebookLM responses captured verbatim**
   - All new retrieval responses must be pasted into `raw-copy.md` under the corresponding Phase 3 query blocks.
   - No fresh NotebookLM output should live only in chat.

4. **`03_Verified_Facts.md` produced or refreshed**
   - Phase 3 must materialize `03_Verified_Facts.md` as the canonical verification layer for the article.
   - This file must contain the exact numbers, exact comparison basis, exact table/figure anchors, page or section citations, and any clarified mechanism explanations needed by the article.

5. **Style capture completed when the edited draft changes reusable voice**
   - If the active edited draft introduces meaningful framing, lexicon, or structural preferences that should shape the final article, the AI must run style capture during Phase 3 and update `STYLE_PACK_TOR5.5-Articles.md` before Phase 4.
   - This is part of Phase 3 execution when such a style delta exists.

6. **Phase 3 completion test passed**
   - The article is Phase-3 complete only when:
     - all required gaps for the chosen narrative are closed,
     - `raw-copy.md` contains any needed new raw retrieval,
     - `03_Verified_Facts.md` contains the verified facts actually needed for writing,
     - and the style pack has been refreshed if the edited draft introduced reusable voice changes.

If any of these outputs is missing, the article has not truly completed Phase 3 and must not be treated as ready for final drafting.

### 📝 Phase 2 Execution Protocol: Rich Contextual Topic Selection

To ensure the human expert has complete narrative visibility and scientific context before selecting topics (KEEP/DISCARD), the AI must **never** generate a blank decision table. 

Instead, the `02_Decision_Log.md` file must be prepopulated with:
1. **Executive Summary**: A robust summary of the study's scope, analytical methods, and data coverage.
2. **Key Scientific Insights**: Detailed explanations of how the climate hazards (e.g., ENSO anomalies, crop sensitivities) directly impact Thailand's sectors, geography, and local communities (the "so what?" of the scientific data).
3. **Traceable Selection Table**: A table linking extracted Issue IDs (`E01`, `E02`, etc.) to clear descriptions of their core concepts.
4. **Narrative Blueprint Placeholders**: Designated placeholders for the human to outline the opening hook, body flow, and adaptation takeaways.

This ensures the decision log acts as a high-signal brief rather than a generic checklist.

---

## 🔁 3. Iterative Style Refinement Loop

To prevent robotic writing and align the articles with your strategic voice, the draft of each article will build upon the style improvements of the previous ones.

```
                  [AI Drafts Article N]
                            │
                            ▼
               [Human Edits/Reviews Article N]
                            │
                            ▼
     [Run /style-capture on Draft vs. Edited Version]
                            │
                            ▼
      [Update STYLE_PACK_TOR5.5-Articles.md Ledger]
                            │
                            └────────────────────────> Calibrates Article N+1 Draft
```

### Steps of the Loop:
1.  **Calibration & Initiation (Stage 0)**: I load the cumulative Style-Pack from [STYLE_PACK_TOR5.5-Articles.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/STYLE_PACK_TOR5.5-Articles.md). If it's the first session, we start with standard [writing-th](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/.agents/skills/writing-th/SKILL.md) rules (e.g., stripping fillers like *"นอกจากนี้"*, *"ยิ่งไปกว่านั้น"*).
2.  **Human Review & Edit (Stage 5)**: Once the AI outputs the draft, you review and edit it. You can correct sentence structure, tone, vocabulary, or storytelling flow.
3.  **Pre-Final-Draft Trigger**: If the edited version is being used as the voice anchor for a later final draft of the same article, the AI must run style capture **before** generating `04_Final_Draft.md`, not only after publication of an earlier draft.
4.  **Linguistic Extraction**: The AI compares the draft and edited files. The **`style-capture`** engine performs a semantic diff to extract:
    *   **Preferred Lexicon**: Words you replaced (e.g., mapping generic verbs to precise strategic terms).
    *   **Linguistic DNA**: Your preferred sentence lengths, hedging habits, and transitions.
    *   **Anti-AI Shield**: Explicit expressions or layouts to avoid.
5.  **Propagation**: The updated rules are written to the master Style-Pack, which I load at the start of drafting the next article **and** at the start of any final-draft regeneration pass for the current article.

---

## 🤝 4. Human-in-the-Loop Collaboration Matrix

| Process | AI Agent Responsibilities (My Work) | Human Expert Responsibilities (Your Work) |
| :--- | :--- | :--- |
| **Extraction** | Uses `notebooklm-rules` to parse candidate sources and extract unverified qualitative concepts (Phase 1). | Selects candidate PDFs or MD source files and assigns them to the article subdirectories. |
| **Story Framing** | Reads the structural blueprint and waits for the selection log to be finalized (Phase 2). | Reviews raw extractions, selects which issues to KEEP/DISCARD, and defines the narrative storytelling hook. |
| **Verification** | Conducts strict, targeted fact-checking, linking numbers and ranges to explicit source citations (Phase 3). | Resolves missing data or ambiguous values by confirming facts directly from the source or external registries. |
| **Strategic Drafting** | Applies the `STYLE_PACK` and Causal Chaining to draft the Thai prose and infographic copy (Phase 4). | Evaluates the draft and edits it to train the style engine (Phase 5). |
| **Guardrails** | Acts as fact gatekeeper—refusing to include any metric or claim in the draft that was not validated in Phase 3. | Respects the fact-checking gate—adds missing numbers to Phase 3 with a source citation before asking to draft. |

---

## 📅 5. Cumulative Tracking Checklist

| Article ID | Source Study | Phase 1 (Ext) | Phase 2 (Dec) | Phase 3 (Ver) | Phase 4 (Dft) | Style Update | Deployed/Sealed |
|---|---|---|---|---|---|---|---|
| **ART01** | Arunrat et al., 2021 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART02** | Vilavan et al., 2024 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART03** | PLOS NTD, 2024 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART04** | ENSO Precipitation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART05** | PMC, 2022 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART06** | PMC, 2018 | [x] | [x] | [x] | [x] | [ ] | [ ] |
| **ART07** | Urban Heat Stress Bangkok | [x] | [x] | [x] | [x] | [ ] | [ ] |
| **ART08** | Griffith Univ / GIZ, 2018 | [x] | [x] | [x] | [x] | [ ] | [ ] |
| **ART09** | J Flood Risk Manag, 2024 | [x] | [x] | [x] | [x] | [ ] | [ ] |
| **ART10** | WIM ExCom Sea Level Rise | [x] | [x] | [x] | [x] | [ ] | [ ] |

---

## 🗃️ Appendix: 01_Raw_Extraction.md Structure (Option A)

Each `01_Raw_Extraction.md` file must follow this exact Markdown structure containing a single, parsable JSON code block:

# Raw Extraction: [Article Folder Name]
- **Source**: [Exact Source Filename.pdf]
- **Date Extracted**: [Timestamp]

```json
{
  "metadata": {
    "source_filename": "[Exact Source Filename.pdf]",
    "extracted_at": "[Timestamp]",
    "notebook_id": "crdb-tor-5-5-climate-risk-arti"
  },
  "core_hypothesis": "[Core scientific hypothesis in one sentence]",
  "sections_outline": [
    "[Section Outline List]"
  ],
  "tables_and_figures": [
    {
      "id": "[Table/Figure ID, e.g., Table 1]",
      "title": "[Title of table/figure]",
      "focus": "[Brief summary of variables/data shown]"
    }
  ],
  "extracted_evidence": [
    {
      "evidence_id": "E01",
      "topic": "[e.g., Rice Yield Sensitivity under SSP5-8.5]",
      "description": "[Qualitative concept or trend extracted]",
      "metrics_mentioned": "[Explicit numbers or ranges, if any]",
      "citations": "[Exact section name, page number, or table/figure reference]"
    }
  ],
  "limitations_and_uncertainties": [
    {
      "issue": "[Warning, model limitation, or source data uncertainty]",
      "citation": "[Location in paper]"
    }
  ]
}
```

---
*Created based on: [AI_Agent_Workflow_Guide-Climate Change in Thailand Project.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/AI_Agent_Workflow_Guide-Climate%20Change%20in%20Thailand%20Project.md)*
