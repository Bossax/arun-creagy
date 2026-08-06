# Reality-First Audit: Current DCCE Website as Groundwork for NCAIF

**Date**: 2026-06-04
**Oracle**: ARUN (Strategic Gatekeeper)
**Audit Scope**: Mapping legacy website sections to NCAIF v5.2 Nodes.

## Executive Summary
The rerun of the asset audit confirms that the **Current DCCE Website** is the primary groundwork for **Institutional Memory, Policy Documents, and Specialized Tools**. While technical reports (Risk DB/CRI) provide the "New Science," the legacy website provides the "Institutional Context."

---

## 1. Mapping: Legacy Website to NCAIF Nodes

| NCAIF Node | Groundwork Section (DCCE Website) | Primary URL(s) | Readiness |
| :--- | :--- | :--- | :--- |
| **1.1 Home / Overview** | About Us (Vision & Mission) | `dcce.go.th/about-us/vision-mission/` | **Migration-Ready** |
| **1.3 Help Me Plan** | Public Services + CCE Information | `dcce.go.th/publicservice/` | **Integration-Ready** |
| **2.3 Policy & Finance** | Central Information Center (Legal/Finance) | `dcce.go.th/datacenter/661/`, `.../6665/` | **High (Direct Link)** |
| **3.4 Adaptation Plan** | Central Info (Adaptation Cluster) | `dcce.go.th/datacenter/669/` | **Partial (PDF unbundling)** |
| **3.5 M&E / Reports** | National Reports (NC/BUR/BTR) | `dcce.go.th/datacenter/657/` | **High (Migration)** |
| **5.2 Success Stories** | CCE Info (Green Office/Eco School/SAR) | `ecoschool.dcce.go.th`, `greenhotelthai.com` | **Integration-Ready** |
| **6.1 Data Catalog** | Data Catalog System (CKAN) | `dgf.dcce.go.th/` | **Integration-Ready** |
| **7.1 News / About** | News Feed + About Us Submenus | `dcce.go.th/news/`, `.../about-us/` | **Migration-Ready** |

---

## 2. Forensic Findings: Content as Groundwork

### **A. Institutional Core (Nodes 1.1, 7.1)**
*   **Audit**: The current "About Us" cluster is 100% complete for institutional identity.
*   **Groundwork**: These pages serve as the **Official Prose** for the new platform. No new writing is required, only structural refactoring.

### **B. The "Scattered" Services (Nodes 1.3, 5.2)**
*   **Audit**: Technical services (Green Hotel, Eco School, e-Learning) are currently distributed across subdomains.
*   **Groundwork**: These are **Functional Assets**. The NCAIF should act as a "Unified Portal" that frames these existing services rather than rebuilding them.

### **C. Policy & Legal (Node 2.3)**
*   **Audit**: The "Central Information Center" contains the most recent Climate Act drafts and Strategy documents.
*   **Groundwork**: These are the **Legal Anchors**. They provide the "Transparency Armor" that justifies the platform's mandates.

### **D. The Gap: Narrative & Dashboards**
*   **Finding**: The legacy website is **Document-Centric** (PDF repositories).
*   **Action**: The groundwork for the *narrative* (Synthesis) must still come from the **Risk DB** and **CRI Reports**, as the website does not yet have a workflow-centric view of adaptation.

## 3. Implementation Action Recommendation
For the vendor, the DCCE Website is the **"Draft 1"** of the content. The implementation strategy should be:
1.  **Harvest**: Scrape/extract prose from the mapped URLs.
2.  **Unbundle**: Transform PDF reports (NC/BUR) into high-level summaries.
3.  **Frame**: Create a unified navigation layer for the scattered `*.dcce.go.th` subdomains.

---
*Verified by ARUN Forensic Sub-Agents.*
