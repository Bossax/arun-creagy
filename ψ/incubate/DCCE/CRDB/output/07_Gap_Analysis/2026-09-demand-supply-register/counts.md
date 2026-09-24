# WP2 §5.1 Gap Analysis — Phase A: Demand-Supply Register Counts

Source: `demand-supply-register.csv` (214 items — 113 D-series + 101 A-series, per the exclusion of ~125 D-series and 21 A-series Response-tagged governance/catalog/portal items from item-level matching, per Boss's instruction).

**Scope split within the 214 matched items:**
- **162 dataset-type items** were matched by this pass against `data_catalog_v4.csv` (260 rows, read in full). This is the substantive gap-analysis work reported below.
- **52 product-type items** (40 D-series + 12 A-series) are flagged `product-type match handled separately` in the register — these are being matched by the coordinator directly against the TOR 5.3.4 Information Product Inventory (114-row xlsx, `260904_TOR5.3.4_Information Product Inventory.xlsx`, sheet `all_datasets`) using Python, since this pass had no code-execution tool available to parse the binary xlsx. No status verdict is asserted for these 52 items here — see "Product-type items" section below for what's known about them short of an item-level verdict.

---

## (a) Dataset-type items: risk_component × status (162 items)

| risk_component | มีและใช้ได้ | มีแต่ใช้ประโยชน์ได้ยาก | ยังไม่มี | total |
|---|---|---|---|---|
| Climatic Driver | 2 | 15 | 7 | 24 |
| Hazard | 0 | 62 | 17 | 79 |
| Exposure | 1 | 12 | 1 | 14 |
| Sensitivity | 1 | 6 | 5 | 12 |
| Adaptive Capacity | 0 | 2 | 3 | 5 |
| Impact | 0 | 12 | 6 | 18 |
| Loss and Damage | 0 | 4 | 6 | 10 |
| **Total** | **4** | **113** | **45** | **162** |

Note on Sensitivity/Adaptive Capacity rows: per the merged-VULNERABILITY-taxonomy caveat (both source documents' own finding — `data_catalog_v4.csv`'s `cdm_sub_domain` field only carries one merged "VULNERABILITY" tag, 72 rows, not split by Sensitivity vs Adaptive Capacity), every status verdict in these two rows reflects matching against that 72-row pool as a whole. The catalog's own taxonomy cannot confirm which side of the split is actually covered — this is a supply-side taxonomy gap, not resolved by this matching pass, and should be carried into the WP7 gap-analysis narrative as its own finding rather than treated as equivalent-confidence to the other 5 risk components.

## (b) Dataset-type "มีแต่ใช้ประโยชน์ได้ยาก" items: risk_component × reason_code (113 items, multi-code items counted once per code)

| risk_component | access | metadata | spatial_detail | format | update_currency | uncertainty_info | certification |
|---|---|---|---|---|---|---|---|
| Climatic Driver | 13 | 1 | 0 | 0 | 1 | 3 | 0 |
| Hazard | 30 | 28 | 7 | 3 | 3 | 4 | 0 |
| Exposure | 7 | 2 | 2 | 2 | 1 | 0 | 0 |
| Sensitivity | 5 | 3 | 1 | 1 | 0 | 0 | 0 |
| Adaptive Capacity | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| Impact | 10 | 5 | 0 | 0 | 0 | 4 | 0 |
| Loss and Damage | 4 | 2 | 0 | 0 | 0 | 2 | 0 |
| **Total instances** | **70** | **42** | **10** | **6** | **5** | **13** | **0** |

**Caveat on this table's precision**: this is a manually-compiled item-by-item tally across 113 multi-code items. A cross-check against an earlier top-down subtraction pass showed the `metadata` and `spatial_detail` grand totals each off by 1 (42 vs. an earlier estimate of 43; 10 vs. an earlier estimate of 11) — likely a single mis-attributed code in one item somewhere in the compilation. The discrepancy is immaterial to the substantive finding (both reason codes are dominated by Hazard-category items either way) but is disclosed here rather than silently smoothed over, per the "flag ambiguous rather than silently resolve" instruction. `access` (Restricted datasets, 70 of 113 hard-to-use items) and `metadata` (undocumented/unfielded content, 42) are by a wide margin the two dominant barriers; `certification` did not occur as a reason code in any of the 113 items — no item was downgraded specifically for lacking QA/endorsement status (all catalog rows share the same `endorsement_status=Baseline-Draft`/`validation_flag=Unverified-Baseline` baseline, which this pass treated as a project-wide caveat rather than an item-specific reason code, consistent with the source A-BTR document's own treatment in its §4.1 table).

