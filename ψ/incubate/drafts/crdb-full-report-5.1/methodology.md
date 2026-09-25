# §5.1 Gap analysis method: reference

**Status**: working reference, 2026-09-25. Written after Boss's review of `draft-v2.md` found that the opening method paragraph and §5.1.1 explain nothing concrete (no clear *what*, *why*, or *how*). Every fact below was checked against the source files named in each section. The rewrite of §5.1's opening and §5.1.1 should be built from this file, not from `argument-map.json` units open-01/open-02/dem-01..03, which carry the old framing.

---

## 1. What the analysis has to answer

TOR 5.3.8, verbatim (Thai original, `inbox_source/260106_DCCE_Climate risk database_inception report_vfinal.md` line 295):

> วิเคราะห์ช่องว่างระหว่างอุปทานและอุปสงค์ของข้อมูล โดยการนำผลการสังเคราะห์ความต้องการใช้ข้อมูล มาเปรียบเทียบกับบัญชีรายการผลิตภัณฑ์ข้อมูลสารสนเทศและชุดข้อมูลที่มีอยู่ เพื่อวิเคราะห์หาช่องว่าง (Gap Analysis) ทั้งในเชิงปริมาณ (ข้อมูลที่ยังขาด) และเชิงคุณภาพ (ข้อมูลที่มีแต่ใช้ประโยชน์ได้ยาก)

The clause fixes the two sides and the two outputs.

| Element | What it is in this project | Size |
|---|---|---|
| Demand (อุปสงค์) | Synthesized data needs. Source 1 is the consultation use cases from TOR 5.3.2–5.3.3 (`output/archive/consultation_workshop/user_use_case_raw.md`). Source 2 is DCCE's own reporting obligation for the adaptation chapter of Thailand's Biennial Transparency Report (A-BTR), which DCCE must fill whether or not any other agency asks for the data (Boss-approved second source, plan-slice §3). | 83 use cases, 122 A-BTR signals |
| Supply, datasets (อุปทาน) | Baseline Data Inventory, TOR 5.3.5 (`output/02_Data_Inventory/data_catalog_v4.csv`) | 260 datasets, 44 agencies |
| Supply, products (อุปทาน) | Information Product Inventory, TOR 5.3.4 (`output/03_Data_Product_Inventory/260904_TOR5.3.4_Information Product Inventory.xlsx`) | 114 products, 56 agencies |
| Output 1 | Quantity gap (ข้อมูลที่ยังขาด): a need that no inventory entry covers | |
| Output 2 | Quality gap (ข้อมูลที่มีแต่ใช้ประโยชน์ได้ยาก): a need that an inventory entry covers, but the user cannot put the entry to work | |

So the analysis answers three concrete questions, in order:

1. **What exactly do users need?** A list of specific data needs, each one small enough to look up in an inventory.
2. **For each need, does an inventory entry exist?** Answered by searching the inventory that holds that kind of thing.
3. **If an entry exists, can the user use it? If not, why not?** Answered by checking the entry's recorded access, resolution, format, currency, metadata, and uncertainty information against what the need requires.

---

## 2. Why the method takes this shape

### 2.1 Why break use cases into single needs first

A use case is a story about a task. For example, a commercial bank wants to price flood risk into a mortgage portfolio. One story contains several separate data needs: a flood probability map at asset level, flood depth and duration, damage functions that convert depth into asset loss, and so on. An inventory entry is one dataset or one product. A story cannot be looked up in an inventory; a single need can. So step 1 turns 83 stories into 238 needs, each tied to the agency that asked and to the line in the interview record where the need appears.

### 2.2 Why sort needs into TOR 5.3.5's 8 categories

TOR 5.3.5 tells the consultant to organize the Baseline Data Inventory "ตามกรอบการประเมินความเสี่ยงที่เป็นมาตรฐานสากล" and lists 8 categories (inception report lines 272–292). Sorting the demand side into the same 8 categories does two jobs.

- **It gives each need a starting place to search.** The catalog has its own sub-domain field (`cdm_sub_domain`). Each TOR category maps to one or more sub-domains (§3.4), so the search for a Hazard need starts in the catalog's HAZARD rows.
- **It lets the committee read the results in the TOR's own structure.** Gap counts per category show which kinds of information are thin, in the categories the TOR itself named.

### 2.3 What the 8 categories actually cover

