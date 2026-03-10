# plan — DCCE / CRDB

Operational plan for **CRDB-only** scope in this thread (do not touch CRI/BTR).

Anchors:
- Digest (onboarding): [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md)
- Decision log (confirmed): [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md)
- MVP/workflow patterns (current): [`ψ/incubate/DCCE/CRDB/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)

## Objectives

1) Lock Phase 1 scope as **conceptual + logical architecture** (not a software build).
2) Publish a coherent **NCAIF (EDM)** narrative: taxonomy + glossary + workflow entry points.
3) Convert workflow patterns into a **Phase 1 MVP shortlist** with explicit “what ships” vs “documentation-only.”
4) Define **governance rails + minimum gates (G1–G5)** required for safe publishing and baseline endorsement.
5) Produce a small set of **immediately usable artifacts** (schemas/templates/checklists) that enable execution.

## Decisions

Confirmed decisions — user confirmation **2026-03-10 14:03 ICT (07:03Z)**. See [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md)

- MVP priority: **MVP-3** + **MVP-2** as Phase 1 core; keep MVP-1/MVP-4 lightweight.
- Sitemap: **Option 3 (Hybrid / workflow-pattern-first)**.
- Architecture: **Catalog-first (link-first)**.
- Rails: **Open → data.go.th; Non-open → GDX; Sensitive → internal-only**.
- Governance gates: **G1–G5** (classification; metadata+preview; endorsement registry; boundary+crosswalk; event schema with timeliness/flags).

Confirmed assumptions (Phase 1, locked)

These were previously tracked as “open confirmations”; they are now **confirmed** and should be treated as Phase 1 design constraints.

1) **MVP core**: Phase 1 core is **MVP-3 Recommended Baseline Registry** + **MVP-2 Disaster data ingestion + Loss & Damage groundwork**; keep **MVP-1/MVP-4** as documentation-lite deliverables.
2) **Sitemap stance**: **Option 3 (Hybrid / workflow-pattern-first)**.
3) **Architecture stance**: **Catalog-first (link-first)**.
4) **Publishing rails**: **Open → data.go.th; Non-open → GDX; Sensitive → internal-only**.
5) **Canonical boundary pattern**: primary reporting uses **administrative boundaries**; budget/operations use **LAO/municipality**; small-area baselines use **EA where available**; publish and govern **crosswalks** explicitly.
6) **Endorsement authority pattern**: **interim endorsement panel** (DCCE central data team + source-agency focal point, co-signature) for recommended baselines.
7) **MVP-2 scope**: Phase 1 is **groundwork** (manual/batch intake + quarantine/validation flags + revision policy), not a fully automated pipeline.

## Outputs (what we will produce next)

Phase 1 “ship list” (minimal, high-leverage):

- **Baseline Registry schema** (MVP-3): required fields + versioning + endorsement audit trail.
- **Publishing rails checklist** (Open/GDX/Internal) + minimum metadata/preview requirements.
- **Boundary + crosswalk governance note**: canonical boundary per flagship output + ownership + versioning.
- **Disaster intake + quarantine template** (MVP-2 groundwork): event registry + impact observation template + validation flags + revision policy.
- **Briefing pack templates** (MVP-1 lite): 3–5 export-first templates + “must include” checklist.
- **Uncertainty/publishing standard** (MVP-4 lite): minimum statements + misuse example + tiered guidance.

## Next steps

1) Draft Baseline Registry schema (start with a single markdown table; evolve later).
2) Draft boundary/crosswalk governance note (one page) + identify owner(s).
3) Draft DDPM disaster intake template + validation flag set (groundwork only).
4) Add “governance gates” checklist that each published artifact must pass.
