# Phase 4 & 5: Demand Clustering & Requirement Synthesis (Corrected)

This analysis groups the 26 normalized service concepts into thematic clusters and synthesizes their common technical requirements, reflecting the corrected canonical mapping.

## 1. Demand Clusters (Phase 4)

| Cluster ID | Cluster Name | Concept Count | Primary Momentum (Votes) | Key Stakeholders | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **CL-A** | **Authoritative Baselines & SSOT** | 8 | High (G2-C6, G3-C9) | TBA, ONWR, NXPO, LDD | Demand for "Single Source of Truth" (4.1) climate baselines (20-50yr) and accepted hydrological projections. |
| **CL-B** | **Localized Vulnerability & Risk** | 7 | High (G2-C4, G3-C8) | DCCE, MSDHS, DOH, UDDC | Focus on high-resolution (Sub-district) integration of hazard maps with socio-economic vulnerability (2.1-2.4). |
| **CL-C** | **Sectoral Impact & Standards** | 6 | High (G2-C5, G4-C7) | OTP, Tourism, MD, Ag | Quantification of sectoral L&D (1.1, 1.7) and resilient infrastructure engineering standards (2.6). |
| **CL-D** | **Urban Resilience & Land Use** | 5 | High (G78-C8) | DPT, BMA, UDDC | Climate-resilient design (2.5) and spatial planning for heat (2.7) and water (3.5-3.7). |
| **CL-E** | **Truly New Domain Frontiers** | 6 | Medium (G78-C2) | TMD, ONEP, DMR | Emergent needs not in the pre-workshop menu: Sinkholes, Marine Biodiversity, Sea Water Quality, and Localized Thresholds. |

## 2. Requirement Synthesis (Phase 5)

Across all clusters, the following "Shared Infrastructure Needs" have been validated against the original system design:

### 2.1 Technical Delivery Formats (The "Utility" Shift)
*   **API Dominance**: Universal demand for **API Access** (G2-C5, G2-C6, G3-C11, etc.) indicates a shift from "Dashboard users" to "Power users" feeding internal systems.
*   **Sub-district Granularity**: The "Tambon" level is now the minimum viable resolution for local planning (Cluster B).
*   **Asset-Level Specification**: Financial and Infrastructure sectors (CL-A, CL-C) require coordinates/asset-level probabilistic data.

### 2.2 Functional Requirements (Hardening Priorities)
*   **SSOT Certification (4.1)**: The CRDB's primary value is seen as the **Certifier** of data, not just the provider. Users need a "National Baseline" they can cite in budget documents.
*   **Historical-Forecast Bridge**: High demand for **10-20yr historical baselines** to complement CMIP6 projections.
*   **Documentation-as-a-Product (4.2)**: "Usage Guides" are requested alongside data to ensure consistent interpretation across provincial offices.

### 2.3 Priority Ranking (Based on Vote Momentum)
1.  **Cluster A (Baselines/SSOT)**: High strategic momentum (TBA/Banks demand for "accepted" figures).
2.  **Cluster B (Localized Risk)**: High operational momentum (DCCE/MSDHS demand for "Tambon" resolution).
3.  **Cluster C (Sectoral Standards)**: High policy momentum (OTP/DPT demand for "Resilient Design" parameters).

---
*Updated: 2026-05-26 (v1.1 Corrected Mapping)*
*Status: Phase 4 & 5 Complete.*