The 8 categories are **categories of information**, grouped the way a risk assessment uses them. They are not all components of risk. Under the IPCC risk concept, risk comes from hazard, exposure, and vulnerability together, and vulnerability combines sensitivity with limited capacity to cope and adapt *(verify the exact IPCC AR5/AR6 citation before quoting it in report prose)*. Read against that concept, TOR 5.3.5's 8 categories fall into three groups.

| Group | TOR 5.3.5 categories | What the information describes | Catalog `cdm_domain` that holds it |
|---|---|---|---|
| A. The conditions that make up future risk | Climatic Driver, Hazard, Exposure, Sensitivity, Adaptive Capacity | Climate conditions, the damaging events they cause, what stands in harm's way, how easily it is harmed, and how well it can cope | FORWARD-LOOKING |
| B. What has already happened | Impact, Loss and Damage | Records of past events and their effects, and the losses and damages measured from them | IMPACT_(BACKWARD-LOOKING) |
| C. What is being done about it | Response | Measures taken to manage risk | ADAPTATION_PLANNING |

The catalog's own top-level field `cdm_domain` already uses this three-way split (plus SPATIAL_UNIT for reference boundaries), so the grouping comes from the supply side's own structure and is not an invented framework.

**Terminology decision (see §7, D1)**: the draft's "องค์ประกอบความเสี่ยง 8 ด้าน" is our own label and it is wrong for Climatic Driver, Impact, Loss and Damage, and Response. Proposed replacement: **"หมวดข้อมูล 8 หมวดตามขอบเขตงานข้อ 5.3.5"**, which uses the TOR's own verb (จัดหมวดหมู่). The critique's alternative "ห่วงโซ่คุณค่าข้อมูลสภาพภูมิอากาศ (Climate Data Value Chain)" does not appear in the TOR or the catalog. Describe the three groups in plain Thai instead of naming a framework.

### 2.4 Why three statuses instead of yes/no

TOR 5.3.8 asks for quality gaps as well as quantity gaps, so "an entry exists" has to be split into "usable" and "hard to use". Each hard-to-use verdict carries a reason code, because §5.2 needs to know *what kind* of fix each gap calls for: opening access is a different action from writing metadata or collecting finer-resolution data.

### 2.5 Why datasets and products are matched separately

A dataset need asks for data the user will analyze themselves (rainfall records, a population grid). A product need asks for a finished output that answers a question directly (a risk map, a vulnerability index, a damage function, a calculation method, a dashboard). The TOR keeps these in two inventories (5.3.4 products, 5.3.5 datasets), so each need is searched in the inventory that holds its type.

---

## 3. How the method is applied, step by step

### Step 1. Itemize the needs

- **Rule**: one need = one thing a user would look up in an inventory: one variable or dataset, or one product. Each need records the requesting agency and the source line.
- **Output**: 238 needs from 83 use cases (D001–D238, `demand-items-extracted.md`) and 122 needs from the A-BTR (A001–A122, `demand-items-abtr.md`). Total 360.

### Step 2. Sort each need on three questions

**2a. Is it a data content need or a system need?** *(This cut is new. Phase A did not make it explicitly. See §5.)*

| Layer | Decision rule | Examples from the register | Where it goes |
|---|---|---|---|
| Data content need | Names a variable, dataset, map, index, statistic, or analytical output | D001 probabilistic flood map at asset level; A007 SSP2-4.5/SSP5-8.5 scenario data | Steps 2b–4, matched against an inventory |
| System need | Asks for how data is organized, described, shared, or delivered: a catalog, portal, API, metadata or format specification, data-sharing arrangement, or coordination mechanism | D007 resolution-disclosure spec; D090 reference-geography definition; A004 national climate information platforms; the Group 5 catalog/portal/API requests (D148–D238 range) | Counted and described in §5.1.1; carried to §5.2 and to the data management framework (Chapter 2). Not matched against the dataset or product inventories, because those inventories list data, not system features. |

**2b. Which of the 8 categories?** (data content needs only; classify by what the user wants to know)

