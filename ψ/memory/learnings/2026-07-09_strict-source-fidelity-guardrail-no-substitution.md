---
id: learning_2026-07-09_strict-source-fidelity-guardrail-no-substitution
type: learning
title: Strict Source-Fidelity Guardrail: No Substitution on Tool Failure
concepts: [RAG-safety, source-fidelity, tool-failure-policy, hallucination-prevention]
tags: [RAG-safety, source-fidelity, tool-failure-policy, hallucination-prevention]
created: 2026-07-09
indexed_at: 2026-07-09T04:58:06.321Z
updated_at: 2026-07-09T04:58:06.321Z
hash: sha256:c458d0886f7e6b750d59bf2d5ce895d17e63f448ee37597d4b4a59ac8c16e91b
source: User correction on NotebookLM query fallback
project: github.com/bossax/arun_creagy
arra_id: learning_2026-07-09_strict-source-fidelity-guardrail-no-substitution
arra_type: learning
arra_concepts: [RAG-safety, source-fidelity, tool-failure-policy, hallucination-prevention]
arra_created: 2026-07-09T04:58:06.321Z
---

# Strict Source-Fidelity Guardrail: No Substitution on Tool Failure

Strict Source-Fidelity Guardrail: No Substitution on Tool Failure
Pattern: When an agent is instructed to query a specific external RAG or knowledge tool (such as NotebookLM) to gather information, and that tool fails, times out, or encounters authentication issues, the agent MUST immediately stop, report the error, and troubleshoot the tool. Under no circumstances is the agent allowed to bypass the tool by falling back to other local repository files or external sources to simulate a successful query. Doing so violates source-fidelity and introduces the risk of hallucinated or out-of-date information.

---
*Added via Oracle Learn*
