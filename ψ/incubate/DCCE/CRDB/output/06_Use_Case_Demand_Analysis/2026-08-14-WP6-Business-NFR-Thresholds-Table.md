# WP6 — Business NFR Thresholds Table

**Status**: Draft, pending Boss review. Not sealed — no ledger entries written.
**Scope**: The 9 high-signal services (D-043's 8 archetypal services + A-BTR), per `plans/2026-08-06-crdb-final-sprint-implementation-plan.md` WP6 and the redirection plan's §2.2 Business-NFR framing.
**Form**: Lightweight thresholds table (requirement ID, description, quantified target, priority, owner) plus short supporting narrative per service — explicitly not the full SLI/SLO/SLA/percentile apparatus (that belongs to TOR70's System NFRs).

## How to read this

Each row is a **Business NFR** — a data-freshness, compliance, quality-divergence, access-latency, retention, or semantic-consistency target CRDB is responsible for capturing (not the infrastructure-level System NFRs TOR70 owns). Owners are named against WP5's 4-tier governance model and CDM v3.0's 8 domains, not invented roles. Where a real number isn't yet knowable from this project's own material, the row is marked **TBD** with a named owner and the reason — per the redirection plan's rule against silent placeholders.

Priority scale: Critical / High / Medium / Low (mirrors the Critical/High/Medium/Low/Future use-case scale from §2.6).

---

## Service 1 — Climate Data Warehouse & Official Data Certification (คลังข้อมูลภูมิอากาศและบริการรับรองข้อมูลทางการ)

**Domain**: DOM_080 (Platform Administration) — cross-cutting; every other service's data passes through this certification layer.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-01-01 | Every certified dataset carries source, update cycle, usage conditions, and named owner before publication | 100% of certified datasets, no exceptions | Critical | Data Owner, Platform Administration (DOM_080) |
| NFR-01-02 | Every published metric maps to exactly one glossary-governed definition | 0% duplicate or conflicting metric definitions across services | High | Data Steward Team (Business Steward) |

## Service 2 — High-Resolution Area-Level Risk Analysis (การวิเคราะห์ความเสี่ยงในระดับพื้นที่ที่มีความละเอียดสูง)

**Domain**: DOM_030 (Exposure & Vulnerability), with DOM_010 (Spatial & Administrative) as a supporting domain.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-02-01 | Any sub-provincial figure shown to a user must be traceable to genuine sub-provincial source data, not silently approximated from a province-level composite | 0% unlabeled approximations — the Appendix B2 finding (composite risk index is not reversible below province level) makes this the platform's sharpest current risk | Critical | Data Owner, Exposure & Vulnerability (DOM_030) |
| NFR-02-02 | Refresh cadence for sub-provincial layers, once built (Briefs E-5/E-6) | **TBD** — depends on whether source is the 77 provincial plans (E-5, likely annual, tied to plan revision cycles) or geospatial reallocation (E-6, tied to underlying dataset refresh, not a fixed cycle of its own) | Medium | DCCE resourcing decision named in Brief E-5/E-6 (WP4 DRD) — not yet made |

## Service 3 — Financial/Budget Decision-Support Evidence (หลักฐานสนับสนุนการตัดสินใจด้านการเงินและงบประมาณ)

**Domain**: DOM_040 (Impact & Loss), with DOM_060 (Policy & Strategy) as a supporting domain.

**Note**: catalog item 3 (this service) was explicitly excluded from Functional Spec / build scope in WP1 (feasibility too low for Phase 1). NFR entries below are logged for TOR70/future-phase reference only — no functional build implied.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-03-01 | Cost, loss, and benefit figures used in any single output share one governed unit basis (currency, nominal vs. real THB, discount rate where applicable) | 0% mixed-basis figures within a single output | Critical | Data Owner, Policy & Strategy (DOM_060) |

## Service 4 — Disaster-Loss-Statistics: Assessment of Past Losses and Damages (การประเมินความสูญเสียและความเสียหาย)

**Domain**: DOM_040 (Impact & Loss). One of WP6's two priority use cases — this table's entries are the NFR half; the full Functional Spec is separate, scoped next.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-04-01 | Reporting cadence aligned to national loss-reporting obligations (Sendai Framework disclosure, referenced in D-043 Service 4's own use cases) | At minimum annual, ahead of any Sendai/BTR submission window | Critical | Data Owner, Impact & Loss (DOM_040) |
| NFR-04-02 | Restricted-access DDPM loss records (`DDPM_2_1`, `DDPM_3_2`, `DDPM_2_3`) resolve to a named requestable owner with a stated turnaround | **TBD** — no current turnaround figure exists anywhere in the project's material; needs a direct answer from DDPM, not an assumption | High | DDPM (external data provider) — request to be logged in Assumption Log |
| NFR-04-03 | Loss records naming individuals or households comply with PDPA before publication | 100% PDPA-reviewed before any record involving personal/household data is published | Critical | Data Owner, Impact & Loss (DOM_040) + DCCE legal/compliance function |

## Service 5 — Engineering Variables for Climate-Resilient Infrastructure Design (ตัวแปรทางวิศวกรรมเพื่อการออกแบบโครงสร้างพื้นฐาน)

**Domain**: DOM_020 (Hazard & Climate).

**Note**: Confirmed out of Phase 1 scope (WP4 DRD, Brief E-4 — "confirmed as a future-project workstream, not part of this launch"). No NFR targets set; logging the exclusion itself so it isn't silently dropped.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-05-01 | Engineering design-value NFRs (rainfall IDF curves, peak flow, temperature extremes) | Deferred — no target set this phase | — | TOR70 / future project, per Brief E-4 |

## Service 6 — Multi-Hazard Early Warning and Impact Monitoring (ระบบเฝ้าระวังและเตือนผลกระทบของภัยล่วงหน้าแบบพหุภัย)

**Domain**: DOM_020 (Hazard & Climate).

**Note**: Not one of Phase 1's 5 core products (WP1 §2a). This is the one service in the whole catalog whose latency need is categorically different from the rest of the platform — sensor/model/operational data on an emergency-relevant cycle, not the document-request cadence used elsewhere (named explicitly in the pre-sprint gap analysis, §3.3).

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-06-01 | Latency from sensor/model/operational source to platform availability during an active hazard | **TBD** — needs direct DDPM/meteorological-operations input; no existing figure in project material, and guessing a number here would misrepresent an emergency-response capability | High (when built) — Phase 2+, not Phase 1 | DCCE + DDPM operational teams, joint decision not yet made |

## Service 7 — National Adaptation Policy Monitoring & Evaluation Tracking (การติดตามและประเมินผลการดำเนินนโยบายด้านการปรับตัว)

**Domain**: DOM_060 (Policy & Strategy).

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-07-01 | Refresh cadence tied to the existing M&E platform's own reporting cycle (`dgf.dcce.go.th/dataset/m-and-e`, confirmed live and maintained per WP4's M&E correction) | Matches the M&E platform's own confirmed cycle — no new cadence invented | Medium | DCCE Adaptation M&E Evaluation Group (existing, already named) |

## Service 8 — National Climate Uncertainty Governance & Institutional Shield (มาตรฐานการจัดการความไม่แน่นอนและเกราะป้องกันการตัดสินใจทางการ)

**Domain**: DOM_080 (Platform Administration) — cross-cutting governance function, not a data domain of its own.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-08-01 | Every dataset or index feeding a policy or budget decision carries a stated confidence/uncertainty caveat before use | 0% of composite or modeled figures presented without a caveat — directly closes the Appendix B2 risk (composite risk index shown as certain when it isn't reversible to inputs) | Critical | Data Governance Committee |

## A-BTR — Biennial Transparency Report M&E Reporting Pipeline

**Domain**: DOM_060 (Policy & Strategy) primary, DOM_040 (Impact & Loss) supporting. WP6's other priority use case — NFR half here, full Functional Spec scoped separately.

| NFR ID | Description | Target | Priority | Owner |
|---|---|---|---|---|
| NFR-A-01 | Reporting cadence aligned to Thailand's UNFCCC Biennial Transparency Report submission | Compiled and ready ahead of each biennial deadline (WP1 §2b success criterion) | Critical | Data Owner, Policy & Strategy (DOM_060) |
| NFR-A-02 | Vulnerable-population data captured in BTR evidence units complies with PDPA | 100% PDPA-reviewed before inclusion in any BTR evidence unit | Critical | Data Owner, Policy & Strategy (DOM_060) + DCCE legal/compliance function |
| NFR-A-03 | BTR-reported figures trace to the same glossary-governed metric definitions used on the public platform | 0% parallel/conflicting definitions between BTR output and public-facing dashboards | High | Data Steward Team (Business Steward) |

---

## Open items carried to the Assumption Log (not resolved here)

1. NFR-02-02 — sub-provincial refresh cadence, pending Brief E-5/E-6 resourcing decision.
2. NFR-04-02 — DDPM restricted-access turnaround time, needs a direct answer from DDPM.
3. NFR-06-01 — early-warning latency target, needs DCCE + DDPM operational input; explicitly not guessed given the emergency-response stakes.

## Cross-references

- Governance roles: `05_Data_Management_Framework/WP5-Data-Management-Framework-Report.md` §4.2 (4-tier structure)
- CDM domains: `05_Data_Management_Framework/WP5-Data-Management-Framework-Report.md` §3.2 (8 domains)
- Service definitions: `บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (D-043)
- Service 2 resolution finding: `04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` Appendix B2, Briefs E-4/E-5/E-6
- disaster-loss-statistics blocker: same DRD, "Loss and Damage product line" entry
- A-BTR biennial deadline: `01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md` §2b
