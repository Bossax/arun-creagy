---
title: NotebookLM Phase 1 extraction is most reliable when orchestration separates the 
tags: [notebooklm, timeouts, phase1-extraction, atomic-queries, packet-workflow, raw-copy, synthesis, traceability]
created: 2026-06-23
source: Session reflection from ψ/inbox/2026-06-23_notebooklm-phase1-error-handling-workflow.md
project: github.com/sitth/arun_creagy
---

# NotebookLM Phase 1 extraction is most reliable when orchestration separates the 

NotebookLM Phase 1 extraction is most reliable when orchestration separates the unit of prompting from the unit of delegation: each NotebookLM prompt should remain atomic (one information target only), but one subtask may run an ordered packet of atomic queries in a single fresh session and append all raw outputs into `raw-copy.md` before a separate synthesis pass builds `01_Raw_Extraction.md`.

Timeout handling rule: if NotebookLM MCP times out, assume the query was likely sent, do not immediately retry, record the timeout in `raw-copy.md`, let the human paste the returned content manually, and synthesize only from content explicitly present in the raw artifact. Unsupported schema fields must remain empty rather than inferred.

Operational rules established in this session:
- resolve exact paper titles from `TOR5.5_Articles_Summary_Table.md`
- use one fresh NotebookLM session per query-runner packet
- prefer high typing speed when supported
- close the session after the packet completes
- preserve failed early raw artifacts for audit traceability

---
*Added via Oracle Learn*
