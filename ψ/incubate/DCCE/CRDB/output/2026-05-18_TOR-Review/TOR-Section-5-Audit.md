# Audit: TOR Section 5 (Scope of Work) - Item-by-Item Review

**Goal**: Clause-by-clause analysis of the 25M THB "National Climate Change Adaptation Database" Draft TOR against the CRDB Anchor Lens and Enterprise Sustainability standards.

---

## 5.1 แผนการดำเนินงาน (Work Plan)
*   **TOR Requirement**: Develop a systematic work plan (Study -> Design -> Dev -> Test -> Install -> Train) with milestones and deliverables.
*   **Audit Findings**:
    *   **CRDB Alignment**: Does not explicitly mandate the ingestion of CRDB's architecture (CDM/NCAIF) as the "Input" for the Design phase.
    *   **Sustainability**: Standard SDLC.
    *   **Industrial Benchmark**: Lacks "Data Engineering" specific milestones (e.g., Schema Mapping, ETL Validation).
*   **Risk**: The consultant might treat this as a "Blank Slate" project, re-designing the architecture from scratch and ignoring the 6 months of work done on CRDB.
*   **Recommendation**: Force the "Study & Design" phase to start with a **"CRDB Architecture Alignment Workshop"** as a mandatory milestone.

## 5.2 ศึกษา สำรวจ รวบรวมข้อมูล (Data Collection & Selection)
*   **TOR Requirement**: Study, survey, and collect climate adaptation data (NAP, Domestic/International) that is reliable and useful.
*   **Audit Findings**:
    *   **CRDB Alignment**: **MAJOR REDUNDANCY.** CRDB has already completed the "Survey and Selection" phase (D-004, D-012, D-026).
    *   **Sustainability**: "Collection" implies manual file gathering (The Portal Trap).
    *   **Industrial Benchmark**: Modern enterprise systems perform **"Automated Data Discovery"** and **"Source-to-Target Mapping"** rather than generic "collection."
*   **Risk**: Spending budget on re-surveying data that is already mapped in the CRDB Recommended Dataset Registry.
*   **Recommendation**: Change scope from "Study/Collect" to **"Operationalize Ingestion for the CRDB Priority Dataset Registry."** Focus on technical connectivity (APIs) rather than manual surveys.

## 5.3 สังเคราะห์เนื้อหา (Content Synthesis & Articles)
*   **TOR Requirement**: Synthesize complex reports into articles/summaries for the general public and policy-makers.
*   **Audit Findings**:
    *   **CRDB Alignment**: Aligns with the "NCAIF v4 Narrative" but needs to be explicitly linked to the **Decision-Translation Support** need.
    *   **Sustainability**: Manual content writing is a one-time value.
    *   **Industrial Benchmark**: **"Dynamic Content Modeling"** or **"Headless CMS"** approaches allow content to be treated as data (E-032).
*   **Risk**: The system becomes a "static library" of articles that go out of date immediately.
*   **Recommendation**: Frame this as **"Content-as-Data"** creation. Ensure summaries are linked to specific CDM entities so they can be dynamically updated when the underlying data changes.

## 5.6 ออกแบบสถาปัตยกรรมระบบและฐานข้อมูล (Architecture & Database Design)
*   **TOR Requirement**: Design system architecture (Technical, Security, DB Schema) following software engineering principles.
*   **Audit Findings**:
    *   **CRDB Alignment**: Mentioning "Relational Database" and "Data Normalization" is generic. It does not mandate the **Conceptual Data Model (CDM)** entities (Hazard, Exposure, etc.).
    *   **Sustainability**: Does not specify **Decoupled Architecture** (Separating Data, Control, and Consumer planes).
    *   **Contractor Risk (Ditto)**: Ditto might lean toward a monolithic **Document Management System (DMS)** architecture which is unsuitable for high-concurrency climate services.
*   **Risk**: The database becomes a flat "Table of Files" rather than a "Graph of Climate Entities."
*   **Recommendation**: 
    1.  Redline 5.6.2 to mandate **Decoupled Architecture** (Data Space Node architecture per WIS 2.0).
    2.  Redline 5.6.4 to mandate that the Logical Schema **MUST** be an implementation of the **CRDB CDM (Anchor 2)**.
    3.  Mandate **API-First Design** as the primary interface for all DB entities.

## 5.7 ระบบบริหารจัดการข้อมูล (Content Management System : CMS & ETL)
*   **TOR Requirement**: Develop CMS for managing content, news, and reports. Includes User Auth (RBAC), Scheduling, and Metadata (5.7.5). Includes ETL for file imports (5.7.6).
*   **Audit Findings**:
    *   **CRDB Alignment**: 5.7.5 (Metadata) is "Lazy"—only asks for File Name, Date, Uploader. This fails the **"Trusted Baselines"** stakeholder need.
    *   **Sustainability**: 5.7.6 (ETL) is a **"Portal Trap"**—it focuses on "manual updates by staff."
    *   **Contractor Risk (Ditto)**: Their core competency is "e-Document/CMS." They will excel at 5.7.1-5.7.4 but likely provide a shallow 5.7.5/5.7.6.
