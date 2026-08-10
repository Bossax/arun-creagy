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
| WP0  | Housekeeping                                      | Retire/rewrite stale `CRDB-Execution-Architecture-Index.md`; resolve CDM's two conflicting sealed records (pick canonical, mark other superseded); log Reference Data as deferred-to-TOR70 decision; flag the stray venv for Boss's exclude/delete call                                                                            | root + `05_CDM_EARCatalog/`                                                       | 1              | **Done — see WP0 Completion Log** |
| WP1  | **Business Objective / Platform Rationale (NEW)** | Draft: why this platform exists, who it serves, what's lost without it — grounded in TOR language + Strategic Alignment Deck already accepted by Director Toey. Feeds WP6 (Gap Analysis) and WP8 (Recommendations) as the thing they're justified against                                                                          | new file in `00_Strategy_Reports/`                                                | 1–3            | **Done — see WP1 Completion Log** |
| WP2  | Data Inventory                                    | **Revised 2026-08-07 (Option 1 "Two and Done" + Boss feedback):** no STM. Instead, a **Data Domain Highlight** — for A-BTR, derived from the existing dissection DB (`06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/`: theme/quantitative_value/requirement_statement tables, 379 requirements, 133 themes); for disaster-loss-statistics, derived from the WP2 Stage A demand-signals draft (`wp2-demand-signals-draft.md`, 6 of its 44 signals, Service 4). Cross-referenced against `data_catalog_v4.csv` (confirmed clean — an earlier reported Thai-text corruption in v4 was a `Grep`-tool display artifact, not real corruption; v3 fallback was designed but not needed) to flag implicated domains only — not field-level. **2026-08-10 completion note:** a third track (DCCE's own climate risk map input datasets) was considered and explicitly deferred to a later session per Boss; final output is the audience-facing `02_Data_Inventory/WP2-Findings-Report.md`, sealed as D-060 (T-044/CH-038). | `02_Data_Inventory/`                                                            | 1–2            | **Done — sealed as D-060 (see `CRDB-Change-Log.md` CH-038)** |
| WP3  | Data Product Inventory                            | **Revised 2026-08-07:** dropped to pure **stocktaking** — list of data products/assets implicated by the 2 priority use cases (from WP2's domain highlight), what exists + where + named owner only. No per-asset governance/compliance depth, no business-metadata build-out. **No Data Contracts** (cut — see WP8)                                                                                                                                                                                         | `03_Data_Product_Inventory/`                          | 1              |        |
| WP4  | Sitemap                                           | No new work — `NCAIF_Detailed_Sitemap_v8.md` (D-050) already satisfies this item. Confirm and close. **+ framing line (2026-08-07):** label as the web-platform/presentation layer, built on the data platform (WP2/3/5/9) — not a substitute for it                                                                                                                                | `04_Sitemap/`                                                    | 1 (check only) |        |
| WP5  | Data Management Framework                         | 4 sub-tracks in parallel: Glossary update (catch up to CDM v3 entities); CDM conflict resolution (from WP0); Governance 5-role/RACI matrix — **stays prose, not tabled** (Option 1, 2026-08-07); Reference Data — **deferred, log only, no build**                                                                                                                      | `05_Data_Management_Framework/`                                                   | 2–4            |        |
| WP6  | Use Case & Demand Analysis                        | **Revised 2026-08-07 (Option 1):** (a) NFR thresholds table scoped to the **2 priority services only** (A-BTR, disaster-loss-statistics), not all 9; (b) full Functional Spec + Assumption Log entries + data-specific Acceptance Criteria for **A-BTR + disaster-loss-statistics** (RESOLVED selection — see Open Decision below). **+ layer tagging:** each requirement tagged data-platform vs. web-platform concern | `06_Use_Case_Demand_Analysis/`                                                    | 2–4            |        |
| WP7  | Gap Analysis                                      | Score DATER dimensions 1–6 against the Item 1 rationale + current state; dimensions 7–9 explicitly deferred to build-stage. **+ split scoring (2026-08-07):** data-platform gaps and web-platform gaps scored separately, per Item 1's 1a framing, not blended                                                                                                                         | `07_Gap_Analysis/`                                           | 4–5           |        |
| WP8  | Recommendations                                   | Roadmap + budget note (reuse TOR70 briefing deck's 3+2 use-case list, D-053); explicitly names Data Contracts and full Reference Data build as TOR70/next-phase tasks. **Expanded 2026-08-07 — becomes the deferral collector:** the other 7 services' NFR/acceptance-criteria/domain-profiling, the ~250 remaining catalog rows' domain profiling, RACI-as-a-formal-table, and DAMA-6 DQ thresholds — each named, owned (TOR70), and phased, not left as a vague gap. **+ sequencing recommendation:** data-platform layer (governance, CDM, catalog) must be built/governed before or alongside the web-platform/CMS layer, naming the Frankenstein Dashboard risk (Section 2b, WP1) as the reason                                                                                          | `08_Recommendations/`                                                            | 5–6         |        |
| WP9  | LDM                                               | Add missing deliverable record (it has no D-ID despite being CRDB's most mature output); link to shared glossary/metric register from WP5                                                                                                                                                                                          | `09_LDM_LossDamage_DataModel/` + ledger                                           | 1 (quick)      |        |
| WP10 | Final Packaging                                   | Assemble WP1–WP9 outputs into `final_report/`'s existing TOR-clause structure; cross-check terminology/phase language across all 9 items; verify every Functional Spec TBD has an owner+deadline. **+ new artifact (2026-08-07):** Assumption Log / Client Dependency Register, platform/governance-level, logging the 4 stalled DCCE decisions (adoption metric, phase-2 trigger, governance ratification, DBA org assignment) as bottleneck evidence; verify every WP8 deferral has a real owner+phase. **+ WP1 terminology touch-up:** "data platform" vs. "data system" find-and-standardize pass, folded into this sweep — not a separate workstream                                                                                                                                   | `final_report/`                                                                   | 6–7          |        |
| WP11 | Communication Deck                                | Executive-facing slide deck for DCCE: platform rationale (WP1), what's being delivered (WP2–9 summary), gap analysis headline (WP7), recommendations + budget ask (WP8), TOR70 bridge. Likely reuses the executive-deck design system from D-058. No compression needed under Option 1. **+ dedicated slide (2026-08-07):** web platform vs. data platform, as the headline reframe for DCCE's own "we want a website" mental model (Item 1, Section 1a)                                                                                   | new Artifact or `00_Strategy_Reports/`                                            | 7          |        |

**Sealing note:** per project rules, none of WP0–WP11's outputs get written into `CRDB-Change-Log.md`, `CRDB-Deliverable-Map.md`, `CRDB-Evidence-Registry.md`, or `CRDB-Trigger-Log.md` directly — each WP's output gets drafted as a normal file first, then committed to those ledgers via the `seal` skill once Boss confirms it's ready (consistent with the existing D-057/D-058 pattern).

---

## Deliverable Pack Decision: Option 1 "Two and Done" (2026-08-07)

With ~7 days remaining, a standards-alignment audit (`research/2026-08-06_deliverable_alignment_audit/`) flagged 3 critical + 3 recommended gaps against DCCE-TOR/TOR70 handoff standards. A two-persona debate (Standards Architect vs. Pragmatic Delivery Lead — `research/2026-08-07_deliverable_pack_prioritization/`) weighed closing those gaps broadly (top-10 assets, all 9 services) against concentrating fully on the 2 already-locked priority use cases (A-BTR, disaster-loss-statistics) and deferring the rest to TOR70 as named, owned, phased tasks — the same pattern already used for Data Contracts and Reference Data. Boss chose **Option 1 ("Two and Done")**: the deciding evidence was that 4 DCCE-side decisions (adoption metric, phase-2 trigger, governance-committee ratification, DB-admin org assignment) are *already* stalled in DCCE's own queue — direct evidence the bottleneck is DCCE's review bandwidth, not CRDB's documentation depth. Authoring more artifacts this week doesn't buy faster sign-off, it just builds backlog.

Boss further scoped down WP2/WP3 beyond Option 1's original shape: no field-level STM at all (not even for the 2 priority use cases) — instead a lightweight **Data Domain Highlight** reusing the already-existing A-BTR dissection database and the WP2 Stage A demand-signals draft; and WP3 dropped to pure stocktaking rather than per-asset governance/compliance depth. Boss also asked WP1 (already sealed as "done") to carry one addendum: a new Section 1a distinguishing **web platform** (what TOR70's "central dashboard" ask literally describes) from **data platform** (what CRDB-TOR §1's fragmentation/governance gap actually requires) — reframing DCCE's own two-altitude TOR language as one pattern (DCCE asked for a website; the gap is the data platform underneath it) rather than two separate depths. This substantially resolves WP1's previously-open item #1 (the two-altitude merge), and ripples as light framing-only additions into WP4 (label as web-platform layer), WP6 (layer-tag each requirement), WP7 (score data-platform vs. web-platform gaps separately), WP8 (recommend the data-platform layer be built/governed before or alongside the web-platform/CMS layer), and WP11 (a dedicated slide, since this speaks directly to DCCE's own mental model).

---

## WP0 Completion Log (2026-08-06)

WP0 went beyond the original housekeeping scope — the folder restructure (originally a later, undated ask) got pulled forward and executed in the same session. What actually happened, in order:

**1. CDM conflicting-records resolution**
- Confirmed via Boss: D-010 (`Conceptual Data Model for climate risk and adaptation data system.md`) is the original conceptual/prototyping-stage note. Canonical CDM content is the **highest-version CSVs** (`Domains-v3.csv`, `Entities-v3.csv`, `Relationships-v4.csv`, D-051) plus the hardened narrative doc (`Pillar_05_CDM_EARCatalog_Deliverable.md`, D-036, already "v3.0 Institutionalized & Hardened" — needed no changes).
- Added an in-file superseded marker to D-010 pointing to D-036/D-051. **Ledger status change (D-010 → superseded) is not yet applied to `CRDB-Deliverable-Map.md` — still pending `/seal`.**

**2. Reference Data deferral logged**
- New decision file: `DECISION-2026-08-06-Reference-Data-Deferred-to-TOR70.md` (now at `05_Data_Management_Framework/RefData_Matrix/` after the restructure below). Records that Reference Data is out of scope for this sprint and named as a TOR70/next-phase task in WP8, not silently dropped.

**3. Stray venv (`consultation_workshop/mvp/code/`)**
- Confirmed already covered by existing `.gitignore` patterns (`venv/`, `venv_clean/`, `**/venv/`) and confirmed untracked via `git ls-files` (0 matches). No action needed; left in place per Boss's call.

**4. Folder restructure — physical `git mv`, not just an index**
Boss chose the higher-risk option explicitly: physically merge the old 9-pillar taxonomy into the new 9-item DCCE structure now, and defer relinking historical references to WP10 ("move now, relink later"). Executed via `git mv` (history preserved) across ~214 files:

| New folder | Item | Was |
|---|---|---|
| `00_Strategy_Reports/` | — (not a DCCE item) | unchanged |
| `01_Business_Objective_Platform_Rationale/` | Item 1 (new) | new, empty — placeholder `README.md` added |
| `02_Data_Inventory/` | Item 2 | `03_DataInventory_DQ/` |
| `03_Data_Product_Inventory/` | Item 3 (new) | new, empty — placeholder `README.md` added |
| `04_Sitemap/` | Item 4 | `01_Sitemap_InterfaceMapping/` |
| `05_Data_Management_Framework/{Glossary,CDM_EARCatalog,Governance_RACI,RefData_Matrix}/` | Item 5 | `04_Glossary/`, `05_CDM_EARCatalog/`, `07_Governance_RACI/`, `08_RefData_Matrix/` |
| `06_Use_Case_Demand_Analysis/` | Item 6 | `02_UseCases_FunctionalSpecs/`; also absorbed `A-BTR_requirement_analysis/` (was at output root) as a subfolder |
| `07_Gap_Analysis/` | Item 7 (new) | new, empty — placeholder `README.md` added |
| `08_Recommendations/` | Item 8 (new) | new, empty — placeholder `README.md` added |
| `09_LDM_LossDamage_DataModel/` | Item 9 | `06_LDM_LossDamage_DataModel/` |
| `99_BuildingBlocks_Dormant/` | — (no DCCE item; retire/continue call still open) | `09_BuildingBlocks/` |

Also archived (not deleted): `interim-report/` and `Interview summary notes/` → `archive/`.

**Known gap left open by "relink later":** the 4 ledgers (`CRDB-Change-Log.md`, `CRDB-Deliverable-Map.md`, `CRDB-Evidence-Registry.md`, `CRDB-Trigger-Log.md`) and most historical docs still cite the **old** pillar paths. `CRDB-Execution-Architecture-Index.md` carries an old→new path translation table as a bridge until WP10's full relink pass.

**5. CDM version-sprawl cleanup**
- 12 superseded `Domains`/`Entities`/`Relationships` CSV versions (`-v2`, `-edited`, `-v2-final`, etc.) archived into `05_Data_Management_Framework/CDM_EARCatalog/archive/`, leaving only the canonical v3/v4 files and current docs visible at the top level.

**6. `CRDB-Execution-Architecture-Index.md` rewritten**
- Replaced stale April-2026 links with the current 9-item folder table, the old→new path bridge, and pointers to `final_report/`, the 4 ledgers, and this sprint plan.

**7. New orientation docs**
- `ψ/incubate/DCCE/CRDB/AGENTS.md` and `CLAUDE.md` (the latter just `@`-includes the former, matching the repo-root pattern) — explain the dual old/new taxonomy, the ledger no-direct-edit rule, and working conventions (highest-version-wins, archive-not-delete, Thai filenames) to any future session working in this folder.

**Committed:** `9804e48` (sealed redirection plan, pre-existing), `a09d256` (WP0 restructuring + orientation docs), `32b3ead` (session retrospective). Not yet pushed beyond `a09d256`.

---

## WP1 Completion Log (2026-08-06)

WP1 ran as a TOR-grounded first draft followed by a full collaborative-session pass, producing two files in `01_Business_Objective_Platform_Rationale/`:

- **`2026-08-06-Business-Objective-Platform-Rationale.md`** — the deliverable itself. Sections: 1 (Why This Platform Exists — two deliberately-separate altitudes, governance-capability gap vs. public-dashboard gap), 2 (Who It Serves — personas, not role-title lists), 2a (Scope & Phasing), 2b (Vision & Success Criteria), 2c (Constraints & Dependencies), 3 (What's Lost Without It), 4 (How This Feeds the Rest of the Package), 5 (Diagnosis — includes a named-owner open-decisions table), and an Appendix (TOR Clause → Product-Language Translation).
- **`2026-08-06-WP1-Collaborative-Session-Guide.md`** — facilitation companion: an ideal-doc checklist (12 questions), a gap map against the draft, and 5 guided-question groups (A–E). **All 5 groups are now resolved**, grounded in secondary sources brought in mid-session (Strategic Alignment Deck, human-reviewed TOR70 briefing deck, Director Engagement Slide Flow, the FGD3 focus-group deck, and `Proposed-governance-plan-to-DCCE.md`) plus direct guidance from Boss and Director Toey.

**What got resolved, group by group:**
- **A — Scope & Phasing:** one platform (the Data Hub) delivered in phases, not two competing products. Phase-1 = 5 core products (3 existing analytical tools + disaster-loss-statistics + A-BTR) + website content + Data Hub foundation. A-BTR named as a separate internal mandate-compliance service, not a catalog-item fill. Catalog item 3 (financial/budget decision-support) explicitly excluded — feasibility too low. No phase-2 trigger defined; CRDB's job is to propose options, not decide one.
- **B — Vision & Success Criteria:** two-level vision (long-term 8-catalog vs. phase-1 concrete site structure + products). 7 checkable phase-1 success criteria. Adoption/usage metric explicitly and deliberately left open — DCCE's call, noted not dropped.
- **C — Personas & Who It Serves:** sectoral/area-based policymakers-authorities (primary external, split by sophistication) and DCCE staff/analysts (primary internal), with DCCE leadership/academics/budget officials as secondary. Explicit, stated phase-1 ceiling: no tailored per-sector/area support yet.
- **D — Constraints & Dependencies:** the database-administrator role resolved to a functional definition (CMS/content-administration, inferred from TOR70 §5.4.14 + §5.5, not a named TOR role). Governance dependency resolved to CRDB's own already-drafted 2-phase roadmap (`Proposed-governance-plan-to-DCCE.md`, the same one FGD3 Slide 23 references) — Phase 1 (0–6mo: standards/roles/committee/inventory) as the minimum bar, Phase 2 (1yr+) as outward-facing and not a phase-1-platform dependency.
- **E — Ownership & Open Decisions:** every remaining open item given a named owner in a Section 5 table (CRDB owns the problem-statement merge and appendix prioritization; DCCE owns the adoption metric, phase-2 trigger, governance-committee ratification, and DB-admin org assignment). A standalone open-decisions-log artifact was considered and deliberately skipped as unnecessary.

**What's still open, carried forward (CRDB's own remaining synthesis work, not blocked on DCCE):**
1. Merge Section 1's two-altitude problem statement into one.
2. Prioritize the ~13 needs in the Appendix.

**Not yet sealed:** per project rules, none of WP1's content has been written into the 4 ledgers — both files exist as plain drafts pending Boss's `/seal` call.

**Committed:** none of WP1's edits are committed yet (working-tree changes as of this log). A related retrospective and lesson-learned are committed at `823c586` (`rrr: crdb-wp1-personas-constraints-ownership-closure`).

---

## Open Decision Before WP6 Can Finish — RESOLVED (2026-08-06)

Which **1–2 use cases** get the full Functional Spec (sample data, sign-off, ECA discipline)? Resolved: **A-BTR reporting system + disaster-loss statistics analysis** — the 2 new products from the TOR70 briefing deck's "3+2" grouping (Slide 15, `TOR70_briefing-deck_slide-text.md`). The "3" in that grouping are DCCE's existing tools, which DCCE itself owns the enhancement-requirements for — out of CRDB's Functional Spec scope. CRDB's own scope centers on the 2 new products it proposed, which have no other owner, and the count (2) matches the 1–2 cap exactly. No further narrowing needed. (The NFR-enrichment sub-track still proceeds on all 9 services regardless.)

---

## Verification

Since this is a documentation/planning sprint, not code, "testing" means:
1. Each WP's draft artifact is reviewed by Boss before being sealed into the ledgers.
2. WP10's cross-check pass explicitly re-reads all 9 items together for terminology consistency (a real risk given the version sprawl already observed in `05_CDM_EARCatalog/`).
3. WP11's deck is reviewed against WP1–WP9's actual content before it goes to DCCE — no claims in the deck that aren't backed by a sealed WP output.
