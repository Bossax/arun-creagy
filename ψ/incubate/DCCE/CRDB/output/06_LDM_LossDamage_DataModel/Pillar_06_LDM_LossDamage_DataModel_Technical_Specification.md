# Pillar 06: LDM (Loss & Damage Model) Technical Specification

## 1. Executive Summary & Design Paradigm
The Loss and Damage Model (LDM) is structurally decoupled from traditional emergency response systems (which focus on immediate humanitarian relief and administrative compensation). This technical specification defines a relational database architecture modeled directly on the **World Bank's Damage and Loss Assessment (DaLA)** methodology, while fully aligning with the **NESDC (สภาพัฒน์ฯ) 5-Sector Reporting Standard**.

**Design Assumptions:**
- **Data Availability:** We assume that a robust `DISASTER_RECORD` (capturing precise hazard boundaries and human impacts during the event) is successfully collected. The pipeline gap analysis for achieving this data perfection is deferred to Pillar 5.3.7.
- **Exclusion of Administrative Compensation:** The model strictly isolates Economic Impacts (Damage and Loss). Administrative relief payments (เงินทดรองราชการ) are excluded from this analytical schema, as they do not represent true economic replacement costs or foregone revenues.
- **Relational Integrity:** The database enforces a strictly normalized `1-to-Many` relationship. One disaster event triggers multiple physical damage and economic loss assessments across various economic sectors.

---

## 2. Core Entity-Relationship (ER) Architecture

The DaLA methodology fundamentally separates **Asset Shocks (Damage)** from **Flow Shocks (Losses)**. The LDM Database reflects this dichotomy through three core interrelated tables:

1. **`DISASTER_RECORD` (The Incident Bounding Box):** Captures the spatial-temporal parameters of the natural hazard event.
2. **`LD_ASSET_DAMAGE` (Physical Destruction - Base Template):** Captures direct structural impacts evaluated at Replacement Cost.
3. **`LD_ECONOMIC_LOSS` (Flow Disruption - Base Template):** Captures post-disaster variations in economic flows (lost income, foregone production, higher operational costs) over a defined recovery horizon.

---

## 3. Data Dictionary and Table Schemas

### 3.1. `DISASTER_RECORD` (Table: Event Parameters)
This table acts as the primary key anchor. It expects fields collected *during* the disaster response phase.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `disaster_id` | VARCHAR(50) | **Primary Key**. Format: `{YYYY}-{HAZARD_CODE}-{PROVINCE}-{SEQ}` |
| `hazard_type` | ENUM | Based on NESDC: `Flood`, `Drought`, `Windstorm`, `Landslide`, `Cold Spells` |
| `start_date` | DATE | Date the hazard impact began |
| `end_date` | DATE | Date the hazard impact subsided |
| `duration_days` | INT | Automatically calculated. Critical for assessing flow losses (e.g., Flood Duration) |
| `location_code` | VARCHAR(10) | GIS / Administrative Boundary Code (Province, District, Sub-district) |
| `num_affected_pop` | INT | Total population directly and indirectly affected |
| `num_dead_missing` | INT | Official mortality and missing persons count |

### 3.2. `LD_ASSET_DAMAGE` (Table: Physical Asset Destruction - Base Template)
Captures the direct destruction of physical infrastructure and assets. Evaluated purely on the physical unit count multiplied by the unit replacement/repair cost (Constant Price).

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `damage_id` | VARCHAR(50) | **Primary Key**. |
| `disaster_id` | VARCHAR(50) | **Foreign Key** linking to `DISASTER_RECORD`. |
| `sector_id` | ENUM | NESDC Sectors: `Agriculture`, `Production`, `Housing`, `Infrastructure`, `Heritage` |
| `asset_type` | VARCHAR(100) | e.g., 'Single Detached House', 'Asphalt Road', 'Greenhouse Structure' |
| `qty_destroyed` | INT / FLOAT | Number of units completely destroyed (requiring full replacement) |
| `qty_damaged` | INT / FLOAT | Number of units partially damaged (requiring repair) |
| `unit_measure` | VARCHAR(20) | e.g., `households`, `kilometers`, `sq_meters`, `units` |
| `unit_replacement_cost` | DECIMAL(15,2) | Unit cost to rebuild/replace (Source: Bureau of Budget / VAT) |
| `unit_repair_cost` | DECIMAL(15,2) | Unit cost to repair partial damage |
| `monetary_damage_thb` | DECIMAL(18,2) | **Calculated:** `(qty_destroyed * replacement_cost) + (qty_damaged * repair_cost)` |

