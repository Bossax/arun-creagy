# Deliverables and Artifacts for Scoping and Defining an Enterprise Data Platform

## TL;DR
- When scoping an enterprise data platform, PMs and BAs produce a **layered chain of deliverables**: a business case (the "why"), a Business Requirements Document (the "what," in business terms), functional/product requirements (the "how it behaves"), non-functional requirements (the "how well"), and a family of **data-specific artifacts** (data dictionary, source-to-target mapping, data quality requirements, data lineage) plus **governance artifacts** (governance charter, stewardship/ownership definitions, data standards) — all tied together by a requirements traceability matrix.
- Authority is split by framework: **PMI** governs the business case and traceability matrix; **IIBA/BABOK** governs the requirements classification (business/stakeholder/solution/transition) and techniques such as the data dictionary and non-functional requirements analysis; **DAMA-DMBOK** governs the data and governance artifacts (charter, policies, standards, business glossary, stewardship, data quality standards, lineage).
- Ownership follows a predictable pattern: the **PM/sponsor** owns the business case and traceability oversight; the **BA** owns the BRD, FRS, NFRs, data dictionary, source-to-target mapping and user stories; the **data architect** co-owns technical mappings and lineage; and the **data governance lead/data stewards** own the governance charter, standards, ownership definitions and business glossary.

## Key Findings

1. **There is no single universally mandated document set.** BABOK, PMI/PMBOK and CMMI do not prescribe a rigid BRD/FRS/SRS structure; organizations tailor them. What *is* consistent is the *logical progression* from justification → business requirements → solution requirements → design, and the requirement (in both BABOK and PMBOK) that every requirement be traceable.

2. **BABOK's requirements classification schema is the backbone.** BABOK defines requirements as business, stakeholder, solution (split into functional and non-functional), and transition. These map cleanly onto the document chain: business requirements → business case/BRD; stakeholder + solution → FRS/PRD and user stories; non-functional → NFR documentation; transition → cutover/migration requirements.

3. **Data platforms add a distinct artifact family that generic software projects lack:** the data dictionary, source-to-target mapping (STM), data quality requirements, and data lineage documentation — plus the DAMA governance layer (charter, policies, standards, business glossary, stewardship definitions). These are what differentiate scoping a data lake/warehouse/hub from scoping an application. Their absence is expensive: Gartner's 2020 Magic Quadrant for Data Quality Solutions (Melody Chien and Ankush Jain, July 27, 2020, surveying 154 reference customers) found poor data quality costs organizations an average of $12.9 million per year.

4. **Ownership is shared and sequential, not siloed.** The BA authors most requirements artifacts; the data architect owns the physical/technical mapping and lineage; the governance lead and data stewards own the governance and standards artifacts. The PM owns the business case and traceability.

## Details

### 1. Business Case / Business Justification Document

- **What it is:** The document that justifies *why* the initiative should be undertaken. PMI (PMBOK Guide, 6th ed.) defines it as "a documented economic feasibility study used to establish validity of the benefits of a selected component lacking sufficient definition and that is used as a basis for the authorization of further project management activities." PRINCE2 defines it as "the justification for an organizational activity (project), which typically contains timescales, costs, benefits and risks, and against which continuing viability is tested." PMI frames three core components: a statement of the problem/opportunity, a conceptual solution, and a business justification for expending resources.
- **What it contains:** Executive summary; background/business need; strategic alignment; options considered (including the "do nothing" option with its costs and risks); expected benefits (financial and non-financial); cost estimates and investment appraisal; gap analysis; risks; timescales/milestones; and recommendation. It is a *dynamic* document — PMI notes virtually every section can change during the project and it should be reviewed at each go/no-go gate.
- **Who owns/authors it:** The project sponsor typically owns it; the PM (and often a BA doing the cost-benefit analysis) authors and maintains it. For a data platform, the CDO or data platform sponsor is usually the owner.
- **Who it's for:** Executives and the investment/steering committee — the go/no-go decision-makers above the project level.
- **Sequence:** First. It precedes and authorizes the project charter and all requirements work. Benefits defined here become the traceability anchors that requirements are later traced back to.