| Category (TOR 5.3.5 definition) | Decision rule | Register examples | Boundary rule |
|---|---|---|---|
| Climatic Driver: ปัจจัยหลักที่มีอิทธิพลต่อสภาพอากาศและภัย | The climate variable itself, observed or projected: temperature, rainfall, sea-surface temperature, sea level, scenario pathways, downscaled projections | A007 scenario pathways; A006 national-platform climate variables | A threshold index of a climate variable (e.g. days above a temperature) is Climatic Driver when the user wants the variable; it is Hazard when the user wants where or how often a damaging event occurs |
| Hazard: ข้อมูลภัยพิบัติต่างๆ | A potentially damaging event or condition: its extent, depth, duration, frequency, or probability (flood, drought, heatwave, landslide, storm surge) | D001 flood probability at asset level; D002 flood depth and duration | See Climatic Driver |
| Exposure: ตำแหน่งและปริมาณของคน/ทรัพย์สินที่อาจได้รับผลกระทบ | Location and quantity of people, assets, infrastructure, land use | A001 population and urbanization baseline | Exposure says *what is there*; Sensitivity says *how easily it is harmed* |
| Sensitivity: คุณลักษณะของระบบ/ประชากรที่ได้รับผลกระทบได้ง่าย | Characteristics that make people or systems easier to harm: age, income, health, disability, building type, crop type | A002 population groups with heightened vulnerability; D048/D051 MSDHS vulnerable-population registry | Sensitivity describes susceptibility; Adaptive Capacity describes resources to cope |
| Adaptive Capacity: ศักยภาพเชิงกายภาพ เศรษฐกิจ และสังคมในการรับมือ | Resources and institutions that help people cope or adapt: savings, insurance, debt position, services, institutional capacity | D144/D146 NXPO institutional resilience index; D141 household debt and asset ownership (dual-tagged) | See Sensitivity |
| Impact: ข้อมูลความเสียหายและความสูญเสียที่เกิดขึ้น | Records of past events and their effects on people, sectors, and places: event records, counts of people affected, sectoral impact studies | D013 event-level flood impact for economic zones | **Proposed rule (§7, D3)**: Impact = what happened and to whom. Loss and Damage = the loss or damage measured or valued under a standard accounting method. The TOR's own definitions overlap, so this rule needs Boss's confirmation. |
| Loss and Damage (8th TOR item, no definition given) | Losses and damages measured or valued: direct asset damage, indirect losses, non-economic losses | D012 losses beyond compensation payouts; D014 direct asset damage estimates | See Impact |
| Response: ข้อมูลมาตรการที่ใช้เพื่อจัดการความเสี่ยง | Data about measures taken: adaptation projects, early-warning coverage, insurance coverage, budget spent on risk reduction | To be identified in the re-sort (§7, D2) | Data *about* measures belongs here. A request for a *system feature* is a system need (2a). |

**2c. Dataset or product?**

- Dataset: data the user will analyze themselves.
- Product: a finished output that answers a question (map, index, report, dashboard, model, method, damage function).

### Step 3. Search the matching inventory

- Dataset needs are searched in the Baseline Data Inventory (260 rows); product needs in the Information Product Inventory (114 rows).
- The search **starts** in the catalog sub-domain(s) mapped to the need's category (table below) and **extends to the whole catalog** when the content fits a row filed elsewhere. The catalog owner's taxonomy does not always follow the TOR's categories. In Phase A, Hazard needs matched 21 rows filed under CLIMATE_DRIVER, and Exposure needs matched 3 SPATIAL_UNIT rows.
- Fields read for each candidate row: `title`, `cdm_sub_domain`, `data_type`, `spatial_resolution`, `time_period_start/end`, `access_rights_dataset`, `use_limitations`, `update_frequency_unit`, `notes`. Self-assigned tags (`tag_string`, `high_value_dataset`, `data_category`) may corroborate a match but never establish one.
- **Evidence rule**: every "exists" verdict cites a `dataset_id` or `product_id`. No citation, no match.

**Crosswalk: TOR category → catalog sub-domain (starting search pool)**

| TOR 5.3.5 category | Catalog `cdm_sub_domain` | Catalog rows |
|---|---|---|
| Climatic Driver | CLIMATE_DRIVER | 49 |
| Hazard | HAZARD | 36 |
| Exposure | EXPOSURE, SPATIAL_UNIT | 68 + 3 |
| Sensitivity | VULNERABILITY (merged) | 72 |
| Adaptive Capacity | VULNERABILITY (merged) | (same 72) |
| Impact | DISASTER_RECORD, LOSS_&_DAMAGE | 2 + 11 |
| Loss and Damage | LOSS_&_DAMAGE, DISASTER_RECORD | 11 + 2 |
| Response | RESPONSE | 4 |
| *(no TOR category)* | RISK_METRIC, COMPOSITE_INDEX | 5 + 10 |

Two supply-side facts come straight out of this table and belong in the report as findings. First, the catalog merges Sensitivity and Adaptive Capacity into one VULNERABILITY tag, so it cannot show which side it covers. Second, the catalog holds combined risk outputs (RISK_METRIC, COMPOSITE_INDEX) that have no slot among the TOR's 8 categories (see §7, D4).

