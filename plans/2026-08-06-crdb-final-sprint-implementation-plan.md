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
| WP4  | Sitemap                                           | `NCAIF_Detailed_Sitemap_v8.md` (D-050) already satisfies this item structurally — confirm and close, no restructuring. **+ framing line (2026-08-07):** label as the web-platform/presentation layer, built on the data platform (WP2/3/5/9) — not a substitute for it. **+ Content Source Gap Analysis (2026-08-10, new):** per-node grouping of the 41 v8 nodes' 63 discrete content requirements (extracted fresh from `NCAIF_Detailed_Sitemap_v8.md`, since the companion `ncaif_sitemap_nodes.csv` field is incomplete) against DCCE's current 391-asset `DCCE_Unified_Digital_Asset_Database.csv` — topical candidate-asset matching only (not a usability/readiness verdict, which would require reading full asset content), flagging zero-match items as real gaps. Supersedes the 2026-07-10 `dcce_assets_content_gap_analysis.md`, which left its own gap section empty; that file stays in place as superseded groundwork, untouched. **2026-08-11 completion note:** extended to a fourth cross-check pass against WP2's separate 260-item `data_catalog_v4.csv` for the 16 analytical/dashboard requirements, plus a full node-level (X.X grain) deep-dive companion covering all 15 second-level sitemap sections. Final: 73 requirements, 21 full / 24 partial / 28 gap. Outputs: `04_Sitemap/wp4-requirement-items-v8.csv`, `04_Sitemap/2026-08-10-WP4-Content-Source-Gap-Analysis.csv` + `.md`, `04_Sitemap/2026-08-11-WP4-Node-Level-Deep-Dives.md`, and a cross-WP synthesis narrative at `00_Strategy_Reports/2026-08-11-NCAIF-Design-Summary-Report.md`. | `04_Sitemap/`                                                    | 1–2 | **Done — see WP4 Completion Log** |
| WP5  | Data Management Framework                         | 4 sub-tracks in parallel: Glossary update (catch up to CDM v3 entities); CDM conflict resolution (from WP0); Governance 5-role/RACI matrix — **stays prose, not tabled** (Option 1, 2026-08-07); Reference Data — **deferred, log only, no build**                                                                                                                      | `05_Data_Management_Framework/`                                                   | 2–4            | **Done — see WP5 Completion Log** |
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

## WP2 Completion Log (2026-08-10)

WP2 went through a real mid-execution correction before landing on its final scope, and that correction is worth recording alongside the result.

