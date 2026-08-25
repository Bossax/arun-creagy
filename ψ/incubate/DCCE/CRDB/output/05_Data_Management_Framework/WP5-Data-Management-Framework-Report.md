# WP5: Data Management Framework Report

## 1. Executive Summary & Framework Scope

### 1.1 Objective of the Data Management Framework
The Data Management Framework serves as the foundational architecture for the DCCE Climate Risk Database (National Climate Adaptation Information Framework). Its primary objective is to establish a robust, scalable, and standardized environment where climate adaptation data can be securely stored, accurately understood, and effectively shared across different divisions and with external stakeholders. Rather than treating the platform as a static IT project, this framework establishes the rules of engagement that ensure the data remains a living, trustworthy asset that directly supports national climate policy and risk assessment.

### 1.2 Boundary Definition: Data Platform vs. Web CMS
A critical distinction must be made between the underlying **Data Platform** and the surface-level **Web Content Management System (CMS)**. 
- The **Web CMS** acts as the presentation layer—the "storefront"—handling user interfaces, dashboards, news articles, and visual navigation. 
- The **Data Platform**, governed by this framework, is the "warehouse" and "supply chain." It dictates how raw data is ingested, modeled, defined, and quality-controlled before it ever reaches the presentation layer. 

This framework strictly governs the data platform. It does not dictate web design, but rather ensures that the information surfacing on the web platform is governed by strict ownership and semantic standards.

### 1.3 The 3 Pillars of the Framework
To achieve this, the Data Management Framework is built upon three inseparable pillars:
1. **Semantic Standards (Business Glossary):** Defining *what* the data means.
2. **Conceptual Data Model (CDM v3.0):** Defining *how* the data is structured and related.
3. **Governance Operating Model:** Defining *who* owns the data and *how* it is managed.

---

## 2. Semantic Standards (Business Glossary)

### 2.1 Bridging Policy and Technical Architecture
Data silos often occur not because of technical barriers, but because of semantic ambiguity—different departments using the same term to mean different things, or different terms to describe the same asset. The Business Glossary eliminates this ambiguity by providing a standardized, human-readable definition for core concepts, acting as the ultimate bridge between high-level adaptation policy and low-level database architecture.

### 2.2 Glossary Scope and Limitations (v5)
The current iteration (Glossary v5) contains 74 canonically defined terms in both Thai and English. 
**Crucially, this glossary is strictly bounded: it covers *only* the data platform for climate adaptation.** It is **not** a DCCE-wide enterprise glossary, nor does it represent the official, finalized terminology for the entire Department of Climate Change and Environment. It serves solely as the specific source of truth required to facilitate cross-departmental data exchange within the exact scope of this adaptation platform.

### 2.3 Integration with the Conceptual Data Model
Every term defined in the Business Glossary maps directly to a technical entity within the database. When a policy maker requests data on a "Hazard Profile," the glossary ensures that the IT team queries the exact `DOM_020` entity defined in the architecture, preventing miscommunication and ensuring accurate data retrieval.

---

## 3. Conceptual Data Model (CDM v3.0)

### 3.1 Logical Architecture Overview
The Conceptual Data Model (CDM v3.0) is the conceptual data architecture that translates the semantic standards into a structured database blueprint. Superseding all previous drafts, CDM v3.0 is the canonical logical blueprint that will be handed off to the downstream system developer (TOR70).

### 3.2 The 8 Domains
To prevent the database from becoming an unmanageable monolith, the architecture is strictly segmented into 8 functional logical domains:
- **DOM_010:** Spatial & Administrative (ขอบเขตพื้นที่และการปกครอง)
- **DOM_020:** Hazard & Climate (ข้อมูลภูมิอากาศและภัยคุกคาม)
- **DOM_030:** Exposure & Vulnerability (ข้อมูลความเปราะบางและสิ่งเปิดรับ)
- **DOM_040:** Impact & Loss (ข้อมูลผลกระทบและความสูญเสีย)
- **DOM_050:** Adaptation Interventions (การดำเนินการปรับตัว)
- **DOM_060:** Policy & Strategy (นโยบายและยุทธศาสตร์)
- **DOM_070:** Knowledge & Resources (องค์ความรู้และทรัพยากร)
- **DOM_080:** Platform Administration (การบริหารจัดการแพลตฟอร์ม)

