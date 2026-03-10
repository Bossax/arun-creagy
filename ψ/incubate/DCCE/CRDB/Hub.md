# Hub — DCCE / CRDB

## Goal
- Deliver **CRDB Phase 1 conceptual + logical architecture** (not a software build) for Thailand’s climate adaptation data ecosystem.
- Define **NCAIF as the Enterprise Data Model (EDM)** (taxonomy + glossary + logical blueprint) and connect it to **workflow patterns → MVPs**.
- Establish **governance rails** and the **minimum gates** needed to publish and recommend baselines safely.

## Current status
- Scope guard: **CRDB only** in this thread (do **not** touch CRI/BTR).
- CRDB onboarding pack + Phase 1 decision log have been triaged into CRDB incubate inbox.

## Key docs
- Plan: [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)
- Knowledge digest (onboarding): [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md)
- Phase 1 decision log (confirmed): [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md)
- MVP/workflow anchor (current): [`ψ/incubate/DCCE/CRDB/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)
- Governance rails (v3): [`ψ/incubate/DCCE/CRDB/Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/incubate/DCCE/CRDB/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md)
- CDM anchor: [`ψ/incubate/DCCE/CRDB/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md)
- Assets: [`ψ/incubate/DCCE/CRDB/assets/`](ψ/incubate/DCCE/CRDB/assets/)

## Scope + roles (operating model)

- CRDB role: **Architect/Librarian** — catalog + governance + conceptual/logical modeling (link-first, not re-host-first).
- ADPC role (dependency interface): **Builder/Curator** for UNDP-BTR Task 2 risk platform + visualization (physical implementation elsewhere).
- DGA alignment: publish via rails (Open → data.go.th; non-open → GDX; sensitive → internal), avoid redundant infrastructure.

## Deliverables (migrated)
- **NCAIF (EDM)**: taxonomy + glossary + sitemap stance; connects user needs to data products.
- **Workflow patterns (P1–P4) + MVP shortlist** (Phase 1) with tiering (Tier 1 export-first vs Tier 2 advanced).
- **Governance rails + Phase 1 minimum gates (G1–G5)** for safe publishing and endorsement.
- **CDM (IVRA-first)** with explicit handling of drivers vs events, attribution links, and vulnerability strategy pattern.

## MVP decisions (confirmed stance)

Anchor: [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md)

- Phase 1 core: **MVP-3 Recommended Baseline Registry** + **MVP-2 Disaster data ingestion + Loss & Damage groundwork**.
- Keep **MVP-1** (briefing pack templates) and **MVP-4** (uncertainty/publishing standard) as **lightweight documentation + templates** to avoid scope creep.
- Sitemap stance: **Option 3 (Hybrid / workflow-pattern-first)** (confirmed).
- Architecture stance: **Catalog-first (link-first)** (confirmed).
- Confirmation note: user confirmed Phase 1 decisions on **2026-03-10 14:03 ICT (07:03Z)**.

## Inbox triage pointers
- Active triage queue (moved): [`ψ/incubate/DCCE/CRDB/inbox/active/`](ψ/incubate/DCCE/CRDB/inbox/active/)
- Writing-notes triage queue (moved): [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/)

## Immediate priorities (next 1–2 sessions)

1) Draft **Recommended Baseline Registry** schema (owner, purpose, scale, limitations, versioning, access path).
2) Define **canonical boundary + crosswalk governance** (ownership, versioning, publishing rules).
3) Define minimal **metadata + preview** template and publishing gate checklist.
