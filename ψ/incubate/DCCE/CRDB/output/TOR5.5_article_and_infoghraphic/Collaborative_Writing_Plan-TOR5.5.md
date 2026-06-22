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
4. `ART04_Dengue_Early_Warning/` - Severe dengue spatial patterns & drivers (PMC, 2019)
5. `ART05_Coastal_Erosion_Southern/` - Hard vs. soft defense structures (PMC, 2022)
6. `ART06_Species_Protected_Areas/` - Wildlife & plant climate migration (PMC, 2018)
7. `ART07_Coral_Reef_Closures/` - Coral bleaching & tourism closures (Reef Resilience, 2020)
8. `ART08_Tourism_Risk_GIZ/` - Tourism sector risk assessment (Griffith Univ / GIZ, 2018)
9. `ART09_BMR_UrbanSprawl_Floods/` - Sprawl vs. rainfall flood risk in BMR (J Flood Risk Manag, 2024)
10. `ART10_Industrial_Damage_Curves/` - Depth-damage industrial flood vulnerability (Int J Disaster Risk Reduct, 2025)

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
3.  **Linguistic Extraction**: The AI compares the draft and edited files. The **`style-capture`** engine performs a semantic diff to extract:
    *   **Preferred Lexicon**: Words you replaced (e.g., mapping generic verbs to precise strategic terms).
    *   **Linguistic DNA**: Your preferred sentence lengths, hedging habits, and transitions.
    *   **Anti-AI Shield**: Explicit expressions or layouts to avoid.
4.  **Propagation**: The updated rules are written to the master Style-Pack, which I load at the start of drafting the next article.

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
| **ART04** | PMC, 2019 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART05** | PMC, 2022 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART06** | PMC, 2018 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART07** | Reef Resilience, 2020 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART08** | Griffith Univ / GIZ, 2018 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART09** | J Flood Risk Manag, 2024 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **ART10** | Int J Disaster Risk Reduct, 2025 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---
*Created based on: [AI_Agent_Workflow_Guide-Climate Change in Thailand Project.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/AI_Agent_Workflow_Guide-Climate%20Change%20in%20Thailand%20Project.md)*
