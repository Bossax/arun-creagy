# TOR70 Amendment Recommendation —  Briefing Deck for Director Toey

Fourteen main slides plus two evidence appendices. The deck is designed as a decision package: it begins with the direction requested from DCCE, demonstrates what CRDB contributes, shows a concrete platform strategy, and then presents both a baseline delivery roadmap and a higher-ambition early-release option.

The audience should not be characterized as “non-technical.” The deck uses plain language, but retains technical substance where it explains scope, control, users, milestones, acceptance and long-term operation. It asks Director Toey to approve or sponsor the drafting direction and route it through the appropriate DCCE process; it does not assume unverified unilateral procurement authority.

Primary sources:

- [2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md](./2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md)
- [2026-08-26_TOR70-high-ambition-agile-delivery-note.md](./2026-08-26_TOR70-high-ambition-agile-delivery-note.md)
- [2026-06-11-Strategic-Alignment-Deck-Final.md](../00_Strategy_Reports/2026-06-11-Strategic-Alignment-Deck-Final.md)

---

## Slide 1 — The decision requested

**Heading:** TOR70 should be revised to protect DCCE's existing investment and deliver an operable data-service capability

**Subhead:** Today we seek approval of the drafting direction before the TOR proceeds to procurement

**Body — three principles only:**

1. **TOR70 formally adopts CRDB as its starting baseline.**
2. **DCCE approves the requirements before the contractor designs and builds.**
3. **The contractor delivers governed, operable data products and services—not only a website.**

**Bottom line:**

> The revision does not reduce the real development scope. It redirects contractor effort from repeating completed foundation work toward implementation, integration, testing and operation.

**Visual layout:** Three large numbered blocks across the slide. Bottom-line statement in a full-width band.

**Speaker notes:** Ask for agreement on direction, not approval of clause language that has not yet been drafted. Suggested opening: “วันนี้ขอความเห็นชอบต่อหลักการ 3 ข้อ เพื่อให้ทีมจัดทำร่างแก้ไข TOR รายข้อเสนอกรมพิจารณา.”

---

## Slide 2 — Why the current draft needs correction

**Heading:** The current TOR does not yet connect CRDB's foundation to the contractor's build work

**Body — three consequences:**

| Current condition | Practical consequence |
|---|---|
| CRDB outputs are not named as contractual inputs | The contractor can repeat surveys, requirements and designs from a blank page |
| Scope is organized mainly around datasets, CMS functions and web pages | Components can be delivered without proving that they work together as useful services |
| Installation, warranty and training substitute for an operating model | DCCE may receive software without clear ownership, monitoring or a repeatable update process |

**Bottom line:**

> The risk is not that TOR70 lacks software features. The risk is that those features can be delivered without becoming a maintainable DCCE service.

**Visual layout:** Three horizontal cause-and-consequence rows; avoid a maturity score on this slide.

**Speaker notes:** Frame this as continuity and investment protection, not criticism of the TOR drafter. Say “the current draft does not yet name CRDB as its baseline,” not “the contractor is ignoring CRDB.”

---

## Slide 3 — The foundation DCCE already owns

**Heading:** CRDB has already prepared much of the foundation TOR70 should verify, extend and implement

**Body — four grouped blocks:**

| Foundation | CRDB assets |
|---|---|
| **Requirements and services** | 75 developer-ready requirements, nine service business cases, stakeholder demand evidence |
| **Data foundations** | 260 catalog entries, 45-entity conceptual data model, 73-term glossary, 12-field metadata standard |
| **User-facing structure** | 38-node sitemap developed through nine iterations, supporting UX evidence and content mapping |
| **Governance and standards** | Data Owner, Data Steward and Data Custodian model; loss-and-damage minimum dataset standard tested against ten years of records |

**Bottom line:**

> These are planning, requirements and design foundations—not a finished software platform. TOR70 still needs to build, integrate, test, deploy and operationalize the system.

**Visual layout:** Four quadrants with one prominent number in each. The bottom line prevents “CRDB already built the platform” from becoming the takeaway.

**Speaker notes:** Distinguish finished, draft and deferred CRDB artifacts if questioned. Require the contractor to assimilate and verify the baseline rather than accept every artifact blindly.

---

