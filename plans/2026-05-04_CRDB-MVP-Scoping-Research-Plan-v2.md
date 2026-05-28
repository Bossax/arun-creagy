# Research Plan: CRDB MVP Technical Scoping  Multi-Pass Benchmarking (v2.6)

**Objective**: Ground the 4 MVPs in reality by finding "Real-World Relatives" using a multi-pass search strategy. Track **Confidence Scores** to ensure "Dummy" designs are empirical.

---

## 1. Multi-Pass Methodology & Toolchain

### Step 1: Discovery (Pass 1)
*   **Tool**: `mcp_perplexity_perplexity_ask` & `google_web_search`
*   **Action**: Identify 3-5 existing platforms/services for each MVP relative.
*   **Keywords**: *e.g., "National climate adaptation portal local planning", "Disaster impact reporting database", "Authoritative climate data catalog".*

### Step 2: Technical & UI Audit (Pass 2)
*   **Tool**: `google_web_search` (with specific URL targets from Pass 1)
*   **Action**: Extract design patterns: How do they handle resolution (Level 1 vs 2), uncertainty, and "Decision Commitment"?

### Step 3: Keyword Refinement & Iteration (Pass 3)
*   **Action**: If results are thin, pivot terms (e.g., from "Portal" to "Decision Support System") and re-run Step 1.
	In addition, use `mcp_perplexity_perplexity_ask` if the results are thin
 

---

## 2. Benchmarking Targets

### MVP-1 (The Exporter)
*   **Focus**: Portals bridging regional narrative vs. local action.
*   **Relative**: Climate-ADAPT, UKCP, Australia Climate Change in Australia.

### MVP-2 (The Intake)
*   **Focus**: Quality flags and triage workflows for impact data.
*   **Relative**: DesInventar, Sendai Framework Monitor.

### MVP-3 (The Catalog)
*   **Focus**: Presentation of "Official/Endorsed" status.
*   **Relative**: Copernicus Data Store, NOAA Catalog.

### MVP-4 (The Interpreter)
*   **Focus**: UX patterns for "Readiness" vs. "Uncertainty".
*   **Relative**: IPCC/Copernicus Uncertainty Guidance. and other climate communication guidance

---

## 3. Reporting: The Confidence Score
After each turn, report confidence (1-5):
*   **1 (Hallucinated)**: No real-world relative found.
*   **5 (Empirically Anchored)**: Clear real-world patterns identified.

---

## 4. Execution Sequence
1.  **Turn 1 (Pass 1 - MVP-1 & MVP-3)**: Discovery of Portals and Catalogs.
2.  **Turn 2 (Pass 1 - MVP-2 & MVP-4)**: Discovery of L&D Intake and Uncertainty UX.
3.  **Turn 3 (Audit & Iteration)**: Deep dive into UI/Logic patterns.
4.  **Turn 4 (Synthesis)**: Build "Grounded Dummies" and report final scores.

---
*Plan restored with explicit Tool Directives.*