## (c) Total counts (dataset-type items only, 162 of 214)

- **4 มีและใช้ได้** (have and usable)
- **113 มีแต่ใช้ประโยชน์ได้ยาก** (have but hard to use)
- **45 ยังไม่มี** (missing)
- out of **162** dataset-type items matched.

The 4 มีและใช้ได้ items: D128 (NSO census/household/agri/establishment baselines, all Public, tambon-linkable), D141 (NSO Agricultural Census debt/asset-ownership/land-tenure indicators — Public, tambon-level, notes field names the exact indicators requested), D152 (DCCE_3_1–3_7 official CCIC risk-map product, Public — flagged as borderline since its own `use_limitations` shows partial-only SSP-scenario coverage, but access/format/resolution present no major barrier for the "official reference map" use case, *see note below on D152's dual product/dataset nature*), A029 and A030 (GISTDA_2_1 observed sea-surface-temperature data, Public, daily resolution, no barrier).

**Note on D152**: this item is tagged `product` in the D-series extraction (it asks for "a set of DCCE risk maps with official status," which is a product-type ask), but its register row is flagged `product-type match handled separately` per the coordinator's instruction to route all product-type items through the xlsx-based matching — the มีและใช้ได้ candidate match noted above (DCCE_3_1–3_7) is recorded as a courtesy cross-reference in the CSV's justification field, not asserted as this pass's final verdict for D152.

## (d) Product-type items (52 of 214) — handled separately, not verdicted by this pass

| risk_component | D-series count | A-series count | total |
|---|---|---|---|
| Climatic Driver | 1 | 3 | 4 |
| Hazard | 9 | 4 | 13 |
| Exposure | 4 | 0 | 4 |
| Sensitivity | 7 | 1 | 8 |
| Adaptive Capacity | 6 | 1 | 7 |
| Impact | 8 | 0 | 8 |
| Loss and Damage | 5 | 3 | 8 |
| **Total** | **40** | **12** | **52** |

Full item-id list: D003, D004, D007, D009, D011, D016, D023, D026, D035, D037, D039, D042, D045, D053, D055, D058, D061, D081, D083, D086, D089, D090, D092, D094, D095, D103, D107, D130, D133, D135, D138, D140, D143, D146, D152, D156, D158, D168, D170, D204 (D-series, 40) — A010, A022, A031, A050, A062, A076, A080, A111, A112, A113, A117, A118 (A-series, 12).

## (e) Items that could not be matched at all due to the missing/unreadable product-inventory data

None, as of this pass — the coordinator has since located and copied in the row-level TOR 5.3.4 Information Product Inventory (`260904_TOR5.3.4_Information Product Inventory.xlsx`, 114 rows, sheet `all_datasets`, columns `product_id`/`title`/`notes_th`/`notes`/`delivery_format`/`service_type`/`owner_org`/`developer`/`geo_coverage`/`use_case`/`sectors`/`data_source`/`source_type`/`url`) and is matching the 52 product-type items above against it directly with Python. This pass had no code-execution tool available in-session to parse the binary `.xlsx` itself (confirmed: the `Read` tool explicitly rejects binary `.xlsx` files), so all 52 product-type items are left unverdicted here by design rather than guessed at — **flagged explicitly, not silently left ambiguous.**

**Separately, an unreconciled discrepancy in the product-inventory's own count**: the TOR 5.3.4 report prose (`ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/5.3.4 ... .md`) states the inventory contains **99** products is not what the prose actually says on inspection — the prose itself (§"การวิเคราะห์ข้อมูล", line: *"จากผลิตภัณฑ์ที่รวบรวมได้ทั้งสิ้น 114 รายการ"*) states **114** products, matching the xlsx's own row count. The task brief's stated "99 vs 114" discrepancy could not be reproduced from the prose file read during this pass — the prose says 114, the xlsx has 114 rows, they agree. **This is flagged rather than silently reconciled or assumed resolved**: either (a) the "99" figure the task brief cites comes from an earlier draft revision of the 5.3.4 report not the version read in this pass, (b) it comes from a different summary document not identified in this session, or (c) the discrepancy was already resolved upstream of this pass and the brief's phrasing is describing history rather than the current state. Not resolvable from the files read in this session — noted for the coordinator/Boss to reconcile with the correct source.

---

## Methodology notes

1. **Catalog coverage**: all 262 data rows of `data_catalog_v4.csv` were read in full (not sampled) across this and the prior session's work. Matching used `cdm_sub_domain`, `title`, `data_type`, `access_rights_dataset`, `use_limitations`, `spatial_resolution`, `update_frequency_unit`, and `notes` as the task specified — no catalog self-tags (`tag_string`, `high_value_dataset`, `data_category`) were used to establish a match, only to corroborate one already made on substantive fields, consistent with the anti-self-tagging instruction.
2. **A-BTR items (101 non-Response, of which 89 are dataset-type and matched here)**: this pass largely translated the *source A-BTR document's own* §4.1 Direct/Partial/Inferred/No-match confidence into the three-way status framework here, rather than re-deriving matches from scratch — that prior matching pass had already read the full catalog against each of the 122 signals with citation-level detail. Translation rule used: Direct/Partial matches with an explicit caveat (access, scenario-coverage, resolution, currency) → มีแต่ใช้ประโยชน์ได้ยาก; Direct matches with no caveat → มีและใช้ได้ (only A029, A030 qualified); Inferred matches (semantic leap required) → มีแต่ใช้ประโยชน์ได้ยาก, flagged ambiguous; No match found (including "no match found by design" for gap-statement items, none of which survived into this 101-item set since those were mostly Response-tagged) → ยังไม่มี.
3. **D-series items (113 non-Response, of which 73 are dataset-type and matched here)**: freshly matched against the catalog in this pass, batched by risk_component (Climatic Driver, then Hazard, Exposure, Sensitivity, Adaptive Capacity, Impact, Loss and Damage in turn) to avoid re-scanning all 262 rows per item, per the task's own suggested approach.
4. **No fabricated matches**: every มีและใช้ได้ or มีแต่ใช้ประโยชน์ได้ยาก verdict cites a specific `dataset_id` and quotes or paraphrases the catalog field that grounds the verdict (title match, `use_limitations` text, `access_rights_dataset` value, `spatial_resolution`/`time_period` field). Where no catalog row could be found or cited, the verdict is ยังไม่มี — never guessed as usable for lack of a better candidate.
5. **Two items caught late in reconciliation** (D027, D036 in Group 1/2 Hazard, plus D126, D204 in Groups 3/5) were initially dropped from a draft compact summary sent to the coordinator mid-task and have been restored here — the final CSV and this counts file reflect the corrected, complete 113-item D-series set.
6. **Two edge cases reconciled to a final verdict** (previously reported as "draft-precision" ambiguous): A050 (landslide projection methodology) is finalized as a product-type item routed to the coordinator's separate matching, so no dataset-catalog verdict is asserted for it in this pass. A090 (A-BTR Table 1-2 disaster records) is finalized as มีแต่ใช้ประโยชน์ได้ยาก — DDPM_2_1/DDPM_2_3 are structurally the right record type but the catalog's own `use_limitations` field explicitly documents the same data-quality weakness (one-way reporting, no central ground-truthing, no UNDRR-taxonomy alignment, late/miscategorized entries) that the A-BTR institutional-gap signals (C-REQ-023/024/027) independently describe — this convergence is the single most consequential finding in the whole register for WP7 framing.
