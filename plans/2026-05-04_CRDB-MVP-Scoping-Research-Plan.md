# Research Plan: CRDB MVP Technical Scoping & "Dummy" Design

**Objective**: Resolve scope ambiguities and design "dummy" content for the 4 MVPs to ensure a coherent, confusion-free workshop presentation.

## 1. Lingering Questions & Scoping Targets
*   **MVP-1 (Policy Briefing)**: 
    *   *Granularity*: Is it Provincial or Municipality level?
    *   *Content*: Does it include "Climate Allowance" (safety factors/engineering margins) or just hazard exposure?
*   **MVP-2 (L&D Pipeline)**: 
    *   *Scope*: How to design a "Sector-Agnostic" intake that serves Health, Agriculture, and Transport, not just DDPM?
*   **MVP-4 (Uncertainty Shield)**: 
    *   *Form Factor*: Is it a pop-up, a watermark, a mandatory "Checklist for Interpretation," or a "Data Sensitivity Label"?

---

## 2. Methodology & MCP Tool Usage

### Step 1: Benchmark Extraction (NotebookLM)
*   **Tool**: `mcp_notebooklm_ask_question`
*   **Target**: 
    *   `climate-service-1`: Extract the "Climate Allowance" (Norway) concept details—how is it calculated and presented to planners?
    *   `climate-service-design-worksho`: Look for "Sectoral L&D" frameworks and "Uncertainty Communication" best practices for local planners.

### Step 2: Local Requirement Synthesis (Oracle & Filesystem)
*   **Tool**: `grep_search` / `read_file`
*   **Target**:
    *   ~~Analyze `ψ/inbox/The current framing of CRDB project...` for specific mentions of municipality vs. province needs.~~ %% waste of time. it is not in this summary %%
    *   Search `ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md` for sectoral L&D signals (Health/Agri).

### Step 3: "Dummy" Artifact Drafting
*   **Tool**: `write_file`
*   **Output**: A "Mock-up" document for each MVP containing:
    1.  **Mock UI/Output**: A Markdown-based visualization of what the user sees.
    2.  **Step-by-Step Logic**: The internal "Rules" the system follows to generate that output.
    3.  **Boundary Stance**: Definitive statement on granularity.

---

## 3. Execution Schedule
1.  **Turn 1**: Extract "Climate Allowance" logic and "Uncertainty Shield" templates from NotebookLM.
2.  **Turn 2**: Review local use cases for Municipality vs. Province priority and Sectoral L&D triggers.
3.  **Turn 3**: Synthesize into a "Dummy MVP Spec" document for the workshop.

---
*Plan initiated by ARUN.*
