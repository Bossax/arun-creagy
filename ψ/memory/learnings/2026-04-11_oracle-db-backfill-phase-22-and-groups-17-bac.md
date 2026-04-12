---
title: Oracle DB backfill – phase 2.2 and groups 1–7: backfill should flow from filesys
tags: [oracle-db, backfill, canonicalisation, workflow, indexing-map, mcp, rrr]
created: 2026-04-11
source: ψ/memory/learnings/2026-04-11_rrr_oracle-db-backfill-phase2.2-and-groups1-7.md
---

# Oracle DB backfill – phase 2.2 and groups 1–7: backfill should flow from filesys

Oracle DB backfill – phase 2.2 and groups 1–7: backfill should flow from filesystem canonicals grouped via an indexing map, into a backfill index table, and then into Oracle DB via the arra_learn MCP tool. Canonical notes describe scope, member artefacts, stable patterns vs one-offs, and their relationship to Oracle DB; the backfill index records date, source type, canonical path, Oracle ID, concepts, and notes. Large Markdown tables are edited via a dedicated helper, not by hand, and Oracle DB writes should always go through the configured MCP tools rather than ad hoc HTTP calls.

---
*Added via Oracle Learn*
