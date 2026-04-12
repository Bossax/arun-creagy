---
title: Oracle DB backfill — Group 1 `oracle_learn` materialisation guardrail.
tags: [oracle-db, oracle_learn, guardrail, durable-capture, workflow-integrity, backfill]
created: 2026-04-11
source: canonical backfill: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group1-oraclelearn-materialisation-guardrail.md
---

# Oracle DB backfill — Group 1 `oracle_learn` materialisation guardrail.

Oracle DB backfill — Group 1 `oracle_learn` materialisation guardrail.

After every `oracle_learn()` call, treat the returned file/source_file path as a claim that must be verified; immediately check that the learning markdown exists under the vault, materialise it if missing, and log any ENOENT as a serious workflow integrity failure so Oracle DB and the Git filesystem stay aligned.

---
*Added via Oracle Learn*
