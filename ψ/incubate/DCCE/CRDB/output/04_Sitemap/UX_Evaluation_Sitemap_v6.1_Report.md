# UX Evaluation Sitemap Report: NCAIF v6.1 (Rigorous Audit Baseline)
**Date:** June 6, 2026
**Framework:** Persona-Capability Friction Analysis
**Technical Baseline:** Sitemap v6.1 & Asset Mapping v6.1 (CSV)

---

## 1. Executive Summary: The "Grounding Gap"
The v6.1 architecture is strategically sound but faces significant **Implementation Friction** due to the low readiness of critical assets. While the "Natural by Design" navigation (Node 1.2/1.3) is intuitive, the destination pages currently lack the web-ready prose needed to fulfill the "Explainer" mandate.

---

## 2. Persona Journey & Friction Audit

### 👤 Persona 1: Somchai (The Policy Maker)
*   **Goal:** Justify budget and risk allocation.
*   **Success Path:** 1.1 Summary → 1.3 Policy Shortcut → 2.3 Finance/Legal.
*   **🚨 Critical Friction Point (Node 2.3):** The "Budget Status" and "Fund Lists" are currently mapped to **"DCCE Internal Library" (Readiness: LOW)**. 
    *   **Impact:** Somchai hits a "Data Black Box." Without harvesting this internal data into a web-ready database, his primary journey is broken. He cannot "one-click export" budget evidence that doesn't yet exist in the system.

### 👤 Persona 2: Dr. Clara (The Scientist)
*   **Goal:** Clean data access for modeling.
*   **Success Path:** 1.3 Shortcut → Section 6 (Data Catalog).
*   **⚠️ Moderate Friction Point (Node 6.1):** Data Catalog is **"Partial (Governance & Metadata Required)"**.
    *   **Impact:** Clara finds the links (TMD/GISTDA), but the *Metadata* and *Lineage* (crucial for her trust) are not yet integrated. Her journey is "Discovery-Ready" but "Integration-Poor."

### 👤 Persona 3: Priya (The Co-Producer)
*   **Goal:** Translate raw data into farmer alerts.
*   **Success Path:** 1.3 Shortcut → 4.2 Sectoral Profiles (Agriculture).
*   **🚨 Critical Friction Point (Node 4.2):** Sectoral Profiles are **"Low (Impact Chain Synthesis Required)"**.
    *   **Impact:** Priya needs pre-calculated "Derived Data" (e.g., soil moisture indices). Currently, the asset mapping only points to raw NC4 reports. She is forced to do the "Janitorial Work" herself, which defeats the purpose of the platform.

---

## 3. Capability-Readiness Matrix (Forensic View)

| **Capability** | **Node** | **Brief vs. Reality Check** | **UX Risk** |
| :--- | :--- | :--- | :--- |
| **Area Search** | 1.2 | Engine ready, but 77 provincial pages (4.1) are **LOW readiness**. | User finds their province, but the landing page is empty/generic. |
| **Policy Tools** | 2.3 | Brief promises "Fund Lists," but asset is "Internal Library." | **Major Hallucination Risk.** Site feels like a "Broken Link Hub." |
| **Explainer Prose**| 3.1/3.2| Brief promises "Narrative Scenarios," asset is "IPCC/NC4 PDF." | High cognitive load. Users will bounce if they have to read 200-page PDFs. |

---

## 4. Remediation Strategy (Prioritized Tasks)

1.  **Node 2.3 Harvesting (High Priority):** Must transform "Internal Library" documents into a structured "Finance & Legal Database" before frontend development starts.
2.  **Node 4.1 Narrative Sprint (High Priority):** 77 provinces require a "Synthesis Template" to turn GIS data into the promised "Historical/Future Risk Summaries."
3.  **Explainer Conversion (Medium Priority):** Sections 3.1 and 3.2 need a technical writer to convert NC4 science chapters into "Natural by Design" web-prose (Max 300 words per node).

---

## 5. Audit Conclusion
The Sitemap v6.1 is a high-fidelity map of the *desired* system. However, the **Asset Mapping v6.1** reveals that the platform is currently a **"Metadata Shell."** Implementation must prioritize **Content Synthesis** over UI features to ensure that the three personas find "Knowledge," not just "Files."
