# Research Plan: CRDB MVP Scoping — Multi-Path Alternatives (v3)

**Objective**: Resolve technical ambiguities and design **two alternative "dummy" versions** for each MVP to account for potential context drift and data availability constraints in Thailand.

---

## 1. Design Philosophy: The Two Paths
For each MVP, research will focus on defining:
*   **Path A: The Full-Service/High-Fidelity Model**: Based on international benchmarks (Norway/Copernicus). Assumes high-resolution data and automated pipelines.
*   **Path B: The Proxy/Low-Fidelity Model**: Designed for current Thai data constraints. Assumes manual verification, coarse resolution, and "Expert Opinion" as a bridge.

---

## 2. Scoping Targets & Key Questions

### MVP-1 (Policy Briefing)
*   **Path A (Climate Allowance)**: Norway benchmark. Engineering safety margins (e.g., +20% rainfall for drainage design). Requires local downscaling.
*   **Path B (Risk Narrative)**: Qualitative trends + sector vulnerability "Rule of Thumb." Uses available regional indices to tell a "Risk Story" without precise engineering decimals.

### MVP-2 (L&D Pipeline)
*   **Path A (Automated Impact Schema)**: Real-time geocoded assets vs. hazard. Automated economic damage calculation.
*   **Path B (Manual Validation/Quarantine)**: Spreadsheet-based intake with "Reliability Flags." Focuses on auditing the *process* of data entry from sectors before it’s geocoded.

### MVP-4 (Uncertainty Data Shield)
*   **Path A (Statistical Confidence Labels)**: Based on model spread and standard deviation (Copernicus-style).
*   **Path B (Decision Readiness Status)**: Simple "Traffic Light" system (Red: Speculative, Green: Officially Endorsed for Budgeting).

---

## 3. Methodology & Toolchain

### Step 1: Internal Project Context (NotebookLM)
*   **Tool**: `mcp_notebooklm_ask_question`
*   **Action**: 
    *   Query `climate-service-1` for Norway's technical details (Path A) vs. any mentions of "Proxy Data" or "Expert Judgment" (Path B).
    *   Query `climate-service-design-worksho` for stakeholder "skepticism" signals that justify the need for Path B.

### Step 2: Global Best Practices & Benchmarking (Web Search)
*   **Tool**: `mcp_perplexity_perplexity_research`
*   **Action**:
    *   **Research**: "Climate services in data-poor environments: Using proxies and expert elicitation."
    *   **Research**: "Standardized Loss and Damage indicators for developing countries vs. high-resolution models."
    *   **Search**: Examples of "Confidence/Uncertainty Labels" for non-expert government planners.

### Step 3: Synthesis — The "Alternative Spec"
*   **Tool**: `write_file`
*   **Output**: A document presenting **Option 1 (Full)** vs. **Option 2 (Proxy)** for each MVP, including the "Logic" and "Visual" for each path.

---

## 4. Execution Sequence
1.  **Turn 1 (NotebookLM)**: Extract Norway details (Path A) vs. Proxy patterns (Path B).
2.  **Turn 2 (Perplexity)**: Deep research on data-poor climate service alternatives.
3.  **Turn 3 (Synthesis)**: Draft the final "Alternative Dummy" artifacts.

---
*Plan updated to account for Context Drift.*
