# Pillar 8: Building Block Catalog & Procurement Tiers
**Project**: CRDB (Climate Risk Data Blueprint)
**Status**: DRAFT (Pillar-Alignment v1)
**Date**: 2026-05-20
**Strategic Anchor**: "Modular Integrity" (Shielding against budget-driven fragmentation)

---

## 1. Purpose
The Building Block Catalog provides a modular inventory of the CRDB platform's functional components. By tiering these "blocks," we provide DCCE with a **Procurement Shield**: a clear hierarchy of what *must* be built to preserve the system's structural integrity (Tier 1) versus what can be scaled or deferred based on budget (Tiers 2-3).

---

## 2. Procurement Tiers (The "Menu" Logic)

### **Tier 1: The Core Resilience Engine (Must-Have)**
*Identity: The non-negotiable plumbing and "Official Truth" anchors.*
*   **Success Criterion**: Without Tier 1, the platform is merely a "website" and fails as a data integration blueprint.

| Block ID | Building Block Name | Sitemap v4 Mapping | Purpose |
| :--- | :--- | :--- | :--- |
| **BB-01** | **Data Engineering & ETL Pipelines** | 4.1 (Backend) | The automated harvesting logic for official sources (TMD, GISTDA, DDPM). |
| **BB-02** | **CDM & Governance Rails** | 4.2 (Standards) | System logic that enforces G1-G5 DQ gates and CDM schema compliance. |
| **BB-03** | **National Situation Dashboard (MVP-2)** | 2.1 (A, B, C) | The "National Monitoring Loop" for L&D stats and Risk Outlook. |
| **BB-04** | **Provincial Risk Profiles (MVP-1)** | 2.2 (Profiles) | Decision-ready "Briefing Pack" generator for governors and planners. |
| **BB-05** | **Recommended Dataset Registry (MVP-3)** | 4.1 (Catalog) | The "Clearinghouse" that defines what data is official vs. experimental. |
| **BB-06** | **Business Glossary Engine** | 2.3 / 4.2 | The semantic service that prevents "Expert Drift" via 100+ approved terms. |

### **Tier 2: Policy Service Layer (Should-Have)**
*Identity: Tools that translate data into implementation action.*
*   **Success Criterion**: Enhances the "Usability" of the core data for specific policy workflows.

| Block ID | Building Block Name | Sitemap v4 Mapping | Purpose |
| :--- | :--- | :--- | :--- |
| **BB-07** | **"Make it Usable" Resource Hub** | 2.3 (Resources) | Centralized repository for Policy, Legal, Funding, and TOR templates. |
| **BB-08** | **Uncertainty-Safe Analysis (MVP-4)** | 2.4 (Methodology) | Interpretive guidance and "Decision Readiness" labeling for future risk. |
| **BB-09** | **Hazard & Vulnerability Overlay Tool** | 2.4 (Services) | Interactive spatial tool for overlaying ADPC hazards with DCCE vulnerability. |

### **Tier 3: Thematic & Expansion Slices (Nice-to-Have)**
*Identity: Deep knowledge hubs and public engagement features.*
*   **Success Criterion**: Provides the "Long-Tail" of climate knowledge for researchers and the public.

| Block ID | Building Block Name | Sitemap v4 Mapping | Purpose |
| :--- | :--- | :--- | :--- |
| **BB-10** | **Adaptation Cycle Knowledge Hub** | 3 (All sections) | Detailed "Knowledge Hub" for researchers (3.1-3.5) by cycle stage. |
| **BB-11** | **Public Engagement & News** | 1 (Home) / 5 | Identity branding, news updates, and "Partner Agency" directory. |
| **BB-12** | **Adaptation Options Library** | 3.4 (Options) | Case studies and NbS vs. Infrastructure catalogs. |

---

## 3. Functional Requirements Mapping (Use Case Alignment)

| Use Case (UC) | Primary Building Block | Why Tiered This Way? |
| :--- | :--- | :--- |
| **UC-01: L&D Impact Stats** | **BB-03** (Nat. Situation) | **Tier 1**: Mandatory for national tracking of climate-related costs. |
| **UC-03: Provincial Risk Profiles** | **BB-04** (Briefing Packs) | **Tier 1**: The primary product for sub-national "Buy-in" and planning. |
| **UC-03b: Budget Justification** | **BB-07** (Resource Hub) | **Tier 2**: Critical for implementation, but requires Tier 1 data first. |
| **UC-10: Baseline Verification** | **BB-05** (Dataset Reg) | **Tier 1**: Required to solve the "Which data is right?" dispute. |
| **UC-11: Financial Stress Testing** | **BB-08** (Uncertainty) | **Tier 2**: Essential for banks/private sector to avoid deterministic misuse. |

---

## 4. Procurement Strategy: "The 3-Year Rollout"
*   **Year 1 (The Shield)**: Focus 100% on **Tier 1**. Establish the CDM, ETL Pipelines, and the first 3 MVPs (Briefing Packs, L&D Stats, Dataset Registry).
*   **Year 2 (The Enabler)**: Introduce **Tier 2**. Roll out the Resource Hub and Uncertainty Methodology to drive implementation.
*   **Year 3 (The Hub)**: Expand into **Tier 3**. Flesh out the Adaptation Cycle knowledge hub and public engagement features.

---
*Synthesized by ARUN for CRDB Pillar 8; derived from Sitemap v4 and Blueprint Strategy.*
