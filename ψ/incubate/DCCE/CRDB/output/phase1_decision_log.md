# DCCE_CRDB — Phase 1 Decision Log (Confirmed)

## Purpose
Capture **Phase 1 decisions** (MVPs, sitemap, governance gates) with recommended choices, rationale, and anchors.

Confirmation: user confirmed Phase 1 decisions on **2026-03-10 14:03 ICT (07:03Z)**.

## Inputs (anchors)
- [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:24)
- [`National Climate Adaptation Information Framework.md`](ψ/writing/2025-11_DCCE-CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md:36)
- [`NCAIF — Workflow patterns + MVP v3.md`](ψ/writing/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md:1)
- [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/writing/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md:82)
- [`NCAIF_Use_Cases.md`](ψ/writing/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:40)
- [`FGD2_Slide_Deck_Guide.md`](ψ/writing/2025-11_DCCE-CRDB/output/FGD2_Slide_Deck_Guide.md:209)

---

## Decision Log (Confirmed)

| Decision Area | Recommended Choice | Rationale | Status | Owner |
|---|---|---|---|---|
| Phase 1 MVP priority | **MVP‑3 Recommended Dataset Registry** + **MVP‑2 Disaster data ingestion + L&D groundwork** (core); **MVP‑1** as lightweight export templates; **MVP‑4** as minimal guidance | v3 frames MVP‑2 as DDPM→DCCE ingestion groundwork tied to the Loss & Damage logical model (MVD), while MVP‑3 remains catalog‑first. MVP‑1/MVP‑4 stay light to avoid scope creep. | Confirmed | DCCE lead + project team |
| Sitemap option | **Option 3: Hybrid (workflow‑pattern‑first)** | Balances a stable taxonomy with visible workflow entry points (P1–P4). Supports Tier 1 vs Tier 2 literacy stance. | Confirmed | DCCE lead |
| Catalog‑first vs host‑first | **Catalog‑first (link‑first)** | Aligns to DGA rails (data.go.th / GDX). NSO prefers linking rather than duplicating data. | Confirmed | DCCE + DGA liaison |
| Canonical boundaries | **Primary reporting:** administrative boundaries; **Budget/operations:** LAO/municipality; **Small‑area baselines:** EA where available; publish **crosswalk ownership** | Interview signals show LAO is key for budgeting, admin for national reporting. Requires explicit crosswalk governance. | Confirmed | DCCE data governance lead |
| Endorsement authority (recommended baselines) | **Interim endorsement panel**: DCCE central data team + source‑agency focal point (co‑signature) | Avoids full governance council dependency while preserving accountability. | Confirmed | DCCE central data team |
| Publishing rails | **Open → data.go.th; Non‑open → GDX; Sensitive → internal‑only** | Matches DGA guidance and avoids redundant infrastructure. | Confirmed | DCCE + DGA |
| Phase 1 governance gates | **G1–G5** (classification, metadata+preview, baseline endorsement, boundary+crosswalk, event schema with timeliness/flags) | Minimum set to ship safely and address FGD1 pain points (preview, QA/QC, staging). | Confirmed | DCCE governance lead |

---

## Resolution (Phase 1 locked)
1) Mandatory Phase 1 MVPs: **MVP‑3** + **MVP‑2**.
2) Official sitemap stance: **Option 3 (Hybrid / workflow‑pattern‑first)**.
3) Official architecture stance: **catalog‑first (link‑first)**.
4) Canonical boundary pattern: **admin** for primary reporting; **LAO/municipality** for budget/operations; **EA** where available for small‑area baselines (with explicit crosswalk governance).
5) Endorsement authority pattern: **interim endorsement panel** (DCCE central data team + source‑agency focal point, co‑signature).
6) MVP‑2 pipeline scope: **groundwork** (manual/batch ingestion + quarantine/validation flags + revision policy), not full automation in Phase 1.

---

## Notes
- If MVP‑1 or MVP‑4 are excluded from Phase 1 scope, keep them as **documentation‑only** deliverables to avoid scope creep while preserving continuity with the workflow patterns.
- MVP‑2 should be explicitly positioned as **groundwork** for DDPM data ingestion and Loss & Damage governance (not a fully automated pipeline in Phase 1).
