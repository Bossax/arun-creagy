# CRDB Final Sprint — Implementation Plan

## Context

CRDB is two weeks from handing DCCE a "requirements blueprint" package (per `99_FINAL_crdb-redirection-plan-v2.md`, sealed as D-057/D-058, T-042, CH-036). Boss reviewed v2 and agrees ~90%, with several points resolved in this session:

- A new **Item 1: Business Objective / Platform Rationale** is added ahead of the existing 8 items (renumbering them 2–9) — because Boss has had to reverse-engineer the platform's "why" from TOR language since the start, and the prioritization/recommendations work (now Items 6, 9) reads stronger if it's justified against a stated rationale instead of an inferred one.
- **Business NFRs** will NOT be scoped 1:1 with the 1–2 priority use cases that get full Functional Specs. Instead, NFR tables enrich the **9 already-identified high-signal services**: the 8 services in `02_UseCases_FunctionalSpecs/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (D-043) plus A-BTR (`2026-07-06_btr-me-reporting-pipeline-use-case`). Full Functional Specs (with sign-off, sample data, ECA discipline) stay narrow — only the 1–2 selected as build-next priority.
- **Data Contracts are cut from this project's scope entirely** — moved into Item 9 (Recommendations) as a named task for TOR70/next phase, not built by CRDB now.
- **Reference Data** (Pillar 08, `08_RefData_Matrix/`) is acknowledged as needed at inception but not buildable in the time remaining — it will be explicitly logged as a deferred-to-TOR70 item (governance housekeeping decision), not silently dropped and not fully built either.

This plan turns those decisions into an executable sprint: a workflow with dated work packages, a folder cleanup pass to support the work, a final packaging structure, and a DCCE-facing communication deck.

**Grounding used:** `99_FINAL_crdb-redirection-plan-v2.md` (Sections 1–7), `SCOPE_LEDGER.md` (5 Settled Findings, current Iteration 5 scope), `CRDB-Deliverable-Map.md` (D-001–D-058), current highest ledger IDs (T-042, E-075, CH-036, D-058), and a full folder survey of `output/`.

---

## Folder Reality Check (from survey)

- **9 pillar folders exist** (`00_Strategy_Reports` … `09_BuildingBlocks`), all flat (no subfolders except `06_LDM_LossDamage_DataModel`, which has `archive/` and `examples/`).
- **`08_RefData_Matrix`** has exactly 1 file — a technical spec, no actual reference data. Confirms Boss's "we don't have time" read.
- **`05_CDM_EARCatalog`** has version sprawl: many `Entities/Relationships/Domains` CSVs with `-v2/-v3/-edited/-final` suffixes, no clear canonical pointer.
- **`CRDB-Execution-Architecture-Index.md`** (top-level nav doc) has stale/broken links to files that have since moved into pillar folders.
- **`consultation_workshop/mvp/code/`** contains a stray Python venv — **13,533 files**, almost entirely `venv/`/`venv_clean/`. Not project content; flagged for exclusion, not deletion (needs Boss's call).
- **`final_report/`** already exists, organized by TOR clause number (5.2, 5.3, 5.4, 5.5 + appendices) — this is the natural DCCE-facing submission shape, already partially populated through 7/8.
- **`interim-report/`** and **`Interview summary notes/`** are stale/superseded (frozen since 7/5 and 3/23 respectively) — archive candidates, not touched this sprint.
- **`2026-05-18_TOR-Review/`** is the most recently active non-pillar folder (8/5) — holds the TOR70 briefing deck/analysis (D-053–055), directly feeds Item 9 (Recommendations).

---

## Work Packages

Numbering below is the **new 9-item DCCE deliverable list** (Item 1 = new). Each WP names its home folder, what changes, and a suggested day range within the 14-day window (Section 7 of the redirection plan, adjusted for the changes above).

| WP   | Item                                              | What happens                                                                                                                                                                                                                                                                                                                       | Folder                                                                            | Days           | Status |
| ---- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------- | ------ |
| WP0  | Housekeeping                                      | Retire/rewrite stale `CRDB-Execution-Architecture-Index.md`; resolve CDM's two conflicting sealed records (pick canonical, mark other superseded); log Reference Data as deferred-to-TOR70 decision; flag the stray venv for Boss's exclude/delete call                                                                            | root + `05_CDM_EARCatalog/`                                                       | 1              |        |
| WP1  | **Business Objective / Platform Rationale (NEW)** | Draft: why this platform exists, who it serves, what's lost without it — grounded in TOR language + Strategic Alignment Deck already accepted by Director Toey. Feeds WP6 (Gap Analysis) and WP8 (Recommendations) as the thing they're justified against                                                                          | new file in `00_Strategy_Reports/`                                                | 1–3            |        |
| WP2  | Data Inventory                                    | Re-score `data_catalog_v3.csv` (260 rows) against the top-10-critical-asset test; deep-capture the 9-field profile (Section 2.1) for those 10                                                                                                                                                                                      | `03_DataInventory_DQ/`                                                            | 2–4            |        |
| WP3  | Data Product Inventory                            | Business metadata + 5-role governance assignment + compliance classification for the same 10 assets. **No Data Contracts** (cut — see WP8)                                                                                                                                                                                         | `03_DataInventory_DQ/` or `02_UseCases_FunctionalSpecs/`                          | 3–5            |        |
| WP4  | Sitemap                                           | No new work — `NCAIF_Detailed_Sitemap_v8.md` (D-050) already satisfies this item. Confirm and close                                                                                                                                                                                                                                | `01_Sitemap_InterfaceMapping/`                                                    | 1 (check only) |        |
| WP5  | Data Management Framework                         | 4 sub-tracks in parallel: Glossary update (catch up to CDM v3 entities); CDM conflict resolution (from WP0); Governance 5-role/RACI matrix + sign-off gate; Reference Data — **deferred, log only, no build**                                                                                                                      | `04_Glossary/`, `05_CDM_EARCatalog/`, `07_Governance_RACI/`, `08_RefData_Matrix/` | 3–7            |        |
| WP6  | Use Case & Demand Analysis                        | (a) Business NFR thresholds table enriching the **9 high-signal services** (8 from D-043 + A-BTR) — freshness, compliance, access-latency-by-persona, retention, semantic consistency; (b) full Functional Spec + Assumption Log for the **1–2 use cases selected as build-next** (selection still open — see Open Decision below) | `02_UseCases_FunctionalSpecs/`                                                    | 5–9            |        |
| WP7  | Gap Analysis                                      | Score DATER dimensions 1–6 against the Item 1 rationale + current state; dimensions 7–9 explicitly deferred to build-stage                                                                                                                                                                                                         | new file, likely `00_Strategy_Reports/`                                           | 8–10           |        |
| WP8  | Recommendations                                   | Roadmap + budget note (reuse TOR70 briefing deck's 3+2 use-case list, D-053); **explicitly names Data Contracts and full Reference Data build as TOR70/next-phase tasks**                                                                                                                                                          | `00_Strategy_Reports/`                                                            | 9–11           |        |
| WP9  | LDM                                               | Add missing deliverable record (it has no D-ID despite being CRDB's most mature output); link to shared glossary/metric register from WP5                                                                                                                                                                                          | `06_LDM_LossDamage_DataModel/` + ledger                                           | 2 (quick)      |        |
| WP10 | Final Packaging                                   | Assemble WP1–WP9 outputs into `final_report/`'s existing TOR-clause structure; cross-check terminology/phase language across all 9 items; verify every Functional Spec TBD has an owner+deadline                                                                                                                                   | `final_report/`                                                                   | 11–13          |        |
| WP11 | Communication Deck                                | Executive-facing slide deck for DCCE: platform rationale (WP1), what's being delivered (WP2–9 summary), gap analysis headline (WP7), recommendations + budget ask (WP8), TOR70 bridge. Likely reuses the executive-deck design system from D-058                                                                                   | new Artifact or `00_Strategy_Reports/`                                            | 12–14          |        |

**Sealing note:** per project rules, none of WP0–WP11's outputs get written into `CRDB-Change-Log.md`, `CRDB-Deliverable-Map.md`, `CRDB-Evidence-Registry.md`, or `CRDB-Trigger-Log.md` directly — each WP's output gets drafted as a normal file first, then committed to those ledgers via the `seal` skill once Boss confirms it's ready (consistent with the existing D-057/D-058 pattern).

---

## Open Decision Needed Before WP6 Can Finish

Which **1–2 use cases** get the full Functional Spec (sample data, sign-off, ECA discipline)? The TOR70 briefing deck (D-053) already names a 3+2 priority list (spatial risk database, hazard/exposure map, Climate Risk Index, then A-BTR + disaster-loss-statistics) — but the redirection plan's Section 2.6 scale correction caps *full* Functional Specs at 1–2 for the two-week window. This needs Boss's pick from that list before WP6's Functional Spec sub-track can start (the NFR-enrichment sub-track can proceed on all 9 regardless).

---

## Verification

Since this is a documentation/planning sprint, not code, "testing" means:
1. Each WP's draft artifact is reviewed by Boss before being sealed into the ledgers.
2. WP10's cross-check pass explicitly re-reads all 9 items together for terminology consistency (a real risk given the version sprawl already observed in `05_CDM_EARCatalog/`).
3. WP11's deck is reviewed against WP1–WP9's actual content before it goes to DCCE — no claims in the deck that aren't backed by a sealed WP output.
