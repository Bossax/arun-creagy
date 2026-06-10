# Learnings from Past Methodology: UNDP Project 2025 (CORRECTED)

**Date**: 2026-06-10  
**Source**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Dataset_review_UNDP_project2025.xlsx`

## 1. Full Metadata Schema & Table Design
The past methodology utilizes a **Comprehensive Utility Schema** that captures the entire lifecycle of a dataset from source to decision-support.

| Column | Analytical Purpose |
| :--- | :--- |
| **HEV** | Classification into **Hazard (H)**, **Exposure (E)**, or **Vulnerability (V)**. Critical for identifying "Integrated Risk" vs "Siloed Hazard" data. |
| **Data Product** | The logical nature of the data: **Statistics, Readings, Analytics, Model Forecast, Climate Projection**. |
| **Description** | Detailed technical context of what the dataset represents (e.g., "Number of villages trained," "Hotspots from MODIS"). |
| **Source** | The originating agency (**TMD, RID, DDPM, GISTDA, LDD, NSO, DPT**). |
| **Format** | The raw data format (**CSV, NetCDF, PDF, XLS, GIS**). |
| **Information Type** | The delivery medium (**Web app, Map, Static Image, Report**). |
| **Use Case** | The administrative intent: **Communicate, Change management or operations, Policy Support, Planning**. |
| **Link** | Evidence anchoring via URL. |
| **Frequency** | Temporal resolution (Daily, Weekly, Monthly, N/A). |

## 2. Advanced Analytical Logic
- **Causal Chaining**: The methodology tracks how **Readings** (Raw data) are transformed into **Analytics** (Decision support) and then delivered via **Web apps/Maps**.
- **Institutional Mapping**: Explicitly tracks which agencies (Source) dominate which Data Products (e.g., TMD for Models, NSO for Exposure/Vulnerability).
- **Format-to-Utility Gap**: Identifies where high-value data (e.g., WRF-DA) is trapped in **Restricted** formats or **Static Images**, preventing automated operational use.
- **HEV Multi-dimensional Mapping**: Identifies datasets that cover multiple dimensions (e.g., H,E,V), which are the highest-value "Synthetic" products for policy making.

## 3. Stylistic & Structural DNA
- **Forensic Precision**: Replaces vague descriptions with specific "Data Product" types.
- **Utility-Led Headers**: Focuses on the *Outcome* of the data (e.g., "Change management or operations").
- **Audit-Ready Evidence**: Every row is anchored by a **Source** and a **Link**, moving from "claims" to "grounded facts."

---
*Status: Corrected and Finalized for NCAIF Section 2.1 expansion.*
