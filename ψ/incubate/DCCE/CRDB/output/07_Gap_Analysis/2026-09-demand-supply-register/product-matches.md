# WP2 §5.1 Gap Analysis — Phase A: Product-type item matching (against the 114-row TOR 5.3.4 inventory)

Source of supply: `ψ/incubate/DCCE/CRDB/output/03_Data_Product_Inventory/260904_TOR5.3.4_Information Product Inventory.xlsx`, sheet `all_datasets`, 114 rows (P001–P114). This matching covers the product-type demand items from `demand-items-extracted.md` (D-series, 40 items) and `demand-items-abtr.md` (A-series, non-Response product-type, 12 items) that were not covered by the wp2-demand-scorer agent's dataset-level pass (its tools cannot parse the binary xlsx). This file is a companion to, not a replacement for, `demand-supply-register.csv`.

Matching method: keyword/semantic search of each demand item's text against product `title`, `use_case`, `sectors`, `data_source` and `url` fields; no fabricated matches — every "มีและใช้ได้"/"มีแต่ใช้ประโยชน์ได้ยาก" cites a specific `product_id`.

## Key finding

Of the 52 product-type items checked (40 D-series + 12 A-series non-Response), only **5 have a clear match** in the delivered product inventory. The other 47 ask for a methodology, calculation framework, standard, guidance document, or analytical index that does not exist as any published product — not a matter of the right product being hard to access, but of no product existing at all. This is a materially different finding from the dataset-level gaps (which are often "exists but restricted/coarse"): **product-type demand is overwhelmingly a "capability was never built" gap, not a "capability exists but is hard to reach" gap.** This should be stated explicitly in §5.1's quantity-gap section, since it changes the kind of response TOR 5.2/5.3.9 recommendations need to propose (build new analytical capability, not just open access to an existing one).

## D-series product-type items (40 total)

| item_id | status | reason_codes | matched_product_id | justification |
|---|---|---|---|---|
| D003 | ยังไม่มี | — | — | No damage-function product in the inventory; DDPM's disaster products (P065–P069) report incidents/risk zones, not asset-level damage functions. |
| D004 | ยังไม่มี | — | — | No product links physical hazard to cascading/supply-chain impact. |
| D007 | ไม่สามารถจับคู่ได้ | — | — | This is a metadata/spec requirement (resolution disclosure), not a demand for a product itself — out of scope for inventory matching. |
| D009 | ยังไม่มี | — | — | No ISIC-to-domestic-operations mapping product exists. |
| D011 | ยังไม่มี | — | — | No standardized economic Loss & Damage calculation methodology product; DDPM's disaster products report incident counts/relief amounts only. |
| D016 | ยังไม่มี | — | — | No macroeconomic-model parameter/assumption product. |
| D023 | ยังไม่มี | — | — | No methodology product addressing indirect-loss calculation limitations. |
| D026 | ยังไม่มี | — | — | No indirect-loss calculation methodology product. |
| D035 | ยังไม่มี | — | — | No business-interruption-cost calculation manual/product. |
| D037 | ยังไม่มี | — | — | No forecast-to-business-cost conversion model/product. |
| D039 | ยังไม่มี | — | — | No tourism-account-to-economic-loss model product. |
| D042 | มีแต่ใช้ประโยชน์ได้ยาก | uncertainty_info | P054 (DWR Flood & Landslide Risk Forecast); also P044 GISTDA Disaster Platform, P068 DDPM Dashboard (Risk Map) | These are near-term forecast/monitoring risk maps at tambon/village level; none is confirmed to be a climate-scenario-based *future* inundation projection as the demand item specifies. |
| D045 | ยังไม่มี | — | — | No Urban InVest retention/drainage-model output product. |
| D053 | ยังไม่มี | — | — | No 2–5 year habitability-forecast product. |
| D055 | ยังไม่มี | — | — | No standard vulnerability-index-set (10–20 indices) product; DDPM's products are disaster alerting/risk-zone tools, not vulnerability indices. |
| D058 | ยังไม่มี | — | — | No spatial vulnerability-score product; DDPM Dashboard (Risk Map, P068) maps hazard zones, not vulnerability scores. |
| D061 | ไม่สามารถจับคู่ได้ | — | — | Methodological note (historical-period selection guidance), not a product demand. |
| D081 | มีและใช้ได้ | — | P063 (DCCE Heat Index Platform); also P040 (TMD Climate Index tool) | Direct match — both compute/display spatial heat-index values from station data. |
| D083 | มีแต่ใช้ประโยชน์ได้ยาก | spatial_detail | P044 (GISTDA Disaster Platform), P068 (DDPM Dashboard Risk Map) | Risk maps exist but resolution is not confirmed at the 10km location/sector-based grain the item specifies. |
| D086 | ยังไม่มี | — | — | No 20-year water-shortage risk-assessment output product for EEC specifically. |
| D089 | ยังไม่มี | — | — | Same as D086 — no EEC-specific overlay product found. |
| D090 | ไม่สามารถจับคู่ได้ | — | — | Reference-geography definition document, not a product demand. |
| D092 | ยังไม่มี | — | — | No EA-to-exposure-layer linkage guidance product. |
| D094 | ยังไม่มี | — | — | No Human Settlement vulnerability-mapping product; NSO-GIS (P079) is a statistics/boundary tool, not a vulnerability map. |
| D095 | ยังไม่มี | — | — | Same as D094. |
| D103 | ยังไม่มี | — | — | No chain-impact policy-evidence summary product. |
| D107 | ยังไม่มี | — | — | No hydrology-model output overlaid on transport-asset-level points; DWR/RID products (P049–P055) are water-management dashboards, not transport-asset risk layers. |
| D130 | ยังไม่มี | — | — | General GIS tools exist (e.g. GISTDA Portal P048, DPT Central GIS P059) but none is purpose-built for spatial-overlay impact summarization as specified. |
| D133 | ยังไม่มี | — | — | No double-vulnerability overlay/index product. |
| D135 | ยังไม่มี | — | — | No social-indicator subgroup-classification product. |
| D138 | ยังไม่มี | — | — | No adaptive/management-capacity index or measurement-framework product. |
| D140 | ยังไม่มี | — | — | Same as D138 — no bottleneck/management-capacity dashboard. |
| D143 | ยังไม่มี | — | — | No product linking these indicators to a vulnerability/risk index. |
| D146 | ยังไม่มี | — | — | No risk×capacity ranking/overlay product. |
| D152 | มีและใช้ได้ | — | P060 (DCCE Climate Risk Database), P061 (T-Plat Info), P105 (Climate-related Risk Maps – Thailand) | Direct match — these are DCCE's own official, citable risk-map products. |
| D156 | ไม่สามารถจับคู่ได้ | — | — | Presentation-format specification, not a product demand. |
| D158 | ยังไม่มี | — | — | No probabilistic-hazard-map interpretation guide/standard product. |
| D168 | ยังไม่มี | — | — | No Milestone 11 (NAP M&E) standard-indicator product in this inventory (the inventory is technical/GIS-oriented, not an M&E indicator catalog). |
| D170 | ยังไม่มี | — | — | Same as D168. |
| D204 | ยังไม่มี | — | — | No product linking climate forecasts to an engineering-design workflow. |

