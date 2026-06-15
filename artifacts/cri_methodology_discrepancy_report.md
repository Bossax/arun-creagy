# CRI Methodology Comparison Report: Pilot vs. Phase 1 Discrepancy Analysis

## 1. Executive Summary

This report outlines the quantitative findings from reproducing and comparing the Climate Risk Index (CRI) rankings between the **TEI Pilot Phase** and **DCCE Phase 1**. 

The analysis reveals **massive shifts in provincial vulnerability rankings** (e.g., Nakhon Ratchasima dropping 59 ranks, Chaiyaphum dropping 48 ranks). The quantitative audit proves that these shifts are not random, but are mathematically driven by a fundamental change in the proxy used to measure **Economic Loss**, compounded by differences in the **GPP Denominator** provided in the pilot data.

## 2. Key Driver: The Economic Loss Proxy (Numerator)

The most significant driver of the discrepancy is the shift in the data source for `Loss_abs`:
*   **Pilot (OAE):** Relied on agricultural compensation data. In rural/agricultural provinces, these values can be massive because crop damage covers vast geographic areas and is uncapped in nature.
*   **Phase 1 (DDPM):** Relied on "เงินทดรองราชการ" (Government Advance Payment). This is an emergency budget used for immediate relief, which is historically capped (e.g., typically 20 million baht per province per disaster declaration). 

### Evidence of Collapse in Economic Loss
When transitioning from the uncapped agricultural proxy to the capped administrative proxy, the absolute loss values collapsed by over 90% for the most impacted provinces:

| Province (จังหวัด) | Pilot Loss (OAE) | Phase 1 Loss (DDPM) | % Difference | Rank Shift |
| :--- | :--- | :--- | :--- | :--- |
| **นครราชสีมา (Nakhon Ratchasima)** | 794.7 M Baht | 7.0 M Baht | -99.1% | -59 places |
| **ชัยภูมิ (Chaiyaphum)** | 652.8 M Baht | 6.6 M Baht | -98.9% | -48 places |
| **ขอนแก่น (Khon Kaen)** | 554.2 M Baht | 22.6 M Baht | -95.9% | -24 places |
| **นครสวรรค์ (Nakhon Sawan)** | 367.4 M Baht | 4.4 M Baht | -98.7% | -52 places |

**Impact:** Provinces heavily reliant on agriculture experienced a massive rank drop in Phase 1 because their astronomical OAE losses were replaced by the artificially capped DDPM advance payments. Conversely, provinces with minimal agriculture saw their relative risk ranking surge.

## 3. The Denominator Reality: Agricultural GPP vs. Total GPP

While the Pilot Methodology states that NESDC Total GPP was intended to be used, an audit of the provided TEI dataset (`gpp_avg_2559_2566.csv`) reveals that the data actually contained **Agricultural GPP (GPPเกษตร)**. 

### Evidence of Denominator Expansion
Phase 1 correctly utilizes the standardized **NESDC Total GPP**. Because Total GPP includes manufacturing, services, and industry, transitioning to Phase 1 resulted in a massive expansion of the denominator, thereby diluting the `Loss Rate` (Loss / GPP).

| Province (จังหวัด) | Pilot GPP Data | Phase 1 Total GPP | Expansion Ratio |
| :--- | :--- | :--- | :--- |
| **กรุงเทพมหานคร (Bangkok)** | 2,213 M Baht | 5,620,290 M Baht | 2538x larger |
| **สมุทรปราการ (Samut Prakan)** | 3,993 M Baht | 729,243 M Baht | 182x larger |
| **ชลบุรี (Chon Buri)** | 19,436 M Baht | 1,058,835 M Baht | 54x larger |

**Impact:** Dividing the already shrunken DDPM loss values by the massively expanded Total GPP caused the `loss_rate` indicator for almost all provinces to approach zero (e.g., Chaiyaphum's rate dropped from 0.036 to 0.000095). This completely compressed the scoring range for the economic pillar in Phase 1, making Human Impact the predominant driver of the final index.

## 4. Human Impact and Temporal Shifts

Both phases utilized **DDPM** data for human impacts (Deaths and Affected), but discrepancies still occurred (e.g., Narathiwat deaths dropped from 3.625 to 0.875). These variations are attributed to:
1.  **Temporal Window:** The Pilot averaged 8 years of data covering **2559-2566**, whereas Phase 1 utilizes the standardized pipeline covering **2560-2567**. 
2.  **Spatial Roll-up Logic:** The Phase 1 pipeline uses strict, automated logic to aggregate village-level DDPM data up to the province level, treating missing reports and "zeros" with greater scrutiny than the manual aggregations performed during the Pilot.

## 5. Conclusion

The CRI rankings are highly sensitive to the administrative boundaries of the financial proxies used. 
*   The **Pilot Phase** functioned effectively as an **Agricultural Risk Index**, elevating rural provinces due to the use of OAE data and an Agricultural GPP denominator. 
*   **Phase 1** functions as a **Fiscal Relief Index**, normalizing economic loss through capped DDPM payouts and diluting it against the Total Economy. This structural shift fundamentally alters the geographic distribution of identified climate risk across Thailand.