**What was built, in order:**
- **Stage A** (`02_Data_Inventory/wp2-demand-signals-draft.md`) — 44 demand signals extracted from D-043's 8 services, Boss-reviewed with 5 inline domain corrections incorporated (notably: the DOPA/LPA dataset named in a Service-7 signal is request-only and never actually resolves to municipal-level data; Service 1 and the Service-8 cluster recharacterized as out of WP2's dataset-matching scope entirely).
- **First Stage B attempt** (`wp2-catalog-scoring-draft.md`) — scored all 44 signals against the full 260-row catalog for a catalog-wide "top 10" shortlist. **This was the wrong scope**: it re-derived the "top-10 assets, all 9 services" option that Boss had already explicitly rejected in the 2026-08-07 Deliverable Pack Decision below, in favor of the narrower Data Domain Highlight. Caught only after Boss asked "why start with the top 10 datasets?" and the sprint plan's own decision history was re-traced. Left on disk, not deleted, as the record of that miss.
- **Corrected two-track Data Domain Highlight** (`wp2-data-domain-highlight-draft.md`) — Track 1 (A-BTR) re-grounded in the A-BTR requirement-dissection database directly (379 requirement rows, not D-043 — A-BTR is a distinct use case D-043 never covered), extracting 122 data-shaped signals; Track 2 (disaster-loss-statistics) reused D-043 Service 4's 6 existing signals verbatim. Matched against `data_catalog_v4.csv` (see correction below), ~55 signals achieved Direct/Partial confidence, ~53 returned genuine no-match (feeding WP7), and 6 open ambiguities were flagged rather than guessed. Boss left 5 further inline corrections (most consequentially: the DCCE composite risk index is confirmed *not* the same product as the BTR's "Yearly Vulnerability Index"/"Climate Resilience Index," and is a policy-communication "gold layer" — its multiplicative, equal-weighted, [0.1, 0.9]-normalized methodology irreversibly compresses its line-agency inputs, so it cannot be reused as platform infrastructure). All incorporated.
- **`data_catalog_v4.csv` corruption correction**: a background diff subagent had reported ~55,700 Thai characters corrupted into literal `?` runs, "confirmed via raw byte inspection." This was false — direct hex inspection found zero corruption; the apparent garbling was the `Grep` tool's own display path silently mangling multi-byte Thai UTF-8 on this environment. v4 is now used directly as the sole catalog reference, no v3 fallback needed.
- **`WP2-Findings-Report.md`** — the final audience-facing synthesis essay (deliberately free of internal dataset IDs, signal codes, and WP jargon, per Boss's explicit ask), covering which existing datasets/domains matter for A-BTR and disaster-loss-statistics, the DCCE climate risk map's actual role and limits (grounded via a NotebookLM query set against the underlying RU-CORE technical methodology report, not just asserted), and the confirmed data gaps.
- A third track — the DCCE risk map's own composite-index *input* datasets (Exposure/Sensitivity/Adaptive-Capacity variables from 12+ line agencies) — was scoped, then **explicitly deferred to a later session** per Boss.

**Sealed:** `WP2-Findings-Report.md` is sealed as **D-060** (Trigger T-044, Change CH-038, Evidence E-077–E-079) — see `CRDB-Change-Log.md` CH-038 for the full decision record.

**Not yet committed:** WP2's file changes are working-tree changes as of this log, not yet committed to git.

**Unblocks:** WP3 (Data Product Inventory stocktake), which is scoped in this plan to reuse WP2's domain highlight directly.

---

## WP4 Completion Log (2026-08-11)

WP4's original content-source gap analysis (73 requirements against DCCE's 391-item asset inventory, sealed as the 2026-08-10 report/CSV) was extended over two follow-up sessions into its final form:

**1. Fourth cross-check pass — dataset catalog, not just documents**
The 391-item inventory mixes documents, media, systems, and datasets together, which understates risk for pages that need real structured data (dashboards, maps, indices) rather than a topically-relevant publication. The 16 requirements judged analytical/interactive/data-driven were re-checked against WP2's separate, dataset-only `data_catalog_v4.csv` (260 rows). Result: 5 items moved from gap to partial (national risk index, historical extreme-weather stats, climatology variables, downscaled projections, sea-level rise), 2 partial items got stronger evidence (coastal erosion index, loss-and-damage dashboard), and one item (the national M&E tracker) was flagged for downgrade, then re-verified.

**2. The M&E tracker correction**
The tracker's cited asset wasn't in the 260-row extract, so it was initially downgraded from full to partial. Checked instead directly against DCCE's live Data Governance Framework catalog (`dgf.dcce.go.th/dataset/m-and-e`), the asset turned out to be real, current, and maintained by DCCE's dedicated Adaptation M&E Evaluation Group, tied to Thailand's official UNFCCC Biennial Transparency Report — the original full-coverage rating was reinstated. A remaining gap in the same node (a technology-readiness-level framework) was then marked covered on Boss's direction, on the reasoning that content genuinely within DCCE's confirmed, actively maintained M&E platform should be assumed in scope rather than checked item-by-item — flagged in the underlying files as an assumption, not an independently verified match. Node 3.4 (Monitoring & Evaluation) closed fully covered (4/4).

**3. Node-level deep-dive companion (2026-08-11, new)**
Per Boss's request, extended the report's three worked examples to all 15 second-level (`X.X`) sitemap sections, each with a full needs/what-exists/assessment write-up and coverage tally — new file `04_Sitemap/2026-08-11-WP4-Node-Level-Deep-Dives.md`.

**4. Interactive explainer artifact**
An HTML companion page (coverage map, methodology walkthrough, the M&E correction as a callout, all 15 node write-ups in an accordion) was built and published as a private Claude Artifact for Boss's review — not part of the committed file set.

