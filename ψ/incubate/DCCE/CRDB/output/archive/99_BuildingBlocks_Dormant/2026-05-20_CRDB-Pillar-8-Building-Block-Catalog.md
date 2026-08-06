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

| Block ID | Building Block Name | Sitemap vNext Mapping | Purpose (The Handoff Requirement) |
| :--- | :--- | :--- | :--- |
| **BB-01** | **Data Engineering & ETL Pipelines** | 6. Knowledge, Tools & Services | **Mandatory Handoff**: Contractor must build Harvester Nodes to implement the source-to-CDM mapping provided in Pillar 4. |
| **BB-02** | **CDM & Governance Rails** | 6. Knowledge, Tools & Services | **Mandatory Handoff**: Contractor must implement G1-G5 validation gates as a hard-coded gatekeeper for the CDM physical schema. |
| **BB-03** | **National Situation Dashboard (MVP-2)** | 2. Policy Maker Center | **Strategic Anchor**: The primary interface for L&D stats and Risk Outlook summary. |
| **BB-04** | **Provincial Risk Profiles (MVP-1)** | 4. Risk & Area Profiles | **Product Anchor**: Automated PDF/Briefing pack generator based on provincial CDM views. |
| **BB-05** | **Recommended Dataset Registry (MVP-3)** | 6. Knowledge, Tools & Services | **Governance Anchor**: The DCAT-AP compliant catalog for 'Official' vs. 'Experimental' data. |
| **BB-06** | **Business Glossary Engine** | 6. Knowledge, Tools & Services | **Semantic Anchor**: The Universal Semantic Layer (USL) that maps technical tables to the 100+ approved terms. |

### **Tier 2: Policy Service Layer (Should-Have)**
| Block ID | Building Block Name | Sitemap vNext Mapping | Purpose |
| :--- | :--- | :--- | :--- |
| **BB-07** | **"Make it Usable" Resource Hub** | 5. Adaptation Measures | Centralized repository for Policy, Legal, and Funding templates. |
| **BB-08** | **Uncertainty-Safe Analysis (MVP-4)** | 6. Knowledge, Tools & Services | Decision-readiness labeling and interpretive guidance for future risk. |
| **BB-09** | **Hazard & Vulnerability Overlay Tool** | 6. Knowledge, Tools & Services | Spatial service for overlaying hazard layers with DCCE assets. |

### **Tier 3: Thematic & Expansion Slices (Nice-to-Have)**
| Block ID | Building Block Name | Sitemap vNext Mapping | Purpose |
| :--- | :--- | :--- | :--- |
| **BB-10** | **Adaptation Cycle Knowledge Hub** | 3. Info by Cycle | Detailed thematic hubs (3.1-3.6) for researchers. |
| **BB-11** | **Public Engagement & News** | 7. News & About | Identity branding and partner agency directory. |
| **BB-12** | **Adaptation Options Library** | 5. Adaptation Measures | Curated case studies and NbS vs. Infra catalogs. |

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