### 2. Business Requirements Document (BRD)

- **What it is:** A plain-language record of *what* the business needs and *why*, without specifying the technical *how*. BABOK defines a business requirement as "a representation of goals, objectives and outcomes that describe why a change has been initiated and how success will be assessed."
- **What it contains:** Per Slite ("Business requirements document: 7 sections"), "Every BRD needs seven sections: executive summary, project objectives, project scope, business requirements, key stakeholders, project constraints, and cost-benefit analysis." Business requirements should be numbered, testable statements each tied to an objective, with explicit scope exclusions. Many teams add assumptions, success metrics/acceptance criteria, timeline, risks, and a glossary. For a data platform, business requirements typically cover reporting/analytics outcomes, regulatory/compliance drivers, and data-consumer needs.
- **Who owns/authors it:** The Business Analyst owns and authors it, gathering from stakeholders. It captures the "Voice of Business."
- **Who it's for:** Project sponsor and senior/middle management (VP, AVP, GM, managers); it is the shared reference that aligns business and technical teams.
- **Sequence:** After business case approval, before detailed functional design. It is the bridge between the business case and the FRS. "The BRD is the *what*; the FRS covers the *how* and the detail."

### 3. Functional Requirements Specification (FRS) / Product Requirements Document (PRD)

- **What it is:** The FRS/FRD describes *how the system will behave* to meet the business needs — the granular, unambiguous functional requirements. BABOK defines functional requirements as those that "describe the behavior of the solution and the information managed... the features and functions of the system." The PRD is the product-management equivalent — a blueprint of the product's purpose, features, functionality and behavior, "concerned with the 'what' of the product," written by the product manager. Under IEEE 830, the equivalent artifact is the Software Requirements Specification (SRS).
- **What it contains:** Per IEEE 830, an SRS/FRS contains: Introduction (purpose, scope, definitions, references, overview); overall description (product perspective, functions, user profiles, constraints, assumptions/dependencies); and specific requirements (functional requirements — each uniquely identified in "shall" form; external interface requirements; performance requirements; design constraints; and quality attributes). A PRD typically contains: purpose/problem statement, success metrics, personas/target users, features and functionality (each with user stories and acceptance criteria), technical requirements (architecture, data models, integrations, performance), designs/wireframes, out-of-scope items, risks, and open questions. For a data platform (e.g., a dashboard or data product), the PRD specifies the data product's outputs, KPIs, and consumer interactions.
- **Who owns/authors it:** The BA or systems analyst authors the FRS; the Product Manager authors the PRD. Written from the user's perspective describing how the solution behaves to external users.
- **Who it's for:** The development/engineering team (to build) and QA/testing team (to derive test cases). PM reviews it.
- **Sequence:** After the BRD, before/into design and build. In waterfall SDLC this is the "Analyze" phase deliverable (alongside the RTM); the FRS elaborates each BRD requirement into granular functional detail.

### 4. Non-Functional Requirements (NFR) Documentation

- **What it is:** Documentation of the *quality attributes* — how well the solution must perform, rather than what it does. BABOK (Technique 10.30, Non-Functional Requirements Analysis) treats these as "quality of service requirements": "conditions or qualities a solution must have." They "define how well the functional requirements must perform."
- **What it contains:** Categories per BABOK/quality-attribute checklists: reliability/availability, performance (response time, throughput — static and dynamic), scalability/capacity, security, usability/operability, compatibility/interoperability, maintainability, and portability. Each NFR must include a measurable success criterion (e.g., "every page should load in 5 seconds"). For data platforms, NFRs are especially critical: data volume/throughput (ingestion rates), query/latency SLAs, retention periods, availability windows, security/access controls (RBAC/ABAC, masking, encryption), and recovery objectives.
- **Who owns/authors it:** The BA authors them; the data architect/solution architect contributes because, as BABOK notes, "the plan for implementing the non-functional requirements is detailed in the system architecture."
- **Who it's for:** Architects and engineers (who design to meet them) and QA (who test against them).
- **Sequence:** Elicited alongside functional requirements; documented within or alongside the FRS/SRS. They shape architecture and are a key input to the data quality standards and SLAs.