### 3.3. `LD_ECONOMIC_LOSS` (Table: Flow Disruption & Opportunity Costs - Base Template)
Captures the indirect economic consequences that occur *after* the disaster strikes. This includes lost revenue and unexpected expenditures necessary to maintain survival or business continuity.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `loss_id` | VARCHAR(50) | **Primary Key**. |
| `disaster_id` | VARCHAR(50) | **Foreign Key** linking to `DISASTER_RECORD`. |
| `sector_id` | ENUM | Must match the `sector_id` taxonomy defined above. |
| `loss_category` | ENUM | `Foregone_Revenue`, `Yield_Reduction`, `Increased_Op_Cost`, `Emergency_Expense` |
| `qty_affected_units` | INT / FLOAT | e.g., `Affected Households` (paying rent), `Rai of Crop` (lost yield) |
| `baseline_projection` | DECIMAL(15,2) | Expected production/revenue in a *Counterfactual (No-Disaster)* scenario |
| `actual_post_disaster` | DECIMAL(15,2) | Actual observed production/revenue after the hazard |
| `increased_costs_thb` | DECIMAL(15,2) | e.g., Higher living costs (rent), buying expensive animal feed |
| `monetary_loss_thb` | DECIMAL(18,2) | **Calculated:** `(baseline - actual) + increased_costs` |

---

## 4. Sectoral Assessment Workflows (NESDC Alignment)

To ensure this database fulfills the NESDC's dashboard requirements, the data ingestion must satisfy the specific calculation logics per sector:

### 4.1. Housing Sector (ด้านที่อยู่อาศัย)
*   **Asset Damage:** `qty_destroyed` (บ้านพังทั้งหลัง) × `unit_replacement_cost` (ราคาประเมินบ้านใหม่)
*   **Economic Loss:** `qty_affected_units` (จำนวนครัวเรือน) × `increased_costs_thb` (ค่าเช่าบ้านชั่วคราวระหว่างซ่อมแซม)

### 4.2. Agriculture Sector (ภาคเกษตรกรรม)
*   **Asset Damage:** Destruction of physical farming infrastructure (e.g., โรงเรือน, บ่อเลี้ยงปลา, ระบบน้ำหยด).
*   **Economic Loss:** `qty_affected_units` (พื้นที่เพาะปลูกเสียหาย/ไร่) × `baseline_projection` (ผลผลิตต่อไร่ในภาวะปกติ) × ราคาตลาดหน้าฟาร์ม.

### 4.3. Infrastructure Sector (สาธารณูปโภค)
*   **Asset Damage:** `qty_destroyed` (กิโลเมตรของถนนที่ขาด / เสาไฟฟ้าล้ม) × Cost to rebuild.
*   **Economic Loss:** Foregone revenue for state enterprises (e.g., การไฟฟ้า/การประปาขาดรายได้) and increased transportation costs for the public due to detours.

---

## 5. Policy & Operational Implementation (Data Collection Directives)
While the database assumes fields are populated, achieving this requires a strict operational directive for the **During-Disaster (Response) Phase**:
*   The Department of Disaster Prevention and Mitigation (DDPM) must enforce the collection of precise **Geospatial Boundaries (Location Codes)** and **Temporal Duration (`start_date`, `end_date`)** during emergency response.
*   These baseline variables are mandatory prerequisites. Without an accurate `DISASTER_RECORD` acting as the Bounding Box, subsequent sectoral ministries (Agriculture, Transport, etc.) cannot anchor their Post-Disaster DaLA assessments to the relational database.

---

## 6. Sector-Specific Schema Extensions (Pending Detail)
The templates for `LD_ASSET_DAMAGE` and `LD_ECONOMIC_LOSS` represent the baseline conceptual schemas. It is explicitly noted that these tables will be extended into granular, normalized child tables (e.g., `LD_AGRI_CROP_LOSS` for crop yields, farm-gate prices, and farmer debt tracking; and `LD_HOUSING_DAMAGE` for structural replacement specs) in subsequent design sessions.

Detailed specifications for these extensions are currently pending and will be integrated upon receipt of further sectoral definitions.