### Step 4. Assign a status

Decision tree, applied to each data content need:

1. No inventory entry covers the need → **ยังไม่มี**
2. An entry covers the need and no barrier below applies → **มีและใช้ได้**
3. An entry covers the need and at least one barrier applies → **มีแต่ใช้ประโยชน์ได้ยาก**, with every applicable reason code

| Reason code | Thai label | Triggered when | Catalog field checked |
|---|---|---|---|
| access | การเข้าถึง | The entry is restricted or available only on request, so the requesting agency cannot obtain it in practice | `access_rights_dataset` |
| metadata | ข้อมูลอธิบายชุดข้อมูล | Source, method, or conditions of use are not documented well enough for the user to judge fitness for use | `notes`, `use_limitations`, empty descriptive fields |
| spatial_detail | ความละเอียดเชิงพื้นที่ | Resolution is coarser than the need (e.g. province where the need is tambon or asset level) | `spatial_resolution` |
| format | รูปแบบข้อมูล | Published in a form the user cannot analyze (view-only web page, scanned report) | `data_format` |
| update_currency | ความทันสมัย | Time period or last update too old for the need | `time_period_end`, `update_frequency_unit`, `last_updated_date` |
| uncertainty_info | ข้อมูลความไม่แน่นอน | No error range or model assumptions given for data the user must weigh | `use_limitations`, `notes` |
| certification | การรับรองคุณภาพ | Defined, but **0 hits**: every catalog row shares `endorsement_status=Baseline-Draft` / `validation_flag=Unverified-Baseline`, so Phase A treated this as a caveat on the whole catalog. State it once as a catalog-wide condition, not as a reason code. |

**A-BTR needs** reuse the item-by-item catalog matching already done in the A-BTR requirement analysis (§4.1 of `wp2-data-domain-highlight-draft.md`), translated by a fixed rule: Direct match with no caveat → มีและใช้ได้; Direct or Partial match with a caveat → มีแต่ใช้ประโยชน์ได้ยาก; Inferred match → มีแต่ใช้ประโยชน์ได้ยาก, flagged; No match → ยังไม่มี (`counts.md` methodology note 2).

### Step 5. Count and report

Counts per category × status (Table 5-2 datasets, Table 5-3 products), reason codes per category (for §5.1.4), and the funnel below (candidate content for Figure 5-1).

---

## 4. The numbers at each step (reconciled)

| Step | D-series (use cases) | A-series (A-BTR) | Total | Source |
|---|---|---|---|---|
| 1. Needs itemized | 238 | 122 | **360** | `demand-items-extracted.md`, `demand-items-abtr.md` |
| 2. Tagged "Response" and set aside in Phase A | 125 | 21 | **146** | same |
| 3. Matched against an inventory | 113 | 101 | **214** | `counts.md` |
| of which dataset needs → Baseline Data Inventory | 73 | 89 | **162** | `counts.md` |
| of which product needs → Information Product Inventory | 40 | 12 | **52** | `product-matches.md` |

| Result | Datasets (162) | Products (52) | Total (214) |
|---|---|---|---|
| มีและใช้ได้ | 4 | 4 | 8 |
| มีแต่ใช้ประโยชน์ได้ยาก | 113 | 4 | 117 |
| ยังไม่มี | 45 | 40 | 85 |
| ไม่สามารถจับคู่ได้ | — | 4 | 4 |

**Errors in the current draft and plan-slice that this table corrects:**

1. **"266 matched items" is a double count.** 214 already includes the 52 product needs; plan-slice §2 added them again. The correct total is **214** (8 + 117 + 85 + 4 = 214). This resolves editorial finding F1.
2. **Draft §5.1.2 calls the 214 "รายการความต้องการประเภทชุดข้อมูล".** The 214 are datasets *and* products. Dataset needs are 162.
3. **The 4 "ไม่สามารถจับคู่ได้" items (D007, D061, D090, D156) are specifications, not products**: a resolution-disclosure spec, a guidance note on choosing the historical period, a reference-geography definition, and a presentation format. Under Step 2a they are system needs and leave the matched set. The status "ไม่สามารถจับคู่ได้" then disappears from the tables, and the matched content needs become 210 (8 / 117 / 85). This also answers the cold reader's question about what separates "ยังไม่มี" from "ไม่สามารถจับคู่ได้".

**File-level discrepancies to fix before the register goes into the appendix:**