*   **Risk**: The system requires permanent manual labor to stay updated, leading to "Data Stale-ness."
*   **Recommendation**:
    1.  **Redline 5.7.5 (Metadata)**: Mandate full **DCAT-AP / ISO 19115** compliance. Metadata must include "Data Quality Flags" and "Stewardship Pathways" (G1-G5 Gates).
    2.  **Redline 5.7.6 (Ingestion)**: Change "Manual Input" to **"Automated Harvesting (Harvester Nodes)."** The system must support scheduled API-to-API ingestion from external agencies (TMD, GISTDA, etc.).
    3.  **Governance Integration**: Mandate that the CMS workflow **MUST** implement the **G1-G5 Governance Gates (Anchor 4)**.

---

## 5.8 ระบบแสดงผลเว็บไซต์ (Frontend & Visualization)
*   **TOR Requirement**: Develop Responsive Frontend with Landing Page, Search, and Interactive Visualization (5.8.5).
*   **Audit Findings**:
    *   **CRDB Alignment**: Aligns with the **"Tiered Service Design"** and **"NCAIF Narrative"** needs.
    *   **Sustainability**: Asks for "Real-time" but doesn't specify how.
    *   **Contractor Risk (Ditto)**: Might deliver "Static Infographics" or "Standard Web Templates" instead of "Decision Support Tools."
*   **Risk**: Executives cannot use the site to justify budgets because the data isn't "Policy-Ready."
*   **Recommendation**: 
    1.  **Redline 5.8.1 (Landing Page)**: Mandate the **NCAIF v4 User Journey** (Situation -> Summary -> Resources).
    2.  **Redline 5.8.5 (Interactive)**: Mandate **"Data-Driven Storytelling Components"** (e.g., using D3.js/Mapbox) that pull directly from the CDM-linked data, not just fixed images.

## 5.9 การติดตั้งระบบ (Installation & Security)
*   **TOR Requirement**: Install the system on the Department's server, configure security, and perform validation testing.
*   **Audit Findings**:
    *   **CRDB Alignment**: Standard IT deployment.
    *   **Sustainability**: Does not mention **CI/CD pipelines** or **Containerization (Docker/K8s)**.
    *   **Contractor Risk (Ditto)**: Ditto has strong server management experience, but might provide a "manual installation" that is difficult for DCCE to maintain or update.
*   **Risk**: The system is "Hard-installed" and becomes a legacy burden that cannot be easily updated with new CRDB features.
*   **Recommendation**: Mandate **"Infrastructure as Code" (IaC)** and **Containerized Deployment**. The contractor must provide the deployment scripts (e.g., Docker Compose/Helm charts) as a deliverable.

## 5.10 การฝึกอบรมและคู่มือ (Training & Manuals)
*   **TOR Requirement**: Conduct at least 1 training for 10 people and provide Admin/User manuals.
*   **Audit Findings**:
    *   **CRDB Alignment**: Standard.
    *   **Sustainability**: One-time training for 10 people is insufficient for a national system.
    *   **Contractor Risk (Ditto)**: High capacity for training, but manuals might be "Software-focused" (how to click buttons) rather than "Domain-focused" (how to curate data).
*   **Risk**: Knowledge is lost when the 10 trained people move to other departments.
*   **Recommendation**: Mandate **"Video Tutorials"** and **"Interactive Documentation (Wiki/Knowledge Base)"** as part of the CMS. The manuals must include **Data Stewardship Workflows (G1-G5)**.

## 5.6 [Repeated] การประเมินผล (Evaluation)
*   **TOR Requirement**: Evaluate the percentage of target groups using the information. Methods must be approved by the Department.
*   **Audit Findings**:
    *   **CRDB Alignment**: Aligns with the need to prove **Utility**.
    *   **Sustainability**: Needs to be automated.
    *   **Contractor Risk (Ditto)**: Might use "Surveys" (Manual).
*   **Risk**: Evaluation becomes a one-time "fake" number for the final report.
*   **Recommendation**: Mandate **"In-system Analytics"** (e.g., Matomo/Plausible) to track actual usage of specific **NCAIF Resource** nodes and **CDM Entity** downloads.

## 5.7 [Repeated] ค่าใช้จ่าย (Costs & Responsibilities)
*   **TOR Requirement**: Consultant is responsible for all costs (meetings, experts, travel, etc.).
*   **Audit Findings**:
    *   **Sustainability**: Does not specify **Cloud/Server Hosting Costs** after the 270 days.
*   **Risk**: The project ends, and DCCE has no budget to keep the server running.
*   **Recommendation**: Mandate a **"Sustainable Hosting & Maintenance Plan"** that includes cost projections for 3 years post-handover.

---

## Step 2 Conclusion
I have completed the granular audit of **Section 5**. The primary finding is that the TOR describes a **"Static Web Build"** while the project requires a **"Sustainable Data Space."**

**Shall I now proceed to Step 3: Synthesis of Redlines (including Section 11 Personnel)?**
