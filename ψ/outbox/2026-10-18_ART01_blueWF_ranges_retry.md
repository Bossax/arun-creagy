# [DELIVERABLE BRIEF] 2026-10-18_ART01_blueWF_ranges_retry

**From:** arun  
**To:** samart  
**Date:** 2026-10-18  
**Topic:** ART01 blue-WF range provenance — fresh NotebookLM run

## Concise source-grounded answer

The fresh source-restricted NotebookLM query succeeded. It locates **crop 1: 55.4–95 m³/t** and **crop 3: 803–1,194 m³/t** in **§3.3, “WF changes under the CMIP6 climate scenarios,” PDF page 8** (page location reported by NotebookLM). These are summary ranges for rice crops in the irrigated RRR (triple-rice) system, accompanying **Fig. 5(a), first rice**, and **Fig. 5(c), third rice**. The paragraph cites “Fig. 5(d)” for third rice; NotebookLM identifies this as a panel typo, supported by the returned figure labels, which list (a) First rice, (b) Second rice, (c) Third rice.

Brief exact source wording from the returned §3.3 excerpt: “The blue WF was highest in the third rice crop (803–1194 m3 ton−1, Fig. 5(d))”.

**What exactly the min–max spans remains only partly verified.** NotebookLM's answer describes multi-model ensemble averages across the three future periods (2015–2039, 2040–2069, 2070–2100) and both SSP2-4.5 and SSP5-8.5. However, its cited excerpts establish the study's general five-GCM/two-SSP/three-period design, not an explicit definition of the population used to calculate these particular extrema. The ensemble citation discusses the approach generally; it does not explicitly connect that calculation to these ranges. Treat the claimed future-ensemble grouping as **NotebookLM's interpretation, not conclusively established range provenance**.

| Specific question | Source-grounded status from this run |
|---|---|
| Baseline-only values? | Not established. Baseline inclusion/exclusion is explicitly UNKNOWN in the NotebookLM answer. |
| Extrema across all three future periods and both SSPs? | Reported by NotebookLM, but not explicitly demonstrated in its returned source excerpts; exact coverage UNKNOWN. |
| Extrema across individual outputs of all five GCMs versus ensemble averages? | NotebookLM says ensemble averages; exact range construction is not established by the returned excerpts, so UNKNOWN. |
| Other grouping, annual observations versus period means? | UNKNOWN; no explicit definition returned. |
| Endpoint-to-period/SSP/GCM mappings? | UNKNOWN for all four endpoints; NotebookLM returned no mapping table. |

Use these as the paper's reported **crop-specific summary ranges**, with a §3.3/Fig. 5 reference. Do not state definitively that the extrema include the baseline, span every future combination, or represent individual-model extrema. No second research query or substitute source was used.

## Source and audit record

- Supplied PDF: `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf` (Arunrat et al., 2022).
- Notebook: https://notebooklm.google.com/notebook/bb0355f2-1119-4385-b3bc-6b7cfa189296
- Only queried source UUID: `ac09eff0-ebf1-4104-9736-620bb838ffe9`.
- Conversation: `54c985c6-0e0d-41dd-ac57-1596030e0d79`.
- Verbatim CLI stdout, stderr, exact request and exit code: /mnt/c/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/notebooklm_runs/2026-10-18_232758_ART01_blueWF_ranges_retry. Query exit code: 0.
- The complete original JSON response follows unchanged, including NotebookLM's answer and cited source excerpts. Those excerpts support the qualifications above; the AI answer itself is not a substitute for source wording.

## Verbatim NotebookLM CLI response

