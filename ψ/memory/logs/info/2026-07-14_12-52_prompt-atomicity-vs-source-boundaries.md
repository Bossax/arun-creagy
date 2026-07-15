---
date: 2026-07-14T12:52:00+07:00
type: info
status: raw
significance: important
---

# Prompt Atomicity vs. Source Boundaries in NotebookLM

During the initialization of the GGGI NAP AP project framework study, we refined a critical process learning regarding NotebookLM prompt engineering under the `/notebooklm-rules` skill:

1. **Atomicity is Conceptual, Not Source-Based**: The rule of atomicity (focusing on a single target concept to prevent the model from synthesizing or "thinking") applies to the query prompt itself, not the physical source file. 
2. **The Multiple Query Requirement**: A large source PDF (such as a national policy plan or system design report) contains multiple disjoint layers (approach, structure, database schema, data collection flows). To extract these layers without forcing the model to perform compound logic, we must run multiple distinct, single-purpose micro-queries against the same source, rather than a single compound query.
3. **Synthesis is Exclusively Local**: All comparison, gap mapping, and consolidation of these extracted puzzle pieces must be done locally in the repository files after the raw, uncorrupted results are saved to the audit log (`notebooklm_runs/`).

Logged via /fyi
