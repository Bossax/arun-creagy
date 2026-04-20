# Mandate: The Oracle Workflow (EPIV)

This mandate defines the execution loop for all tasks, prioritizing analytical rigor and inquiry-driven progress.

## 1. The EPIV Loop (Researcher Edition)
1. **Explore (Audit First)**: Systematically map the codebase or data system and validate assumptions. This MUST culminate in a **Baseline Audit**, documenting existing structures, lineage, and constraints (e.g., Administrative Gaps) before proposing new actions.
2. **Plan (Inquiry-First)**: Define a strategy framed as a sequence of **Research Questions** and specific **Verification Strategies**. Avoid premature commitment to specific models or activities until empirical validation is achieved.
3. **Implement (Targeted)**: Apply targeted and idiomatic changes strictly based on the verified hypotheses from the Plan phase.
4. **Verify (Empirical)**: Provide empirical evidence (tests, logs, or statistical correlations) of success and structural integrity.

## 2. Decision Protocol
- **Directives**: Clear requests for action. Implement autonomously after a Baseline Audit and Inquiry-First Planning.
- **Inquiries**: Requests for analysis. Provide findings and limitation profiling without modifying files.
- **Ambiguity**: Seek clarification before proceeding.

## 3. The Verification Rule
A task is considered complete only when behavioral correctness and statistical significance (where applicable) have been demonstrated through a verifiable shell command or log.
