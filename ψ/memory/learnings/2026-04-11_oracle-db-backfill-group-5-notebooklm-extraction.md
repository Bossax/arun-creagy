---
title: Oracle DB backfill — Group 5 NotebookLM extraction vs harmonisation & source-fid
tags: [oracle-db, notebooklm, extraction, harmonisation, source-fidelity, guardrails, prompt-design]
created: 2026-04-11
source: canonical backfill: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group5-notebooklm-extraction-harmonisation-guardrails.md
---

# Oracle DB backfill — Group 5 NotebookLM extraction vs harmonisation & source-fid

Oracle DB backfill — Group 5 NotebookLM extraction vs harmonisation & source-fidelity guardrails.

NotebookLM should be treated as a pure data-extraction engine with short, atomic prompts; harmonisation and schema alignment happen locally, and strict source-fidelity plus parameter-discipline guardrails (including title probes) are enforced to prevent over-synthesis or leakage beyond in-scope sources.

---
*Added via Oracle Learn*
