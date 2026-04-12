---
title: Oracle DB Phase 2.2 — oracle-framework & skills-governance learning backfill
tags: [oracle-db, oracle-framework, skills-governance, mcp, vector-search, fts, oracle-skills, hybrid-shell]
created: 2026-04-11
source: Oracle Learn via Arun_Creagy canonical; source_file=ψ/memory/learnings/2026-04-11_oracle-db-phase2.2-oracle-framework-and-skills-governance-backfill.md
---

# Oracle DB Phase 2.2 — oracle-framework & skills-governance learning backfill

Oracle DB Phase 2.2 — oracle-framework & skills-governance learning backfill

Source file: ψ/memory/learnings/2026-04-11_oracle-db-phase2.2-oracle-framework-and-skills-governance-backfill.md
Type: learning
Scope: Oracle DB backfill – Phase 2.2 batch of oracle-framework and skills-governance patterns, distilled from existing learnings and aligned with the Group 6–7 canonicalisation pattern.

Stable patterns captured:
1) Treat FTS as the baseline and design around vector-search fragility — Oracle MCP may temporarily report vector search unavailable while FTS remains healthy; design skills and backfill selections so they never depend on semantic/vector search for correctness, lean on strong filenames, tags, and concepts, and treat vector search as an optimisation.
2) Run Oracle MCP inside the same container/runtime as the HTTP engine — run the Oracle MCP entrypoint in the same Bun Docker container as the HTTP engine, sharing runtime, /vault path mapping, and SQLite/vector index files; treat .roo/mcp.json as code with explicit wiring to docker-compose.
3) Separate family skills from project-local Roo skills — distinguish agent/family skills installed by oracle-skills-cli under ~/.claude and ~/.codex from Roo/project skills under ~/.roo and .roo, and treat oracle-skills updates as affecting only the family layer; use patch-carrying fork + sync-branch workflow instead of force pushes.
4) Keep ~/.roo/skills as a patch-carrying fork via sync branches — manage installed skills as a git repo with origin (fork) and upstream (mother-oracle), creating sync/<tag> branches per release and merging via PR to preserve local fixes.
5) Align shell and skills version layers in hybrid environments — adopt Git Bash as primary shell with POSIX commands and forward-slash paths; recognise distinct version layers (CLI binary vs installed bundles); verify installed skills vs PATH; restart agents after updates and treat /awaken as a continuity audit.

Open questions include stabilising the Chroma/vector backend and defining helper scripts for oracle_stats() health checks.

This is the Phase 2.2 oracle-framework batch canonical learning for wiring and skills-governance patterns in Oracle DB backfill.

---
*Added via Oracle Learn*
