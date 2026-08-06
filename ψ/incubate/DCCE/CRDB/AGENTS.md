# CRDB Project — Agent Orientation

CRDB (Climate Risk Database / National Climate Adaptation Information Framework) is a DCCE-commissioned project. This folder is the whole project's home. Read this before touching anything under `output/`.

## What this project is

CRDB is the **Planning + Requirement Analysis + Design** phase of a data platform for DCCE (Settled Finding 3, `research/2026-08-05_lifecycle-grounding/SCOPE_LEDGER.md`). CRDB does not build the system — it hands a requirements blueprint to a downstream contractor, **TOR70**, who builds it. The current work (as of 2026-08-06) is the **final two-week sprint** producing that handoff package. Start with:
- `plans/2026-08-06-crdb-final-sprint-implementation-plan.md` (repo root `plans/`) — the active work plan, 12 work packages (WP0–WP11)
- `ψ/incubate/DCCE/CRDB/research/2026-08-05_lifecycle-grounding/99_FINAL_crdb-redirection-plan-v2.md` — the underlying strategy this sprint implements
- `ψ/inbox/handoff/` (repo root) — most recent session handoff, newest filename wins

## The ledger system — read before editing anything

Four files are the **project ledgers**: `CRDB-Change-Log.md`, `CRDB-Deliverable-Map.md`, `CRDB-Evidence-Registry.md`, `CRDB-Trigger-Log.md` (all at this folder's root). Per the repo-wide `AGENTS.md` mandate: **do not edit these directly** — they are only updated via the `seal` skill, once Boss confirms a deliverable/decision is ready. Draft new content as plain files first; propose the ledger entry; wait for `/seal`.

## `output/` folder structure — two different taxonomies, don't confuse them

There are **two numbering schemes** layered on this project's history. Knowing which one a given number belongs to prevents real confusion:

1. **The old "9-pillar" taxonomy** (`00_Strategy_Reports` … `09_BuildingBlocks`) — CRDB's own self-organized working categories from the May 2026 "Blueprint-as-a-Shield" pivot (D-032, CH-013/CH-014). Most of the project's history (commits, older plans, the 4 ledgers) refers to paths in this scheme.
2. **The new "9-item" DCCE deliverable structure** — what `output/` physically looks like **as of 2026-08-06** (WP0 of the final sprint). This matches the numbering DCCE itself uses for the 8 things it asked for, plus a new Item 1 that CRDB added (Business Objective / Platform Rationale — DCCE never asked for this explicitly, but Boss judged the platform's "why" was never made explicit and needed to be before the handoff).

**The physical folders were renamed/merged on 2026-08-06 to match scheme 2.** The 4 ledgers and most older docs still cite scheme-1 paths (e.g. `output/05_CDM_EARCatalog/...`), which **no longer exist at that path**. Full relink is deferred to WP10 (Final Packaging) — until then, use the translation table below or `output/CRDB-Execution-Architecture-Index.md` (kept current, authoritative navigation entrypoint).

| Current folder | DCCE Item | Old path (still cited in ledgers/history) |
|---|---|---|
| `00_Strategy_Reports/` | — (not a DCCE item; internal strategy/decision trail) | unchanged |
| `01_Business_Objective_Platform_Rationale/` | Item 1 (new) | none — new |
| `02_Data_Inventory/` | Item 2 | `03_DataInventory_DQ/` |
| `03_Data_Product_Inventory/` | Item 3 (new) | none — new |
| `04_Sitemap/` | Item 4 | `01_Sitemap_InterfaceMapping/` |
| `05_Data_Management_Framework/Glossary/` | Item 5 (sub) | `04_Glossary/` |
| `05_Data_Management_Framework/CDM_EARCatalog/` | Item 5 (sub) | `05_CDM_EARCatalog/` |
| `05_Data_Management_Framework/Governance_RACI/` | Item 5 (sub) | `07_Governance_RACI/` |
| `05_Data_Management_Framework/RefData_Matrix/` | Item 5 (sub) | `08_RefData_Matrix/` |
| `06_Use_Case_Demand_Analysis/` | Item 6 | `02_UseCases_FunctionalSpecs/` (also absorbed `A-BTR_requirement_analysis/`, previously at output root, as a subfolder) |
| `07_Gap_Analysis/` | Item 7 (new) | none — new |
| `08_Recommendations/` | Item 8 (new) | none — new |
| `09_LDM_LossDamage_DataModel/` | Item 9 | `06_LDM_LossDamage_DataModel/` |
| `99_BuildingBlocks_Dormant/` | — (no DCCE item; retire-or-continue call still open) | `09_BuildingBlocks/` |

Why one DCCE item spans four subfolders (Item 5): the redirection plan's own gap analysis found that "Data Management Framework" is DCCE's umbrella term for glossary + conceptual model + governance + reference data together — CRDB's four separate pillar categories don't collapse into one DCCE ask by accident, they're genuinely one deliverable with four parts.

**Other moves from the same restructure:**
- `interim-report/` and `Interview summary notes/` → `archive/` (both stale/superseded, not touched further this sprint)
- CDM's superseded `Domains`/`Entities`/`Relationships` CSV versions → `05_Data_Management_Framework/CDM_EARCatalog/archive/`. Canonical CDM data is always the **highest version number** present outside that archive subfolder (currently `Domains-v3.csv`, `Entities-v3.csv`, `Relationships-v4.csv`, D-051) plus the narrative doc `Pillar_05_CDM_EARCatalog_Deliverable.md` (D-036). The older `Conceptual Data Model for climate risk and adaptation data system.md` (D-010) is marked superseded in-file — don't treat it as current.

**Untouched, not part of either numbering scheme:**
- `final_report/` — submission staging, organized by TOR clause number (5.2–5.5 + appendices)
- `2026-05-18_TOR-Review/` — TOR70 briefing/analysis deck (D-053–055), feeds Item 8
- `consultation_workshop/` — includes a gitignored, untracked Python venv under `mvp/code/`; left in place, do not restructure or delete
- `00_Drafts_Archive/`, `TOR5.5_article_and_infoghraphic/` — self-contained, leave alone

## Working conventions specific to this project

- New empty item folders (1, 3, 7, 8) each carry a placeholder `README.md` explaining what work package fills them — check there before assuming a folder is truly empty of intent.
- File naming favors versioned suffixes (`-v2`, `-v3`, `-final`, `-edited`) over overwriting — when in doubt about which version is canonical, the highest version number outside an `archive/` subfolder wins, and superseded predecessors get moved to an `archive/` subfolder rather than deleted (matches the project-wide "nothing deleted" philosophy).
- Thai-language filenames are common (service intelligence docs, sitemap Thai titles, TOR-clause drafts) — don't assume an English-only file list when searching.
