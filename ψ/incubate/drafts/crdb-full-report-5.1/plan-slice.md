# Plan slice — CRDB full report §5.1 (TOR 5.3.8 Gap Analysis)

**Supersedes** the 2026-09-02 plan-slice.md in this folder, which was built around the 8-service platform framing. This version reflects Boss's 2026-09-24 decision to re-analyse the section as an inventory-centred comparison instead. The old `writing-contract.json` and `argument-map.json` in this folder are likewise stale and must be rebuilt from this plan, not patched.

## 0. Why this rewrite (context for a fresh session)

The งวด 4 committee checklist (`ψ/incubate/DCCE/CRDB/inbox_note/2026-09-23-Checklist...md`) asked to redo TOR 5.3.8: make demand analysis complete and aligned with project objectives, show the demand-vs-supply comparison, and complete the Data Inventory.

Reading the TOR as a whole (Objectives 2.1–2.2, the 5.3 heading "Develop Information Product Inventory & Baseline Data Inventory", clauses 5.3.4/5.3.5/5.3.9) shows this is a substantive misfit, not a presentation problem: the **current** `draft.md` answers "what blocks the 8 platform services we designed" — our own question — instead of the TOR's actual ask, "compare agency demand against both inventories, organised by the inventory's own categories, and report gaps in quantity and quality." The 11-structural-gap/8-service framing, the A-BTR case study, and the website-readiness check are all real analysis but answer the wrong question for this clause.

Boss decisions (2026-09-24, all final):
- **Inventory-centred re-analysis.** Axis = TOR 5.3.5's 8 risk components (Climatic Driver, Hazard, Exposure, Sensitivity, Adaptive Capacity, Impact, Response, Loss and Damage), not the 8 services.
- **The 125 D-series "Response"-type items** (governance/catalog/portal asks, not physical-risk data — see §2 below) get **one paragraph** in 5.1.1's coverage reading, not a separate subsection, and are excluded from the Table 5-2/5-3 item-level comparison.
- Trust `/trace` for internal-knowledge searches going forward (this is now a standing rule, not §5.1-specific).

## 1. Evidence base

| Role | Source | Notes |
|---|---|---|
| Demand: agencies | `output/archive/consultation_workshop/user_use_case_raw.md` | 83 use cases → 238 atomic items, extracted and tagged in Phase A (see §3). |
| Demand: DCCE's own reporting duty | `output/02_Data_Inventory/wp2-data-domain-highlight-draft.md` §2/§7 | 122 A-BTR signals, already tagged in Phase A. |
| Supply: datasets | `output/02_Data_Inventory/data_catalog_v4.csv` (260/262 rows) | TOR 5.3.5 Baseline Data Inventory. `cdm_sub_domain` is the real risk-component field. |
| Supply: products | `output/03_Data_Product_Inventory/260904_TOR5.3.4_Information Product Inventory.xlsx`, sheet `all_datasets` | TOR 5.3.4 Information Product Inventory. **114 products, 56 owner orgs** (not the 99/45 that the older report text and slide 39 used — see §6). Copied into the repo this session; previously existed only on OneDrive/SharePoint, never committed to git (confirmed via `/trace`, log at `ψ/memory/traces/2026-09-24/2046_crdb-product-inventory-file.md`). |
| Chapter links | `crdb-full-report-3.2` (interviews/demand themes), `3.3` (use cases → 8 services), `3.4` (both inventories, already updated to 114/56 this session), Chapter 4 (MVD/loss and damage) | Cite these; don't re-derive. |
| Gap causes (recycled as explanation, not backbone) | Current `draft.md` gaps 2–9, WP7 `output/07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md` | |
| Thai TOR wording | `inbox_source/260106_DCCE_Climate risk database_inception report_vfinal.md` (Thai original) | Quote this, never the English `CRDB-TOR.md` translation, in Thai prose. |

## 2. Phase A — DONE (2026-09-24/25)

Full demand-supply register built and saved to `output/07_Gap_Analysis/2026-09-demand-supply-register/`:

| File | Content |
|---|---|
| `demand-items-extracted.md` | 238 items from 83 use cases, tagged by risk_component/type/agency. |
| `demand-items-abtr.md` | 122 A-BTR signals, tagged the same way. |
| `demand-supply-register.csv` | 214 non-Response items (113 D-series + 101 A-series) matched dataset-type against the 260-row catalog. |
| `product-matches.md` | 52 product-type items matched against the 114-row product inventory. |
| `counts.md` | Cross-tabs. |

**Key structural finding**: of 238 D-series items, **125 (53%) are "Response"-type** — governance/catalog/metadata/API/portal asks, not physical-risk data — concentrated in the consultation's Group 5 (32 of 83 use cases, data-governance interpretation). These don't fit the 8-component scheme and can't be matched against either inventory; per Boss's decision they get one paragraph in 5.1.1, not a subsection, and are excluded from the item-level comparison below.

**Combined matched-item totals (266 items, both passes):**