4. `demand-supply-register.csv` has **211 rows** (110 D + 101 A; 49 product rows). `counts.md` and `product-matches.md` cover 113 D and 52 products. Three D-series product rows are missing from the CSV.
5. A-series type split: the tagging file gives 85 dataset / 16 product among non-Response items; the register gives 89 / 12. Four items changed type between the two files without a note.
6. 9 register rows have more columns than the header (unquoted commas in text fields). The CSV needs repair before anyone opens it in a spreadsheet.

---

## 5. What Phase A did differently, and what that means for the prose

| Phase A as executed | Consequence | Fix in this method |
|---|---|---|
| Category tags were "this analyst's best-guess reading of the item text" (`demand-items-extracted.md` header), with no written rules | The report cannot explain how a need was classified. This is the gap Boss found in the opening method paragraph. | Decision rules in Step 2b. The rules need a check against the existing tags (§7, D5). |
| "Response" served as a catch-all for governance, catalog, portal, and platform requests (118 of the 125 D-series Response items are product-type asks) | Two different things share one label: TOR's Response category (data about measures) and system needs. All 146 were then set aside, so the catalog's 4 RESPONSE rows were never compared with any need, and Tables 5-2/5-3 show 7 of TOR's 8 categories. | Step 2a separates system needs first; genuine Response data needs are matched like any other category (§7, D2). |
| Specification requests were typed as products | The unexplained "ไม่สามารถจับคู่ได้" status | Step 2a |
| Impact and Loss and Damage were not separated by a rule (Impact needs matched LOSS_&_DAMAGE rows 5 times; L&D needs matched DISASTER_RECORD rows 2 times) | The Impact and L&D rows in Table 5-2 are not comparable with each other | Proposed boundary rule in Step 2b (§7, D3) |

---

## 6. What this changes in §5.1

**Opening, method paragraph.** Replace the four vague steps with the structure of this file, in the reader's order:
1. The question the TOR asks (§1), in one or two sentences with the TOR quote.
2. Why needs must be itemized before they can be compared (§2.1), with the bank example.
3. Why the 8 TOR categories, and what they cover in three groups (§2.2–2.3). This is where the terminology change lands.
4. How a need is classified and how status is decided (§3), with the decision-rule table and reason-code table as report tables, explained in prose before each table.
5. Figure 5-1 as a **funnel with the real numbers** (360 → system needs set aside → 210 content needs → 162 datasets / 48 products → statuses), replacing the current four-box placeholder.

**§5.1.1.** Describe demand in two layers from the first paragraph: data content needs, classified into the 8 categories, and system needs, counted and described in their own paragraph with a pointer to §5.2 and Chapter 2. Table 5-1 should show **all 360 needs** by layer × category × type, so the reader sees the whole demand before the funnel narrows it. The current Table 5-1 shows only the 162 matched dataset needs, which hides both the products and the system needs.

**Whole section.** Replace "องค์ประกอบความเสี่ยง" everywhere (prose, table headers, `argument-map.json`, `writing-contract.json`) with the term Boss picks in D1. Fix counts per §4.

---

## 7. Decisions needed from Boss

| # | Decision | Recommendation | Effort if yes |
|---|---|---|---|
| D1 | Term for the 8 categories | "หมวดข้อมูล 8 หมวดตามขอบเขตงานข้อ 5.3.5", with the three groups described in plain Thai. Skip "ห่วงโซ่คุณค่าข้อมูล", which has no source in the TOR or the catalog. | Terminology pass on the draft, map, and contract |
| D2 | Re-sort the 146 "Response" items into system needs and genuine Response data needs, and match the latter against the catalog | Yes. Without it, the TOR's 8th category has no result and the system-need count is not defensible. | Reopens Phase A for 146 items; the Response data subset is probably small |
| D3 | Impact vs Loss and Damage boundary rule (Step 2b) | Adopt the proposed rule and re-check the 49 items tagged Impact or L&D (D-series 16 + 10, A-series 9 + 14) | Re-tag and re-count 49 items |
| D4 | Needs for combined risk outputs (risk maps, risk indices) have no TOR category | Treat them as product needs and report them as their own row in the product table, labelled as outside the TOR's 8 categories | Small; identify the items |
| D5 | Check the existing category tags against the written rules | Spot-check a sample from each category; full re-tag only if the sample shows many disagreements | Sample of ~30–40 items |
| D6 | Repair the register CSV (211 vs 214 rows, 9 malformed rows, A-series type split) | Yes, before it goes in the appendix | Small |