## Slide 4 — The drafting mindset

**Heading:** Five principles keep DCCE in control of what the contractor builds

**Body — five concise rows:**

1. **DCCE owns the products; the contractor implements them.**
2. **TOR70 continues from CRDB; it does not restart.**
3. **Every dataset, dashboard and feature serves an approved user or policy need.**
4. **Governance becomes system behaviour—ownership, validation, approval and audit—not a separate report.**
5. **The contract transfers an operating capability DCCE can maintain and extend.**

**Bottom line:**

> TOR70 should procure the implementation of a DCCE-owned data-service capability built on the CRDB foundation.

**Visual layout:** Five numbered bands or a vertical progression. No supporting paragraphs on the slide.

**Speaker notes:** This applies the Product Owner and governance position already discussed with Director Toey in June; it should feel like continuity, not a newly introduced framework.

---

## Slide 5 — A concrete platform strategy

**Heading:** Build one reusable platform by putting five real products into operation

**Subhead:** Three existing analytical products are operationalized; two new services are built end to end

**Body — converging diagram:**

```text
EXISTING — onboard and operationalize          NEW — specify and build end to end
• Spatial climate-risk database                • A-BTR reporting service
• Hazard and exposure maps                     • Disaster loss-statistics service
• Climate Risk Index (CRI)

                       \                    /
                        \                  /
                         v                v
                  ONE SHARED DATA + WEB PLATFORM
       pipelines • catalog • quality • approvals • APIs
       dashboards • maps • search • downloads • monitoring
```

**Bottom line:**

> The five products are the recommended delivery anchors. Their detailed functional and data requirements must still be approved by DCCE before implementation.

**Visual layout:** Products at the top; shared capability layer beneath. Use different colors for existing and new products.

**Speaker notes:** The five products are a delivery strategy, not a replacement for CRDB's longer-term service portfolio. The remaining services stay on the future roadmap. Existing products are not rebuilt unless approved requirements identify a necessary correction.

---

## Slide 6 — What DCCE receives

**Heading:** Success means DCCE can operate the five products and add the sixth

**Body — six outcomes:**

- Three existing analytical products operating in a governed, maintainable environment
- Two new services working from real source data through to a user-facing result
- Shared pipelines, standards, interfaces and security controls proven through real products
- Named owners and repeatable processes for keeping data and products current
- Separate interfaces and responsibilities for content publishing, data stewardship and technical operation
- A tested method for onboarding the next data product without rebuilding the platform

**Operator strip at the bottom:**

| Role | Primary platform interaction |
|---|---|
| Content staff | Draft, review and publish web content |
| Data Steward | Metadata, quality, validation and publication approval |
| Data Custodian | Pipelines, jobs, errors, permissions, monitoring and backup |
| Data Owner | Authoritative status, accountability and approval |

**Speaker notes:** This corrects the TOR's implicit assumption that all back-office work is “CMS.” The functions may share a coordinated back-office portal, but their responsibilities and acceptance criteria are different.

---

## Slide 7 — The reference development lifecycle

**Heading:** Six connected stages keep requirements, design, build, testing and operation aligned

**Body — lifecycle diagram:**

```text
1. Requirements          2. Functional analysis       3. Implementation
   and approval      →       and integrated design →      Data + Web in parallel
                                                                  ↓
6. Operate, monitor   ←  5. Deploy and transfer    ←  4. Integrate, verify
   and improve              operational control          and validate
        └──────────────── feedback to requirements ────────────────┘
```

**Four decision gates:**

- requirements approved by DCCE;
- integrated solution design approved;
- combined platform validated against measurable requirements; and
- operational readiness accepted before handover.

**Speaker notes:** Call this a reference lifecycle, not a universal fixed order. It corresponds to the seven-stage model previously presented: project planning is a cross-cutting management activity, while maintenance and improvement form Stage 6 here.

---

## Slide 8 — Baseline 270-day delivery roadmap

**Heading:** The existing 270 days can be converted into four meaningful control points for DCCE

**Body — timeline:**