| Status | Dataset (162) | Product (52) | Combined |
|---|---|---|---|
| มีและใช้ได้ (have, usable) | 4 | 4 | **8** |
| มีแต่ใช้ประโยชน์ได้ยาก (have, hard to use) | 113 | 4 | **117** |
| ยังไม่มี (missing) | 45 | 40 | **85** |
| ไม่สามารถจับคู่ได้ (not a matchable demand) | — | 4 | **4** |

Dataset-side `risk_component × status` (162 items — the core Table 5-2 data):

| risk_component | มีและใช้ได้ | มีแต่ใช้ประโยชน์ได้ยาก | ยังไม่มี | total |
|---|---|---|---|---|
| Climatic Driver | 2 | 15 | 7 | 24 |
| Hazard | 0 | 62 | 17 | 79 |
| Exposure | 1 | 12 | 1 | 14 |
| Sensitivity | 1 | 6 | 5 | 12 |
| Adaptive Capacity | 0 | 2 | 3 | 5 |
| Impact | 0 | 12 | 6 | 18 |
| Loss and Damage | 0 | 4 | 6 | 10 |

Hard-to-use reason codes (113 dataset items, multi-code): **access 70**, **metadata 42**, uncertainty_info 13, spatial_detail 10, format 6, update_currency 5, certification 0. `access` and `metadata` dominate by a wide margin — this is the quality-gap section's spine (§5.1.4 below).

**Product-side finding (different shape from dataset side)**: only 8 of 52 product-type demands have any match at all; 40 want a methodology, index, or framework that was never built as a product. This is a *different kind of gap* than the dataset side's "exists but restricted" pattern — state this explicitly, since it implies §5.2 needs two distinct recommendation tracks (open access to what exists vs. build new analytical capability).

**Known caveat to carry into prose**: the catalog's `cdm_sub_domain` only has one merged "VULNERABILITY" tag (72 rows) — it cannot distinguish Sensitivity from Adaptive Capacity content. Every Sensitivity/Adaptive-Capacity verdict above is checked against that merged 72-row pool as a whole. State this as a supply-side taxonomy gap in 5.1.4, not a matching weakness to hide.

**One finding worth flagging to committee-review sensibility**: A090 (A-BTR disaster-record signal) and the catalog's own `use_limitations` field for DDPM_2_1/2_3 independently describe the *same* data-quality weakness (one-way reporting, no central ground-truthing, no UNDRR-taxonomy alignment). Two independent sources agreeing is unusually strong evidence — worth a named callout in 5.1.4 or 5.1.5.

## 3. Chapter flow (Boss-approved outline, reader-journey basis)

Reader = a TOR-literal, non-technical committee member who has just read Chapter 3 (inventories, services) and Chapter 4 (MVD/loss and damage). Rule for every paragraph: start from what the reader already knows, answer one question, introduce at most one new idea (explained before used), end on the question the next paragraph answers.

**Opening (2 paragraphs + Figure 5-1)**
- P1: state DCCE's aim (products that answer agency needs), define ข้อมูลที่ยังขาด / ข้อมูลที่มีแต่ใช้ประโยชน์ได้ยาก using the TOR's own words — these are the measuring stick for the whole section.
- P2: method in 4 plain steps (list items → sort by risk component → look up in both inventories → assign status). Explain why risk components are the sorting frame: the baseline inventory is organised the same way (`cdm_sub_domain`).

**5.1.1 ความต้องการใช้ข้อมูลของหน่วยงาน** (answers checklist item 1)
- P1: demand sources — interviews/workshop (3.2–3.3, don't re-derive), 83 use cases, N agencies, **+ one paragraph on the 125 Response-type items** (per Boss's decision — note the pattern, don't build a subsection), **+ A-BTR as second demand source** (DCCE's own reporting duty).
- P2: explain Table 5-1 before showing it (rows = 8 components, columns = target groups, cells = item counts).
- Table 5-1.
- P3: coverage reading — which components/groups dominate, fit against Objectives 2.1–2.2, thin spots stated honestly.

**5.1.2 ผลการเปรียบเทียบความต้องการกับบัญชีรายการ** (answers checklist item 2)
- P1: recall both inventories by TOR name (260 datasets/44 agencies per 5.3.5; 114 products/56 agencies per 5.3.4 — cite 3.4).
- P2: define the 3 statuses + hard-to-use reason codes.
- Table 5-2 (datasets) and Table 5-3 (products) — components × status, real counts from §2 above.
- P3: reading — where missing clusters, where hard-to-use clusters, note the dataset-vs-product asymmetry.

**5.1.3 ช่องว่างเชิงปริมาณ: ข้อมูลที่ยังขาด** — one paragraph per real missing cluster (45 datasets + 40 products), what's missing → who needs it → what it blocks. Link to Chapter 4 for loss-and-damage.