### 5. Data Requirements Artifacts (Data-Platform-Specific)

#### 5a. Data Dictionary

- **What it is:** BABOK Technique 10.12: "A data dictionary is used to standardize a definition of a data element and enable a common interpretation of data elements within a single data source or across multiple data sources." Also called a metadata repository. It documents **technical metadata** — the structure and content of data elements.
- **What it contains:** Per BABOK v3, for each data element: **Name** (unique), **Aliases** (alternate names used by stakeholders), **Values/Meanings** (list of acceptable values), and **Description** (definition in the solution's context). It also documents **composite data elements** — how primitives combine into composite structures using sequences (required ordering), optional elements (shown in parentheses), and repetitions/iterations.
- **Who owns/authors it:** The BA (as a BABOK technique); in a data platform, jointly with the data architect/data modeler and populated/maintained by data stewards.
- **Who it's for:** Developers, data modelers, testers, and data consumers who need a common interpretation of fields.
- **Sequence:** Built during requirements analysis and data modeling; feeds and is fed by the source-to-target mapping and the business glossary. Per DMBOK, the data dictionary is a component of the Metadata Repository (Ch. 12).

#### 5b. Source-to-Target Mapping (STM)

- **What it is:** As Hevo Data defines it ("What is Source to Target Mapping?"): "Source to Target Mapping defines how fields in a source system correspond to fields in a target system (e.g., a data warehouse). It establishes rules for transformations, naming conventions, and data flows to ensure accurate, consistent data integration, migration, or transformation." Alteryx describes it as a detailed blueprint for how data moves from one environment to another. It is the key work product for data warehouse, data integration, and data migration projects.
- **What it contains:** For each source field: source table/field and data type; target table/field and data type; the transformation rule/logic; default values; nullability; and format conversions. Per Hevo's STM guidance, teams must "Apply Naming Conventions – Standardize formats (e.g., DD/MM/YYYY vs MM/DD/YYYY)" so the required end format is unambiguous. It also captures profiling details (value ranges, blank/missing frequency) and integration frequency. STMs are typically versioned and reviewed like code.
- **Who owns/authors it:** Jointly authored by the BA (business rules) and the data architect/ETL developer (technical mapping). DMBOK lists "Data Mapping Management Tools" as a metadata source (Ch. 12).
- **Who it's for:** ETL/data engineers (who build the pipelines) and QA (who validate transformations). It is a shared reference for analysts, engineers, and business users.
- **Sequence:** After source profiling and target model definition; derived from the transformation rules in the requirements specification. Sits between the data dictionary/data model and pipeline build.

#### 5c. Data Quality Requirements

- **What it is:** Documented, measurable expectations for the fitness-for-use of data. DAMA-DMBOK (Ch. 13): "All stakeholders in the data lifecycle have data quality requirements. To the degree possible, these requirements should be defined in the form of measurable standards and expectations against which the quality of data can be measured."
- **What it contains:** Defined against the DAMA-DMBOK canonical six dimensions. Per Dataworkers ("Data Quality Dimensions: The DAMA Framework Explained"): "DAMA-DMBOK lists the canonical six (accuracy, completeness, consistency, timeliness, uniqueness, validity) and some frameworks add integrity, conformity, and reasonableness." (The broader taxonomy is large: per Dataversity, "In 2020 the Data Management Association (DAMA) developed a list of 65 data-quality dimensions and subdimensions ranging from 'Ability' to 'Identifiability' to 'Volatility.'") For each critical data element the artifact records: the applicable dimension(s), the measurement method/metric, the threshold/target, and often a data quality SLA tied to service levels. DMBOK's DQ context lists inputs including data policies/standards, DQ expectations, business rules, data requirements, and data lineage.
- **Who owns/authors it:** The BA/data quality analyst defines them; data stewards own the rules and thresholds; DMBOK notes stewards are responsible for "definition/documentation of business rules, data standards, and data quality rules."
- **Who it's for:** Data engineers (who implement checks), stewards (who monitor), and consumers (who rely on the SLA).
- **Sequence:** Defined during requirements; operationalized into DQ operational procedures and monitoring after build. DMBOK principle: quality should be "connected to service levels" and "systematically enforced."

#### 5d. Data Lineage Documentation

- **What it is:** Documentation of data's journey — where it originates, how it moves, and how it transforms across systems. DMBOK (Ch. 4): "Data flows are a type of data lineage documentation that depicts how data moves through business processes and systems."
- **What it contains:** Three complementary layers: **business lineage** (how data supports business processes/metrics and who owns them), **technical lineage** (schemas, tables, columns, SQL/transformations, ETL flows), and **operational lineage** (job logs, execution times, success/failure, volumes). Documented at a chosen granularity — system, table, column, or row level — and at either "high" or "detailed" levels (DMBOK Ch. 8). Data flows map relationships between data and applications, datastores, network segments, business roles, and locations (DMBOK Ch. 4).
- **Who owns/authors it:** The data architect and data engineers; the governance lead ensures coverage. DMBOK positions lineage across at least seven knowledge areas — as an input (Data Quality), a deliverable (Data Modeling, Metadata), and a requirement (Architecture, Integration, MDM, DW/BI).
- **Who it's for:** Compliance/audit (regulatory evidence for GDPR/CCPA), data engineers (impact analysis/root-cause), and business users (trust/verification of metrics).
- **Sequence:** Designed alongside the STM and data model; captured and maintained continuously post-build. Often begins as Excel and migrates to catalog/metadata-repository tooling.

### 6. Data Governance Artifacts

#### 6a. Data Governance Charter / Framework

- **What it is:** The foundational scoping document for the governance program. DMBOK (Ch. 3): the Charter "identifies the business drivers, vision, mission, and principles for data governance, including readiness assessment, internal process, and next steps." DMBOK's native governance deliverables include the DG Strategy, Data Strategy, Business/DG Strategy Roadmap, Data Principles/Policies/Processes, Operating Framework, Roadmap and Implementation Strategy, Operations Plan, Business Glossary, DG Scorecard, and Communications Plan.
- **What it contains:** Business drivers, vision/mission, guiding principles, scope, readiness assessment, operating model/framework, roles and decision rights, and roadmap/next steps.
- **Who owns/authors it:** The data governance lead / Chief Data Officer, ratified by a governance council/steering body.
- **Who it's for:** Executives, data owners, stewards, and the whole organization (often published via a DG website).
- **Sequence:** Established early in the program (before or in parallel with platform scoping); it frames all downstream policies, standards, and stewardship definitions.

#### 6b. Data Ownership / Stewardship Definitions

- **What it is:** Documentation assigning accountability and responsibility for data. DMBOK: "Data Stewardship is the most common label to describe accountability and responsibility for data and processes that ensure effective control and use of data assets."
- **What it contains:** Role definitions and RACI-style assignments distinguishing:
  - **Data Owner** — a senior business leader accountable for a data domain, who approves policy, sets quality expectations, controls access, and owns the budget.
  - **Data Steward** — a business practitioner responsible for day-to-day data quality, definitions, business rules, and the business glossary; DMBOK enumerates types (business, technical, coordinating, executive, chief). DMBOK: "Coordinating Data Stewards lead and represent teams of business and technical Data Stewards in discussions across teams and with executive Data Stewards."
  - **Data Custodian** — the technical role (DBA, data/platform engineer) that implements and operates the controls owners approve and stewards maintain. DMBOK treats "steward" and "custodian" as linguistically synonymous but differentiates by qualifier (business vs. technical).
- **Who owns/authors it:** The governance lead defines the framework; owners and stewards are named by the governance council.
- **Who it's for:** All data producers and consumers; auditors; the platform team (to know who approves access and definitions).
- **Sequence:** Defined as part of the governance charter/operating model, before or during platform build; a prerequisite for populating the business glossary and enforcing standards.

#### 6c. Data Standards Documentation

- **What it is:** The detailed, measurable rules that operationalize data policies. DMBOK distinguishes: "Data policies describe the 'what' of data governance (what to do and what not to do), while standards and procedures describe 'how' to do data governance." Policies are few, brief, and global; standards are the specifications.
- **What it contains:** Naming conventions (logical vs. physical names, word order, class words, abbreviations), data format/value standards, classification and handling rules, quality thresholds, security/privacy standards (RBAC/ABAC, encryption, masking), lifecycle standards (retention, archival, disposal), and interoperability standards (metadata, schemas, APIs). A **business glossary** — distinct from the technical data dictionary — is, per DMBOK, the governed "system of record for business terms related to data," owned by stewards; the data dictionary by contrast documents technical fields, formats, tables, and system structures.
- **Who owns/authors it:** Data stewards author and maintain standards; the governance lead ratifies. DMBOK: stewards handle "definition/documentation of business rules, data standards, and data quality rules."
- **Who it's for:** Every pipeline, dashboard, and API must follow them; engineers, modelers, and analysts consume them.
- **Sequence:** Derived from data policies (set in the charter); feed the data dictionary, STM, and DQ requirements. Reviewed and versioned regularly.

### 7. User Stories / Acceptance Criteria (Applicability to Data Work)

- **What it is:** A user story is a short feature description from a user's perspective ("As a [user], I want [function], so that [benefit]"); acceptance criteria are the specific, testable conditions that confirm a story is complete. They *are* applicable to data platform work — but with adaptation, because data pipeline work is often not user-facing.
- **What it contains:** Story title, the "As a / I want / so that" statement, story points, acceptance criteria (testable pass/fail conditions), and a Definition of Done. For data engineering, acceptance criteria commonly encode data-specific checks: "the CSV contains the right data," row-count reconciliation, transformation correctness, and the DoD typically includes unit tests, integration tests, performance tests, and documentation. Acceptance criteria are unique per story; the Definition of Done is universal across all stories.
- **Who owns/authors it:** The Product Owner/PM writes stories and acceptance criteria; the development team defines the Definition of Done.
- **Who it's for:** The engineering team (to build) and QA (to verify).
- **Sequence:** In agile/iterative data delivery, stories decompose the PRD/FRS into buildable increments; they sit at the bottom of the requirements hierarchy and trace up to features and business requirements. In pure-waterfall data projects, use cases or the FRS may substitute.

### 8. Requirements Traceability Matrix (RTM)

- **What it is:** A structured table linking each requirement to its origin and to the artifacts that implement and verify it. BABOK defines traceability as "the ability to track a requirement from its origin through its implementation and verification"; PMBOK treats the RTM as a key output of the Collect Requirements process. BABOK also calls it a Coverage Matrix.
- **What it contains:** For each requirement: a unique identifier, description, source/origin, priority, owner, status, and links to business needs/objectives, other requirements, design components, and test cases. It supports **backward traceability** (why does this requirement exist?) and **forward traceability** (what did this requirement produce?).
- **Who owns/authors it:** The BA maintains it; the PM uses it for scope/change/impact management. It is central to BABOK's Requirements Life Cycle Management knowledge area (Trace Requirements, 5.1).
- **Who it's for:** BA, PM, QA, and stakeholders — it demonstrates coverage (every business need → requirement → deliverable → test) and enables impact analysis for change requests.
- **Sequence:** Initiated when requirements are first captured and maintained throughout the lifecycle to go-live. In waterfall it is an "Analyze" phase deliverable alongside the FRS; in data platforms it ties business/data requirements to STM entries, DQ rules, and test cases.

## Recommendations

1. **Anchor the artifact set to three frameworks by layer.** Use **PMI** for the business case and RTM, **BABOK** for the requirements chain (BRD → stakeholder/solution requirements → NFRs → transition) and the data dictionary technique, and **DAMA-DMBOK** for every data and governance artifact. This avoids reinventing structure and gives auditors recognizable, defensible documents.

2. **Sequence the work in this order** and don't start a downstream artifact until its upstream anchor is signed off: (1) Business case → (2) Governance charter + stewardship/ownership definitions (in parallel, since governance frames everything) → (3) BRD → (4) FRS/PRD + NFRs → (5) data-specific artifacts (data dictionary → STM → DQ requirements → lineage) → (6) user stories/acceptance criteria for build → with the (7) RTM opened at step 3 and maintained throughout.

3. **Treat the four data-specific artifacts as non-negotiable for a data platform.** A generic software BRD/FRS will not surface source profiling, transformation logic, quality thresholds, or lineage — the four areas where data platform projects most often fail. Make the STM version-controlled and reviewed like code, and start lineage capture at design time rather than retrofitting it for audits.

4. **Assign ownership explicitly using a RACI.** BA = requirements artifacts; data architect = mappings/lineage/model; governance lead + stewards = charter/standards/glossary/ownership; PM/sponsor = business case + RTM oversight. The most common failure mode DMBOK flags is confusing owner/steward/custodian accountabilities — resolve this in writing before build.

5. **Distinguish the business glossary (business terms, steward-owned) from the data dictionary (technical metadata, BA/architect-owned).** Publish both in a catalog so standards are discoverable alongside the data. When "active customer" means different things to finance and marketing, standardized glossary definitions prevent the trust-destroying dashboard discrepancies DMBOK warns about.

**Thresholds that would change these recommendations:** For a small, single-source analytics build, collapse the BRD/FRS into one requirements document and skip the formal governance charter (use lightweight standards). For a regulated, multi-source enterprise platform (GDPR/CCPA/BCBS 239 exposure), treat lineage documentation and DQ SLAs as mandatory compliance deliverables, not optional.

## Caveats

- **No framework prescribes an exact template.** BABOK, PMBOK and CMMI define concepts and techniques but not a mandated BRD/FRS/SRS format; the section lists here reflect widely accepted practice, and real organizations tailor them heavily. Treat them as checklists, not contracts.
- **Terminology is overloaded.** "Business requirement," "functional requirement," and "technical requirement" mean different things in different shops; BABOK explicitly warns to publish a glossary of terms. FRS, FRD, SRS and PRD overlap substantially and are sometimes used interchangeably.
- **Several DMBOK quotations are sourced from reproductions of the copyrighted DMBOK2 text** (study aggregators and chapter sites) rather than a DAMA-hosted page; wording is faithful but exact page numbers should be verified against a physical DMBOK2 (2nd ed., 2017; Revised Edition March 2024). DMBOK 3.0 is in development.
- **DMBOK does not give "data owner" a single crisp glossary sentence** the way it defines "data stewardship"; the owner/steward/custodian distinctions synthesized here draw on DMBOK's role taxonomy plus widely-used practitioner interpretations.
- **Agile vs. waterfall changes emphasis, not existence.** In agile data delivery, user stories/acceptance criteria and a living backlog partly replace a heavy static FRS, but the underlying requirement types and data artifacts still must be produced.
- **This report deliberately excludes tooling and process/methodology** per scope; where tools (Excel, catalogs) or ceremonies are mentioned, it is only to locate where an artifact physically lives.