**5. Cross-WP synthesis report (new, spans WP1/WP4)**
`00_Strategy_Reports/2026-08-11-NCAIF-Design-Summary-Report.md` — an audience-facing narrative pulling together why NCAIF exists (WP1), how the sitemap's structure was reached and justified (WP4's design history), and the content-gap findings above, closing with a prioritized "what's next" grounded in this plan's own WP5–WP10 structure. Written for a reader with no CRDB context; internal codes/jargon confined to its appendix.

**Final numbers:** 73 requirements, **21 full / 24 partial / 28 gap**.

**Known open item, carried forward (not blocking WP4's close):** of the 8 items reclassified by the fourth cross-check pass, only the M&E tracker was individually re-verified against DCCE's live catalog. The other 7 (the 5 gap→partial moves plus the 2 evidence-strengthened partials) are real rows within the 260-item catalog with their own dataset IDs and URLs — not missing, so not the same existence question the M&E case raised — but several carry the catalog's own Restricted-access or Baseline-Draft/Unverified flags, unconfirmed against DCCE's live system. Worth closing before WP6/WP8 build a schedule on these specific numbers.

**Not yet sealed:** per project rules, none of WP4's content (the original report, the CSV, the node-level deep-dives, or the synthesis report) has been written into the 4 ledgers — all exist as plain drafts pending Boss's `/seal` call.

**Committed:** none of WP4's edits are committed yet (working-tree changes as of this log).

---

## WP5 Completion Log (2026-08-14)

WP5 closed out the Data Management Framework by synthesizing the Glossary, CDM, and Governance into a formal, unified handoff package (`D-065`, `D-066`, `D-067`) for TOR70, enforcing several critical scoping constraints:

1. **Glossary Scoping**: The master glossary (`NCAIF_Glossary_v5_Master.csv`) was strictly bounded to the climate adaptation platform, rejecting any "DCCE-wide" or "official DCCE glossary" expansion. This ensures clear domain definitions to support data ownership assignments downstream.
2. **Governance Reframing**: Excluded all "RACI" terminology and consultant-jargon (e.g., "anchor", "hub"). Adopted a 4-tier functional governance structure (Committee, Data Owner, Steward, User) grounded directly in the July 2 FGD3 slide deck (`E-083`).
3. **Roadmap Alignment**: The framework was mapped to the 7-phase enterprise data system lifecycle (Phases 1-3 under CRDB, Phases 4-7 under TOR70).
4. **Reference Data Deferral**: Confirmed the deferral of reference data lists to the TOR70 build phase, executing purely as a log constraint rather than a build output.

**Final outputs**:
- `05_Data_Management_Framework/WP5-Data-Management-Framework-Report.md` (D-065)
- `05_Data_Management_Framework/Glossary/NCAIF_Glossary_v5_Master.csv` (D-066)
- `05_Data_Management_Framework/Glossary/NCAIF_Glossary_v5_Review.md` (D-067)

**Sealed**: Trigger T-046, Change CH-040, Evidence E-083.

---

## Open Decision Before WP6 Can Finish — RESOLVED (2026-08-06)

Which **1–2 use cases** get the full Functional Spec (sample data, sign-off, ECA discipline)? Resolved: **A-BTR reporting system + disaster-loss statistics analysis** — the 2 new products from the TOR70 briefing deck's "3+2" grouping (Slide 15, `TOR70_briefing-deck_slide-text.md`). The "3" in that grouping are DCCE's existing tools, which DCCE itself owns the enhancement-requirements for — out of CRDB's Functional Spec scope. CRDB's own scope centers on the 2 new products it proposed, which have no other owner, and the count (2) matches the 1–2 cap exactly. No further narrowing needed. (The NFR-enrichment sub-track still proceeds on all 9 services regardless.)

---

## Verification

Since this is a documentation/planning sprint, not code, "testing" means:
1. Each WP's draft artifact is reviewed by Boss before being sealed into the ledgers.
2. WP10's cross-check pass explicitly re-reads all 9 items together for terminology consistency (a real risk given the version sprawl already observed in `05_CDM_EARCatalog/`).
3. WP11's deck is reviewed against WP1–WP9's actual content before it goes to DCCE — no claims in the deck that aren't backed by a sealed WP output.