| Control point | DCCE should receive and verify |
|---|---|
| **Day 30** | Contractor playback of the CRDB baseline; technical interpretation report; assumptions, dependencies and requirements register |
| **Day 120** | DCCE-approved requirements for all products and platform components; integrated data/web solution design; prototype evidence |
| **Day 210** | Integrated products and shared platform in a controlled target environment; traceability and test evidence ready for acceptance |
| **Day 270** | Accepted production service; operational monitoring; trained DCCE roles; runbooks, documentation and handover |

**Bottom line:**

> Each milestone should end with an approved operating or technical baseline—not only another cumulative progress report.

**Speaker notes:** This is the baseline, non-agile correction. The formal §7 deliverables and §8 payment acceptance should be revised to match these outcomes. Payment proportions may remain unchanged if DCCE prefers.

---

## Slide 9 — Enhanced delivery option

**Heading:** DCCE can validate a working platform before the contract ends

**Subhead:** A DCCE-approved working release by day 180 leaves time to learn, correct and strengthen the final system

**Body — contrast:**

| If DCCE waits until final handover | With an early working release |
|---|---|
| Integrated usefulness is discovered near day 270 | DCCE sees the combined data and web service by day 180 |
| Feedback arrives when time and budget are nearly exhausted | Real use produces evidence while correction capacity remains |
| UAT mainly checks contractual conformity | Controlled public use also tests findability, comprehension and practical value |
| Improvements become a future procurement problem | DCCE can select the highest-value improvements inside the current contract |

**Bottom line:**

> This is a stage-gated, iterative delivery option—not unrestricted Scrum. Scope, budget, security, approvals and mandatory outputs remain controlled.

**Speaker notes:** Introduce the practical effect first; “agile-like delivery” can remain in the notes. The purpose is not to teach agile terminology but to let DCCE learn from working software before final acceptance.

---

## Slide 10 — Enhanced 270-day cycle

**Heading:** A working release at day 180 creates a controlled improvement window inside the same contract

**Body — timeline:**

```text
DAY 1–30       DAY 31–120          DAY 121–180          DAY 181–210
Assimilate     Approve requirements Build and integrate  Controlled public beta
CRDB baseline  + design + prototype DCCE working release usage evidence + backlog
                                                               │
                                                               v
DAY 270        DAY 251–270         DAY 211–250          AROUND DAY 210
Final          Production release  Selected improvements DCCE prioritizes backlog
acceptance  ←  and handover      ←  + security hardening within reserved capacity
```

**Release gates:**

1. DCCE approves requirements before build.
2. DCCE validates the integrated working release before public beta.
3. Security and operational-readiness criteria must pass before beta.
4. DCCE selects which feedback items enter the remaining implementation window.

**Speaker notes:** The day-180 release should include representative end-to-end products, real approved data, functioning governance workflows and the web interface. It is not merely a wireframe or clickable prototype.

---

## Slide 11 — Safeguards for the enhanced option

**Heading:** Early feedback improves the result without turning the TOR into unlimited scope

**Body — six safeguards:**

1. **Mandatory scope remains fixed.** Every required TOR capability must still be delivered.
2. **Feedback cannot replace contractual outputs.** It can refine or strengthen them within agreed boundaries.
3. **DCCE controls prioritization.** User requests become a managed backlog; the contractor does not choose the product direction alone.
4. **Improvement capacity is capped.** The TOR reserves defined person-days, sprint capacity or a fixed implementation window.
5. **Release is gated.** Security, privacy, data quality, rollback and incident procedures must pass before controlled public use.
6. **Unselected requests remain visible.** They become a documented roadmap rather than informal promises or unpaid scope.

**Bottom line:**

> Same 270-day duration and ฿12.5 million ceiling; effort is reorganized so that learning occurs before the final release.

**Speaker notes:** Do not promise “no cost.” Assimilation, beta support and improvement work consume contractor effort. The proposition is that the same budget is allocated differently and more effectively.

---

## Slide 12 — What must change in TOR70

**Heading:** The recommendation changes specific contractual mechanisms—not the entire build scope

**Body — amendment map:**

