# Operational Plan: NCAIF Forensic Service Enrichment & Gap Analysis (v2.0)

**Objective**: Synthesize 32 granular agency demands into 7 contextualized Climate Services, ensuring strict institutional traceability and preventing technical sanitization.
**Location**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Service_Enrichment_Orchestration_Plan_v2.0.md`
**Version**: 2.0 (Forensic Correction Revision)

---

## 1. Methodological Flaws Addressed (Anti-Sanitization Rules)
This v2.0 plan introduces strict guardrails to prevent the methodological flaws identified in v1.0:
*   **Preventing "Source Skimming"**: Sub-agents are restricted to a strict **Source Manifest** of raw workshop data. Reading high-level summaries is prohibited during extraction.
*   **Preventing "Institutional Erasure"**: Agencies that coined foundational concepts (e.g., UDDC for "Single Source of Truth") must remain anchored to those foundational services (Service 01), rather than being pushed into downstream analytics silos.
*   **Preventing "Generic IT Specs"**: Every technical module must retain its institutional "Why" (the specific pain point, such as "Fear of Liability" or "OAG Audit") alongside its "How" (the hard data specs).
*   **Enforcing "Originator Tags"**: Every synthesized requirement must carry a strict lineage tag: `[Agency] - [Decision Moment] - [Source File]`.

---

## 2. The Source Manifest (Strict Whitelist)
Sub-agents MUST extract requirements ONLY from the following raw files:
1.  `ψ/incubate/DCCE/CRDB/output/consultation_workshop/user_use_case_raw.md` (Primary source for explicit agency demands and pain points).
2.  `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md` (Primary source for normalized mapping and newly discovered use cases).
3.  `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_raw_extraction.md` (Backup for granular workshop transcript context).

---

## 3. Orchestration Architecture (3-Phase Forensic Workflow)

### Phase 1: High-Fidelity Raw Extraction
*   **Agent**: `codebase_investigator`
*   **Operational Detail**: Extract the 32 use cases from the Source Manifest. For each use case, extract:
    1.  **Originating Agencies**: (List ALL agencies requesting this, do not limit to 1).
    2.  **Institutional Pain Point**: (Why do they need this? What is the fear/blocker?)
    3.  **Hard Technical Specs**: (Resolutions, return periods, latencies).
    4.  **Originator Tag**: (Strict citation of where this was found).
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Traceable_Dependencies.json`

### Phase 2: Context-Preserving Synthesis & Grounded Expansion
*   **Agent**: `generalist` (with Google/Brave Search access)
*   **Operational Detail**: Blend the JSON inventory into the 7 Services and expand technical depth where stakeholder inputs are underspecified.
    *   **Rule A**: Service 01 (Authoritative Discovery / SSOT) MUST be treated as a foundational layer. Any agency that demanded "authoritative data", "certified data", or "SSOT" (like UDDC) MUST be mapped to Service 01's common core.
    *   **Rule B**: Build "Contextual Modules" for specific edge cases (e.g., Sinkholes for DMR, Accumulated Funds for DLA), attaching the `[Originator Tag]` to each module.
    *   **Rule C (Grounded Expansion)**: If a stakeholder requirement lacks technical parameters (e.g., "We need an ROI model" but no specific variables), the agent MUST use web search to find standard industry benchmarks (e.g., "World Bank ROI for Coastal Adaptation").
    *   **Rule D (Explicit Citation)**: Online sources used for expansion MUST be explicitly labeled as `[Technical Enrichment: Source URL]` to clearly distinguish them from the `[Stakeholder Grounding: Source File]`. This ensures the design is complete but never "floating in the air".
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Enriched_Service_Specs_v2.0.md`

### Phase 3: Triple-Audit Gap Analysis
*   **Agent**: `codebase_investigator`
*   **Operational Detail**: Perform the Data, Legal, and Technical readiness scoring (1-5) against the new v2.0 specs. Identify the specific "Blocker of the Week" for each service.
*   **Handoff Artifact**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Readiness_Report_v2.0.md`

---

## 4. Execution Protocol
No phase may begin until the Human validates the Handoff Artifact of the previous phase. 

*Status: Awaiting Human approval to initiate Phase 1.*