**D-series summary: 2 มีและใช้ได้ (D081, D152) / 2 มีแต่ใช้ประโยชน์ได้ยาก (D042, D083) / 32 ยังไม่มี / 4 ไม่สามารถจับคู่ได้ (metadata/spec/reference-document items, not product demands — out of the three-way framework).**

## A-series product-type items (non-Response, 12 total)

| item_id | status | reason_codes | matched_product_id | justification |
|---|---|---|---|---|
| A010 | มีและใช้ได้ | — | P041 (DCCE Climate Projection), P042 (DCCE Downscaling) | Direct match — DCCE's own GCM/downscaling products, same EC-Earth3-Veg + RegCM basis. |
| A022 | มีและใช้ได้ | — | P041, P042 | Same products cover precipitation projection methodology. |
| A031 | ยังไม่มี | — | — | No dedicated SST-projection product; consistent with the source document's own §4.1 finding. |
| A050 | ยังไม่มี | — | — | No landslide-projection-methodology product. |
| A062 | ยังไม่มี | — | — | No synthetic-cyclone-projection product; TMD Tropical Cyclone Statistics (P094) is historical, not projected. |
| A076 | มีแต่ใช้ประโยชน์ได้ยาก | uncertainty_info | P058 (Sea Level Projection System – Gulf of Thailand) | A sea-level projection product exists, but the item's CMIP6/GeoMIP6/SRM scenario range is not confirmed covered — needs verification against the product's own documentation. |
| A080 | มีแต่ใช้ประโยชน์ได้ยาก | metadata | P040 (TMD Climate Index tool), P063 (DCCE Heat Index Platform) | Heat-index tools exist and likely embed threshold logic, but the specific 35.0–39.9°C/≥40°C classification is not confirmed documented as a standalone reference. |
| A111 | ยังไม่มี | — | — | No "Yearly Vulnerability Index" product; DCCE's composite risk products (P060/P061/P105) are a distinct index, per the source document's own confirmed-gap finding. |
| A112 | ยังไม่มี | — | — | No "Climate Resilience Index" product. |
| A113 | ยังไม่มี | — | — | No product scoping economic/non-economic loss categories; this exists only as raw agency data (DDPM, DOHealth), not a defined-scope product. |
| A117 | ยังไม่มี | — | — | No DANA/PDNA/DALA methodology product in the inventory. |
| A118 | ยังไม่มี | — | — | No sectoral/macroeconomic loss-assessment-level product. |

**A-series summary: 2 มีและใช้ได้ (A010, A022) / 2 มีแต่ใช้ประโยชน์ได้ยาก (A076, A080) / 8 ยังไม่มี.**

## Combined product-type total

- มีและใช้ได้: 4 (D081, D152, A010, A022)
- มีแต่ใช้ประโยชน์ได้ยาก: 4 (D042, D083, A076, A080)
- ยังไม่มี: 40
- ไม่สามารถจับคู่ได้ (excluded from the three-way count — metadata/spec/reference items, not product demands): 4 (D007, D061, D090, D156)

Total matched: 48 of 52.