| TOR area | Required correction |
|---|---|
| **§5.1–§5.2** | Name CRDB artifacts as inputs; require contractor assimilation, playback, requirements traceability and formal DCCE requirements approval |
| **§5.3–§5.4** | Adopt and verify the CRDB catalog and models; complete product specifications, physical design, contracts, environment separation and integrated data/web design |
| **§5.5–§5.6** | Build coordinated end-to-end products; separate content-management, data-operation and technical-administration responsibilities |
| **§5.7** | Establish development, test, staging and production environments; controlled promotion, rollback and—if approved—public-beta deployment |
| **§5.8–§5.9** | Add measurable acceptance criteria and two release gates: working-release/beta readiness and final production acceptance |
| **§5.10 and §15** | Add operating ownership, monitoring, runbooks, incident handling, change management and post-launch evidence—not warranty alone |
| **§7–§8** | Align deliverables and payment acceptance with approved baselines, working integrated results and operational readiness |

**Speaker notes:** Follow this briefing with a clause-level redline matrix containing current wording, proposed wording, deliverable, acceptance evidence, owner and milestone. The main deck approves the direction; the redline package executes it.

---

## Slide 13 — What DCCE must own

**Heading:** DCCE does not need to build the system, but it cannot outsource product ownership

**Body — three responsibilities:**

### 1. Approve what will be built

DCCE approves the functional, data, content, governance and non-functional requirements before implementation.

### 2. Assign who owns and operates it

DCCE routes the appointment of appropriate Product Owners, Data Owners, Data Stewards, Data Custodians and operational administrators.

### 3. Accept evidence—not promises

DCCE reviews working products, test results, operating procedures and measurable acceptance evidence at the contractual gates.

**Bottom line:**

> The contractor supplies technical capability; DCCE retains authority over purpose, requirements, acceptance and long-term direction.

**Speaker notes:** Do not overload this slide with individual product-policy decisions. Those decisions belong in the requirements-approval process and should be routed to the correct authority when they become relevant.

---

## Slide 14 — Decision and next action

**Heading:** Approve the drafting direction and authorize preparation of the clause-level TOR70 amendments

**Body — three blocks:**

**Approval requested today**

> Confirm the three principles from Slide 1 and whether the enhanced day-180 working-release option should be included in the redraft.

**What the team prepares next**

> A clause-by-clause amendment package showing current wording, proposed wording, deliverable, acceptance evidence, responsibility and milestone impact.

**How the decision is closed**

> Set a review date for DCCE to approve, revise or route the proposed clause language before procurement.

**Visual layout:** Three centered blocks matching Slide 1. The enhanced option can be approved, rejected or held as an alternative without weakening the baseline amendments.

**Speaker notes:** If an immediate direction is not possible, leave with a named route and fixed review date. Do not ask for decisions on every product requirement during this meeting.

---

# Appendix A — Structured lifecycle assessment

## Appendix Slide A1 — Coverage estimates

**Heading:** The structured assessment confirms that the largest gaps sit before build and after handover

| Reference stage | TOR70 as written | With CRDB adopted |
|---|---:|---:|
| Requirements Elicitation & Analysis | ~35% | ~70% |
| Functional Analysis & Solution Design | ~40% | ~80% |
| Implementation | ~45% | ~50% |
| Integration, Verification & Validation | ~65% | ~70% |
| Deployment & Operational Transition | ~65% | ~70% |
| Operations, Maintenance & Improvement | ~12% | ~30% |
| **Overall estimate** | **~45%** | **~62%** |

**Required qualifier:** These are structured assessment estimates derived from scored lifecycle activities, not statutory compliance scores or an objective percentage of project completion.

**Speaker notes:** Use only if asked how the analysis was quantified. The method scores each constituent lifecycle activity as present, partial or absent. Keep the full scoring method in the storyline note.

---

## Appendix Slide A2 — Evidence and continuity

**Heading:** The recommendation extends positions already established through CRDB

**Evidence blocks:**

- June strategic alignment: DCCE as Product Owner; CRDB as planning, requirements and design; TOR70 as system design and implementation.
- FGD3 roadmap: assign ownership and stewardship, establish standards and inventory, then operationalize the catalog and embed governance in future TORs.
- TOR70 review: build and testing scope remains necessary; duplication is concentrated in requirements and design.
- Industry reference: requirements and baseline first; coordinated data/web design; integration and validation before production; operational feedback after launch.

**Speaker notes:** This slide is for continuity questions. It demonstrates that the briefing applies prior CRDB recommendations to TOR drafting rather than introducing a disconnected methodology.
