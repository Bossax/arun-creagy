# NCAIF Service-Level Data Gap Analysis: Execution Plan

## 1. Objective
Elevate the Data Gap Analysis from a transactional Use Case mapping (40 UCs) to a structural Service Platform evaluation (8 Platforms). The goal is to identify systemic bottlenecks where foundational datasets fail to meet rigid target service requirements, ultimately producing high-level, actionable policy recommendations for the National Climate Committee.

## 2. Methodological Framework
The analysis will be driven by three core concepts:
1.  **Data Primitives:** Defining the non-negotiable foundational data units required for each Service Platform to function.
2.  **Service Dependency Matrix:** Mapping how failures in foundational platforms (e.g., S01) cascade and block application-level platforms (e.g., S02, S05, S06).
3.  **5-Dimension Gap Typology:** Classifying gaps not just as "missing data," but diagnosing the structural cause:
    *   *Translational/Analytical* (Needs scientific conversion)
    *   *Granularity/Resolution* (Needs spatial/demographic downscaling)
    *   *Temporal/Telemetry* (Needs real-time API integration)
    *   *Institutional/Legal* (Needs regulatory unlocking, e.g., PDPA)
    *   *Authoritative/Certification* (Needs official state mandate/seal)

## 3. Operational Execution Steps & Tool Allocation

### Phase 1: Abstraction of Data Primitives
**Goal:** Translate the 40 Use Case requirements into rigid "Data Primitives" for the 8 Service Platforms.
*   **Step 1.1:** Parse the `NCAIF_Use_Case_Inventory_v2.0.csv` and `NCAIF_Full_Readiness_Matrix_v1.0.csv`.
*   **Step 1.2:** Abstract the demands into non-negotiable primitives per platform (e.g., S01 = Baseline + Scenarios; S02 = S01 + Asset Exposure + Vulnerability).
*   **Tooling/Agents:**
    *   `read_file` to ingest the matrices.
    *   `invoke_agent` (`generalist` sub-agent) to perform the semantic abstraction and grouping of 40 UCs into 8 Service Primitives, outputting a structured JSON or Markdown list.

### Phase 2: Foundation vs. Target Mapping (The Pillar 3 Assessment)
**Goal:** Evaluate the 260 datasets in `Data_catalog_v3.csv` against the defined Service Primitives to identify structural mismatches.
*   **Step 2.1:** Categorize the 260 datasets into "Foundational" (Broad, base layers) vs. "Application-specific" (Sectoral, niche).
*   **Step 2.2:** Map the categorized supply against the rigid Service Primitives from Phase 1.
*   **Tooling/Agents:**
    *   `run_shell_command` using PowerShell/Python (pandas) to programmatically filter, categorize, and cross-reference the `Data_catalog_v3.csv` against keywords derived in Phase 1. This handles the large data volume efficiently.

### Phase 3: Dimensional Gap Typology Evaluation
**Goal:** Classify the mismatches identified in Phase 2 using the 5-Dimension Gap Typology.
*   **Step 3.1:** For each missing primitive, determine *why* it fails (e.g., is it a Translational issue like IDF curves, or an Institutional issue like household census data?).
*   **Step 3.2:** Research existing Thai institutional precedents or similar barriers within the project context to ensure grounded analysis.
*   **Tooling/Agents:**
    *   `invoke_agent` (`generalist`) to apply the logical typology framework to the mapped data.
    *   `mcp_oracle-v2_arra_search` and `mcp_oracle-v2_arra_read` to query the Oracle vault for existing knowledge on Thai data governance, PDPA precedents, or inter-agency data sharing agreements (e.g., searching for "PDPA", "TMD", "GISTDA").
    * if no useful information return, resort to google and brave web search
    * if still not useful, use perplexity ask

### Phase 4: Synthesis & Policy Formulation
**Goal:** Author the final Thai Institutional Report detailing the Service-Level Gaps and actionable policy recommendations.
*   **Step 4.1:** Synthesize the findings into the institutional structure (Purpose-First phrasing, In-line Justification).
*   **Step 4.2:** Draft policy recommendations targeting the structural root causes (e.g., mandating an Authoritative Seal, establishing an anonymization pipeline for spatial risk).
*   **Tooling/Agents:**
    *   `activate_skill` (`writing-th`) to load the Thai report writing memory and `STYLE_PACK_NCAIF-Institutional.md` alignment.
* 
    *   `write_file` to generate the final artifact: `รายงานนโยบายช่องว่างข้อมูลระดับบริการ_v1.0.md` (Service-Level Data Gap Policy Report).

## 4. Expected Artifacts
1.  `Service_Primitive_Requirements.json/csv` (Output of Phase 1)
2.  `Service_Dependency_Gap_Matrix.csv` (Output of Phases 2 & 3)
3.  `รายงานนโยบายช่องว่างข้อมูลระดับบริการ_v1.0.md` (Final Policy Report - Output of Phase 4)