### 3.3 Domain Definitions and Boundaries for Data Ownership
The most critical function of these 8 domains is not merely technical organization, but the establishment of strict **domain boundaries**. By clearly defining where one domain ends and another begins, the architecture directly enables the assignment of Data Ownership down the line. A Group Director cannot take ownership of a dataset if its boundaries are blurred with another division's data. The CDM draws these hard lines, ensuring that technical structure perfectly mirrors organizational accountability.

### 3.4 Entity and Relationship Blueprints
The physical manifestation of this model is documented in the canonical `Entities-v3.csv` and `Relationships-v4.csv`, which detail the exact data types, constraints, and relational mappings required to physically build the database.

---

## 4. Governance Operating Model

### 4.1 The Need for Governance
As highlighted in the FGD3 alignment sessions, 80% of data projects fail not due to technology, but because organizations fail to sustain usage. Without assigned ownership, data becomes rapidly outdated, users lose trust, and the system is abandoned. Data governance prevents the "Abandoned System" trap by formally defining accountability.

### 4.2 DCCE Data Governance Structure
To sustain the platform, DCCE will implement a 4-tier operational governance structure:
1. **Data Governance Committee (คณะกรรมการด้านการกำกับดูแลข้อมูล):** The executive steering board, chaired by the Director-General, responsible for ratifying standards and resolving cross-divisional disputes.
2. **Data Owner (เจ้าของข้อมูล):** Group Directors (ผอ.กลุ่ม) who hold ultimate accountability for the quality, security, and publication of data within their assigned logical domains (e.g., the Director of the Risk Assessment Group owns `DOM_020` and `DOM_030`).
3. **Data Steward Team (ทีมบริกรข้อมูล):** The operational backbone, comprising Business Stewards (domain experts who define data rules) and Technical Stewards/Custodians (IT staff who maintain the physical infrastructure).
4. **Data User (ผู้ใช้ข้อมูล):** The internal and external consumers who rely on the governed data to make adaptation decisions.

### 4.3 Stewardship Operations in Practice
In practice, the Data Owner delegates day-to-day data quality monitoring to the Data Stewards. When a new dataset is proposed for ingestion, the Business Steward validates its accuracy against the Business Glossary, and the Technical Steward ensures it conforms to the CDM schema before it is published to the catalog.

### 4.4 Feature-Driven Governance Rollout Strategy
Rather than attempting to implement governance across all DCCE data simultaneously ("boiling the ocean"), the rollout will utilize a **Feature-Driven** strategy. Governance capabilities (like metadata tagging or data quality gates) will be deployed *just-in-time* to support the release of specific, high-value data products. This ensures that governance efforts are strictly tied to immediate business value and user adoption.

---

## 5. Implementation Roadmap (CRDB to TOR70)

### 5.1 The 7 Phases of the Enterprise Data System Lifecycle
The transition from the current planning phase to the actual software build follows the standard 7-phase Enterprise Data System lifecycle, establishing a clear boundary between current efforts and future vendor responsibilities.

### 5.2 Phase 1-3: Foundations & Design (CRDB Scope)
The current project (CRDB) is exclusively responsible for:
- **Phase 1 (Planning):** Defining the vision, critical use cases, and glossary.
- **Phase 2 (Requirement Analysis):** Identifying data gaps and product demands.
- **Phase 3 (Design):** Engineering the conceptual data model, system architecture, and governance framework.

### 5.3 Phase 4-7: Development & Deployment (TOR70 Scope)
The downstream contractor (TOR70) will execute:
- **Phase 4 (Development):** Writing code, building the database, and ingesting raw data.
- **Phase 5 (Testing):** QA, performance testing, and user acceptance.
- **Phase 6 (Deployment):** Installing the system into DCCE infrastructure.
- **Phase 7 (Maintenance):** Ongoing operational support.

### 5.4 The 3 Critical Governance Milestones
For TOR70 to successfully execute Phase 4, DCCE must achieve three critical governance milestones before development begins:
1. **DCCE as Product Owner:** DCCE must explicitly finalize the functional requirements for the highest-priority products.
2. **Certified Ownership:** Group Directors must formally accept their roles as Data Owners, and operational staff must be appointed as Data Stewards.
3. **Enforced Interoperability Standards:** The CDM and Glossary must be formally ratified as the mandatory standards for the system build.

### 5.5 Critical Dependencies and Stalled Decisions
The full execution of the TOR70 build is currently bottlenecked by several pending institutional decisions. Most critically, the formal ratification of the Data Governance Committee and the official assignment of Database Administration (DBA) organizational duties remain stalled. Resolving these dependencies is a strict prerequisite; failure to do so before Phase 4 begins will result in a technically sound system that lacks the organizational mandate required to operate it.