**5.1.4 ช่องว่างเชิงคุณภาพ: ข้อมูลที่มีแต่ใช้ประโยชน์ได้ยาก** — one paragraph per reason code, largest first: **access (70)**, **metadata (42)**, uncertainty_info (13), spatial_detail (10), format (6), update_currency (5). State the merged-Vulnerability-taxonomy caveat here. Consider the A090/DDPM convergence as a named example.

**5.1.5 ช่องว่างที่ต้องแก้ด้วยการพัฒนาระเบียบวิธีและการตัดสินใจเชิงนโยบาย** (short) — the product-type "never built" finding belongs here: 40 of 52 product demands need new analytical capability, not access or better metadata.

**Closing (1 paragraph + Table 5-4)** — gap type × component × response type (collect/improve/develop method/decide). Hands to 5.2 without stating recommendations.

**Moved out of §5.1**: the 8-service table (services become passing examples only), the A-BTR case-study narrative (folded into demand-source + gap examples above), the 75-topic website-readiness check (does not compare against the TOR inventories — appendix + one sentence, per earlier default, confirm with Boss if not yet done), any recommendation-shaped sentences (→ 5.2).

**Appendix**: the demand-supply register itself, answering checklist item 3.

## 4. Writing pipeline (writing-th revision mode + safeguards)

The 2.3 rewrite (parallel session, same day) showed the writing-th gates can pass while still failing the reader: vague contract-coined labels, dropped subjects/objects (STYLE_PACK_TH rule 11 missing from `prose-kernel.md`), concepts named before being explained, tables before their explanatory prose, meta-commentary about the document's own structure, and a misquoted TOR list — none of which the mechanical lint or the editorial rubric's 9 dimensions actually test. Full diagnosis: `.oracle-shared-skills/skills/writing-th/` stages, `ψ/memory/style/evidence/2026-09-24_19-11_TH_diff-evidence.md`, and the amended `ψ/incubate/drafts/crdb-full-report-2.3/writing-contract.json`/`plan-slice.md` (reader-onboarding rules + `reader_bridge` field — copy this pattern into 5.1's contract/map).

| Stage       | Standard                | Add-on safeguard for §5.1                                                                                                                                                                                                                                                                                                               |
| ----------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 Contract  | `writing-contract.json` | **Term screen**: every term in `terminology` gets a plain-Thai definition + assigned first-use paragraph from §3. Ban สองสาย-style abstractions and แกน/กลไก/โครงสร้าง without a referent. Copy `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md` rules + the 2.3 reader-onboarding rules into `report_specific_rules`.                   |
| 1 Map       | `argument-map.json`     | Every unit gets `reader_bridge` {assumed_knowledge, opening_link, concept_explanation, project_application, transition_to_next} — note: `argument_gate.py` doesn't validate this field, so check it manually. Add a `fidelity-ledger.json`-style list of every Thai TOR quote and every number, with source citation to this file's §2. |
| 3 Verbalize | th-verbalizer           | Explicitly pass STYLE_PACK_TH rule 11 (missing from the compressed kernel) + `required_structures` + each unit's `reader_bridge`. **Pilot gate**: verbalize Opening + 5.1.1 first, Boss reads before the rest runs.                                                                                                                     |
| 4 Lint      | `lint_thai_writing.py`  | Section-local `check_5_1.py` (assert-based): every number traces to §2's counts, every table has explanatory prose before it, no meta-commentary phrases, every map unit has all 5 `reader_bridge` fields.                                                                                                                              |
| 5 Review    | th-editorial-reviewer   | **Cold-reader pass**: fresh subagent gets only the draft + Thai TOR + checklist, plays a non-technical committee member, flags any unexplained term or unanswered question at a subsection boundary.                                                                                                                                    |

## 5. Sequence from here

1. Stage 0 contract + this plan-slice → Boss approves flow (§3) — **flow already approved 2026-09-24**.
2. Build `writing-contract.json` + `argument-map.json` with real counts from §2, `reader_bridge` on every unit → Boss approves map.
3. Pilot-verbalize Opening + 5.1.1 → Boss reads for flow.
4. Remaining sections → lint + `check_5_1.py` → editorial + cold-reader review.
5. Boss approves merge.

## 6. Open items for Boss

- **O2** (was O1 — resolved): product inventory file found and copied in; **99/45/12 → 114/56/14** already corrected in `5.3.4` draft and `crdb-full-report-3.4/draft.md` this session. Slide 39 of the dissemination deck was updated for the clean counts but the "6 agencies = 80%" concentration claim and the old 6-category product-type table were flagged `[ต้องทบทวนกับ Boss]` rather than guessed — the real top-6 owners now sum to only ~38% and UNEP (not a domestic agency) is now #1. Needs your call on how to re-tell that slide.
- **O3**: website readiness check placement — confirm appendix + one sentence, or handle differently.
- **O4**: may §5.1 prose say "ขอบเขตงานข้อ 5.3.8" (as used in the 2.3 rewrite), or name the task without a TOR-clause citation style?
- **New**: the merged-Vulnerability catalog taxonomy (§2 caveat) is a real supply-side gap worth a policy recommendation in 5.2 — flag it there when that section is planned.
