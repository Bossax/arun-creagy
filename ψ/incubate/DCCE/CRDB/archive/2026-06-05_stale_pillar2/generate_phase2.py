import json
import os

with open('ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

s01 = [u for u in data if u.get('service_id') == 'S01']
s02 = [u for u in data if u.get('service_id') == 'S02']
s03 = [u for u in data if u.get('service_id') == 'S03']
s04 = [u for u in data if u.get('service_id') == 'S04']
s05 = [u for u in data if u.get('service_id') == 'S05']
s06 = [u for u in data if u.get('service_id') == 'S06']
s07 = [u for u in data if u.get('service_id') == 'S07']

def format_ucs(ucs):
    return '\n'.join([f"  - **{u['id']} ({u['agency']})**: {u['use_case']} (Specs: {u.get('data_parameters', {}).get('resolution', '')})" for u in ucs])

md = f"""# Logic Memo: Sector-Agnostic Canonical Synthesis (Phase 2)

**Status**: Intermediate Synthesis Artifact (v5.0 Pipeline)
**Date**: 2026-06-08
**Input**: 40 Use Cases from `P2_Hard_Dependencies_Inventory.json` (Activity 1 & 2)

## Synthesis Rule Application
This document maps 40 granular agency demands into 7 Service Platforms based strictly on **Technical Methodology**, explicitly rejecting sector-based silos (Rule A). 

---

### S01: National Authoritative Data Catalog & Discovery (SSOT)
**Methodology**: Federated metadata cataloging (DCAT-AP).
**Clustered Inputs**:
{format_ucs(s01)}
**Synthesis Logic (Rule B & C)**: 
*   UDDC and DCCE require a single truth baseline. This will form the core 'Urban/National Catalog'.
*   *Enrichment*: DCAT-AP 3.0.0 standards must be applied to ensure interoperability with DGA's GDX highway.

### S02: Exposure & Vulnerability Analytics
**Methodology**: Spatial intersection of physical hazards with cross-sectoral exposure indicators.
**Clustered Inputs**:
{format_ucs(s02)}
**Synthesis Logic (Rule A, B & C)**: 
*   *Sector-Agnostic Proof*: LDD (Agricultural Crop/Soil) and MSDHS (Human/Bedridden) both require exactly the same spatial overlay math.
*   *Enrichment*: EA (Enumeration Area) logic from NSO must be applied as the highest-resolution denominator for both social and agricultural vulnerability.

### S03: Climate Investment ROI & Fiscal Planning
**Methodology**: Financial Cost-Benefit Analysis (CBA) & Triple Dividend.
**Clustered Inputs**:
{format_ucs(s03)}
**Synthesis Logic (Rule B & C)**: 
*   DLA requires a regulatory shield (ROI) to unlock accumulated funds. NESDC needs GDP adjustments.
*   *Enrichment*: World Bank 'Triple Dividend of Resilience' framework must be injected to standardize the Avoided Loss calculations.

### S04: Climate Loss & Damage Assessment
**Methodology**: Post-event economic accounting (Replacement Cost).
**Clustered Inputs**:
{format_ucs(s04)}
**Synthesis Logic (Rule A & C)**: 
*   MOTS (Tourism) joins DDPM (Disaster Relief) here. Tourism economic loss is calculated using the same post-event replacement cost models.
*   *Enrichment*: Sendai Framework Target C (Economic Loss) Sub-indicators C-2 to C-6.

### S05: Infrastructure Risk & Engineering Specifications
**Methodology**: Climate-adjusted engineering design codes.
**Clustered Inputs**:
{format_ucs(s05)}
**Synthesis Logic (Rule A & C)**: 
*   MD (Marine Port Infra), OTP (Transport Infra), and DPT (Urban Drainage) all rely on climate-adjusted return periods.
*   *Enrichment*: PIANC WG 178 / TG 193 Framework for port infrastructure and climate-adjusted IDF curves for urban drainage.

### S06: Real-Time Threshold Monitoring
**Methodology**: Near real-time API telemetry and threshold triggering.
**Clustered Inputs**:
{format_ucs(s06)}
**Synthesis Logic (Rule A & B)**: 
*   *Sector-Agnostic Proof*: Combines BMA (Heatwaves), DMCR (Coral Bleaching), ONWR (Water Supply), and TMD (Flash Floods). The methodology is universal: Track API > Hit Threshold > Trigger Alert.
*   *Enrichment*: Wet Bulb Globe Temperature (WBGT) for health, and 30-day thermal stress models for marine ecosystems.

### S07: Policy Monitoring & NAP Compliance
**Methodology**: AI/NLP gap analysis against national targets.
**Clustered Inputs**:
{format_ucs(s07)}
**Synthesis Logic (Rule B)**: 
*   PMUA (Research Funding) and NXPO (Technology Readiness) require tracking progress against NAP targets to allocate funds.
*   *Enrichment*: Automated tracking algorithms mapped directly to the 6 core NAP sectors.
"""

with open('ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_v5_Intermediate_Clustering_Synthesis.md', 'w', encoding='utf-8') as f:
    f.write(md)

print("Phase 2 Logic Memo Generated Successfully.")
