---
traceId: 462e5595-048a-43d6-80b9-032d4eef4076
query: what are data fields of government advancement payment datasets?
date: 2026-06-26
---

# Trace: what are data fields of government advancement payment datasets?

## Search Waves Findings

### Wave 1 (Oracle Hybrid Search) & Wave 2 (File Grep)
The trace revealed that the term "government advancement payment" is actually recorded in the project as **"Government Advance Payment"** (เงินทดรองราชการ). 

**Key Findings:**
1. **Terminology Shift**: A global terminology refactor was completed across the repository (e.g., `C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/2026-06-15_Phase1-vs-Pilot-Comparison-Plan.md`, `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/handoff/2026-06-15_18-00_terminology-and-analytical-update.md`) changing "Total Economic Loss" / "Eco-Loss" to "Government Advance Payment" (Relief Fund). 
2. **Data Context**: This data stream comes from the **DDPM (Department of Disaster Prevention and Mitigation)** and represents a secondary administrative public-finance response proxy, not a direct measure of total economic loss. It is an emergency budget used for immediate relief, historically capped (e.g., 20 million baht per province per disaster declaration).
3. **Primary Data Fields Identified**:
   The actual parsed master files broken down from the workbook are **`master_financial_relief_by_hazard.csv`** and **`master_financial_relief_by_sector.csv`** in the Silver layer (`C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/`).
   
   *   **By Hazard (`master_financial_relief_by_hazard.csv`)**:
       *   `จังหวัด` (Province)
       *   `ปี` (Year - Buddhist Era, e.g., 2568)
       *   **Hazards (Values in THB)**: `อุทกภัย` (Flood), `ภัยแล้ง` (Drought), `ฝนทิ้งช่วง` (Dry Spell), `ภัยหนาว` (Cold Spell), `อัคคีภัย` (Fire), `วาตภัย` (Windstorm), `โรคศัตรูพืช` (Plant Pests/Disease), `โรคระบาดสัตว์` (Animal Epidemic), `ภัยอื่น` (Other)
       *   **Budgeting Metrics (Values in THB)**: `รวมทั้งสิ้น` (Total), `วงเงินเสนอ` (Proposed Budget), `วงเงินอนุมัติ` (Approved Budget), `วงเงินไม่อนุมัติ` (Unapproved Budget)
   
   *   **By Sector (`master_financial_relief_by_sector.csv`)**:
       *   `จังหวัด` (Province)
       *   `ปี` (Year)
       *   **Sectors (Values in THB)**: `ด้านดำรงชีพ` (Livelihood), `ด้านสังคมสงเคราะห์` (Social Welfare), `ด้านการแพทย์และสาธารณสุข` (Medical/Public Health), `ด้านเกษตร_พืช` (Crops), `ด้านเกษตร_ประมง` (Fisheries), `ด้านเกษตร_ปศุสัตว์` (Livestock), `ด้านเกษตร_อื่น` (Other Agriculture), `ด้านบรรเทาสาธารณภัย` (Disaster Relief), `ด้านการปฏิบัติงานบรรเทาทุกข์` (Relief Operations), `เชิงป้องกันหรือยับยั้ง` (Prevention/Inhibition)
       *   **Budgeting Metrics (Values in THB)**: `รวมทั้งสิ้น` (Total), `วงเงินเสนอ` (Proposed), `วงเงินอนุมัติ` (Approved), `วงเงินไม่อนุมัติ` (Unapproved)

### Wave 3 (Session Digging)
Session mining confirmed the strategic pivot regarding "Audit-to-Asset" traceability and highlighted the importance of distinguishing between evidence and deliverable artifacts, which resonates with the conceptual shift from calling this "Total Economic Loss" (a conceptual deliverable/claim) to accurately labeling it "Government Advance Payment" (the empirical evidence).

---

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: The need to accurately label and standardize disaster financial relief metrics without conflating them with true economic loss measurements.
- **[E] Supporting Evidence**: 
  - `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_hazard.csv`
  - `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_sector.csv`
  - `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/methodology.py`
  - `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_CRI_to_CRDB_MVD_gap_analysis.md`
  - `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/2026-06-18_in-ddpm-datasets-total-economic-loss-is-often-j.md`
- **[D] Potential Decision**: Enforce a strict boundary in the semantic data model between "Response-Finance Proxies" (like Government Advance Payments) and "Total Economic Damage", ensuring all economic loss ratios account for the 1,000,000x THB to Million THB scaling difference.
- **[A] Target Asset**: Data dictionaries, metadata tracking sheets (e.g. `cri-data-govt-adv-payment.definition.md`), and dashboard methodology pages.