```json
{
  "answer": "In the paper (*Arunrat et al., 2022*), the blue water footprint (\\\\(\\text{WF}_{\\text{blue}}\\\\)) ranges of **\\\\(55.4\\text{--}95\\text{ m}^3\\text{ ton}^{-1}\\\\) for first rice** and **\\\\(803\\text{--}1194\\text{ m}^3\\text{ ton}^{-1}\\\\) for third rice** are reported as summary min–max ranges in **Section 3.3 (\"WF changes under the CMIP6 climate scenarios\") on PDF Page 8** [1]. \n\n### Grouping and Scope\n* **Figure & Panels Referenced:** The text references **Figure 5(a)** for the first rice crop and **Figure 5(d)** for the third rice crop [1]. *(Note: \"Figure 5(d)\" in the text is a figure-panel typo, as Figure 5 contains only panels (a), (b), and (c), with third rice plotted in Figure 5(c))* [1, 2].\n* **Values Included:** The ranges reflect **multi-model ensemble averages** across the future projection periods (**near-future 2015–2039**, **mid-future 2040–2069**, and **far-future 2070–2100**) under both **SSP2-4.5** and **SSP5-8.5** climate scenarios for the irrigated triple-cropping (RRR) rice system [1-4].\n* **Baseline Inclusion:** **UNKNOWN.** Although the historical baseline (1981–2014) is plotted in Figure 5 alongside the future scenarios, the text does not explicitly state whether the baseline bar is included in or excluded from these summary min–max numbers [1, 2].\n* **Individual Endpoint Mapping:** **UNKNOWN.** The paper presents these figures strictly as overall summary ranges in the text accompanying Figure 5 and does not include a numerical lookup table mapping individual endpoints (such as \\\\(55.4\\\\), \\\\(95\\\\), \\\\(803\\\\), or \\\\(1194\\text{ m}^3\\text{ ton}^{-1}\\\\)) to specific GCM outputs, individual years, or specific SSP/period combinations [1].\n\n💡 *Would you like to examine the crop yield projections or green/grey water footprints for these irrigated rice crops across the different SSP scenarios?*",
  "question": "In the paper, what exactly do the blue-WF ranges 55.4-95 m3/t for irrigated rice crop 1 and 803-1194 m3/t for crop 3 span? Are these baseline values, future periods, SSP scenarios, GCM outputs, or another grouping? Give the exact figure/table/page or say unknown.",
  "conversation_id": "54c985c6-0e0d-41dd-ac57-1596030e0d79",
  "sources_used": [
    "ac09eff0-ebf1-4104-9736-620bb838ffe9"
  ],
  "citations": {
    "1": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
    "2": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
    "3": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
    "4": "ac09eff0-ebf1-4104-9736-620bb838ffe9"
  },
  "references": [
    {
      "source_id": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
      "citation_number": 1,
      "cited_text": "3.3. WF changes under the CMIP6 climate scenarios The green WF was higher than the blue WF in the rainy season, while the blueWFwashighly consumed in the dry season. As a baseline, the total WFs of rice and maize production were between 1206 and 1467 and 682–866 m3 ton−1, respectively. Soybean, mung bean, and cassava had totalWFs of 542, 437, and 575m3 ton−1, respectively, com-pared to the baseline (Figs. 5–7). In irrigated areas, the total WF of rice production under the RRR cropping system continued to decline from near to far-future periods under the SSP245 scenario, while the total WF increased in mid and far-future periods under the SSP585 scenario. The highest greenWF occurred in the production of the first rice crop (758–1318 m3 ton−1, Fig. 5(a)), followed by the second (287–371 m3 ton−1, Fig. 5(b)) and third rice crops (153–194 m3 ton−1, Fig. 5(d)). The blue WF was highest in the third rice crop (803–1194 m3 ton−1, Fig. 5(d)), followed by the second (628–790 m3 ton−1, Fig. 5(b)) and first rice crops (55.4–95 m3 ton−1, Fig. 5(a)). The grey WF was 223–349 m3 ton−1, overall (Fig. 5(a), (b), and (c))."
    },
    {
      "source_id": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
      "citation_number": 2,
      "cited_text": "ecirdnoceS)b(ecirtsriF)a( (c) Third rice Fig. 5.Water footprint changes of RRR cropping system in irrigated areas (business-as-usual cropping systems). ecirdnoceS)b(ecirtsriF)a( Fig. 6.Water footprint changes of RR cropping system in the rain-fed area (business-as-usual cropping systems). N. Arunrat, S. Sereenonchai, W. Chaowiwat et al. Science of the Total Environment 807 (2022) 150741 eziaMecirtsriF (a) RM cropping system naebyoSecirtsriF metsysgnipporcSR)b( naebgnuMecirtsriF (c) RB cropping system"
    },
    {
      "source_id": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
      "citation_number": 3,
      "cited_text": "In this study, five CMIP6 global circulation model datasets (CESM2, MRI-ESM2-0, BCC-CSM2-MR, GFDL-ESM4, and CanESM) were selected under three future periods: 2015–2039, 2040–2069, and 2070–2100. Furthermore, SSP245 (538.9 ppm CO2 equivalent) and SSP585 (936.4 ppm CO2 equivalent) were used to predict the major crop yield and WF changes in the future. This is because the SSP245 scenario is subjective to most countries striving for sustainable development, while the SSP585 scenario represents the worst scenario (energy-intensive, fossil-based economy), which embodies the impact of uncon-ventional development (O'Neill et al., 2016). The precipitation and maximumandminimum temperatures under CMIP6 climate projection were obtained from HAII, which were downscaled (at resolution 0.1 × 0.1° of grid size) and analyzed bias correction (Chaowiwat et al., 2016; Chaowiwat et al., 2019)."
    },
    {
      "source_id": "ac09eff0-ebf1-4104-9736-620bb838ffe9",
      "citation_number": 4,
      "cited_text": "The multi-model ensemble average approach is widely used for cli-mate modelling to reduce the large biases and uncertainties from model parameterization errors, model structures, assumptions, and input variables (Khan et al., 2018; Ahmed et al., 2019). However, CMIP6 models have shown improvement based on the previous re-gional studies (e.g., Stouffer et al., 2017; Rivera and Arnould, 2020; Gusain et al., 2020; Gao et al., 2021). Kim et al. (2020) reported that the CMIP6 models improve the limitation of the CMIP5 models in terms of the observed global and regional patterns of temperature ex-tremes. Bağçaci et al. (2021) indicated that CMIP6 models outperform CMIP5 models in terms of accuracy statistics, especially precipitation simulation. Meanwhile, the error in precipitation and temperature under CMIP6 models were reduced by 11% and 6%, respectively. Yazdandoost et al. (2021) revealed that CMIP6models showed less sys-tematic biases of precipitation simulation in the arid zone and underes-timation in the humid zone indicating high uncertainty in wet regions. Similar to in the Mainland South-East Asia (MSES), Iqbal et al. (2021) found that the CMIP6 models simulated the annual mean precipitation in the central and southern region of MSEA with a bias of less than 25%, whereas high biases (−25 to−75%) were detected in the western coastal region of Myanmar, where the highest precipitation was ob-served. However, CMIP6 models can be used for climate change projec-tions after correcting the related biases and uncertainties."
    }
  ]
}
```
