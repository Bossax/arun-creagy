# Data Medallion: Bronze Layer (Raw Data Sources)
Location: `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/`

This layer contains immutable, raw source files used as the foundation for the CRI Phase 1 Impact Index.

---

## 1. BMA (Bangkok Metropolitan Administration)
- **Source:** BMA direct file transfer
- **File**: `สถิติข้อมูลอุทกภัย ภัยแล้ง ดินถล่ม และวาตภัย ในพื้นที่กรุงเทพมหานคร_BMA.xlsx`
- **Description**: Multi-hazard disaster statistics for Bangkok districts.
- **Role**: Capital-specific impact metrics.
- **Comments:** Data is sparse; definitions differ from national DDPM disaster declarations.

---

## 2. DDPM (Dept of Disaster Prevention & Mitigation / กรมป้องกันและบรรเทาสาธารณภัย)
- **Source:** DDPM direct file transfer
- **Village Disaster Statistics (2557 - 2567)**:
  - Individual yearly CSVs: `2557 - สถิติการเกิดสาธารณภัยรายหมู่บ้าน.csv` to `2567 - สถิติการเกิดสาธารณภัยรายหมู่บ้าน.csv`.
  - **Contents**: Granular village-level (`Moo`) impact data (house damage, casualties, affected households).
- **Financial Relief**:
  - **File**: `สถิติข้อมูลการใช้จ่ายเงินทดรองราชการ ปี 2546 - ปัจจุบัน.xlsx`
  - **Description**: Provincial-level emergency fund spending records.
- **Wildfire Data (2026-07-16 Bundle)**:
  - **File**: `0_bronze/2026-07-16-cri-proj-data/Wildfire_hh_data.csv`
  - **Contents**: Sub-district level wildfire affected households and casualty statistics across 2560–2567.
  - **Processing Script**: [`script/ELT/build_gold_wildfire_ddpm_fact.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_wildfire_ddpm_fact.py)

---

## 3. DOPA (Dept of Provincial Administration / กรมการปกครอง)
- **`ccaatt.xlsx`**: Master administrative code sequential file (Province-District-Subdistrict).
  - **Source:** https://stat.bora.dopa.go.th/stat/statnew/statMenu/newStat/ccaa.php
  - **Description**: Official sovereign hierarchy mapping 2-digit Province, 2-digit District, 2-digit Subdistrict codes.
- **`code_village_dopa_2019.xls`**: High-resolution village code master list (2019 vintage).
- **Administrative Shapefiles**:
  - **Source:** https://drive.google.com/drive/folders/1zi3Z0l7wvsGN1p5YIWVVL3LFs3WnS7VQ
  - **Files**: `thailanda-administrative-boundary/*.shp`

---

## 4. CRI Project Data Bundle (2026-06-12 Multi-Agency Bundle)
Location: `0_bronze/2026-06-12_cri_proj_data/`

* **Population & Households**:
  - **Workbook**: `CRI Data - Population.xlsx`
  - **Extracted Intake CSVs**: `population_extracts/pop67.raw.csv`, `pop60-67.raw.csv`
  - **Agency Owner**: **DOPA (กรมการปกครอง)**
* **Economic GPP**:
  - **Workbook**: `CRI Data - GPP.xlsx`
  - **Extracted Intake CSVs**: `gpp_extracts/gpp-67.raw.csv`, `gpp-60-67.raw.csv`
  - **Agency Owner**: **NESDC (สภาพัฒน์ / Office of the National Economic & Social Development Council)**
* **Government Advance Financial Relief**:
  - **Workbook**: `CRI Data - Government_Advanced_Payment.xlsx`
  - **Extracted Intake CSVs**: `govt_adv_payment_extracts/govt_adv_payment-*.raw.csv`
  - **Agency Owner**: **Ministry of Finance (กค. / CGD) & DDPM (ปภ.)**
* **Extreme Heat Casualties**:
  - **Workbook**: `CRI Data - Heatwave.xlsx`
  - **Extracted Intake CSVs**: `heatwave_extracts/heatwave.raw.csv`
  - **Agency Owner**: **Department of Health (DOH / กรมอนามัย, Ministry of Public Health)**

---

## 5. Excluded Data Sources
- **WorldPop Dasymetric Population Grid**: Evaluated in exploratory research notebooks (`pillar1_comparative_dasymetric_analysis.ipynb`) but **excluded from production CRI pipelines**. All demographic multipliers strictly use official DOPA subdistrict population & household counts.
