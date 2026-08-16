# Policy and Technical Recommendations for Developing Thailand's Climate Adaptation Data Products and Services

**Date:** 16 August 2026

**Status:** Draft, pending review. English working version. The Thai submission text is a separate, later step.

## Purpose

This report sets out what should happen next. It covers how DCCE should develop and own the data products and services on the national climate adaptation platform, how accountability for data should be structured, what each output of this project needs in order to become a working part of the system, and in what order the work should proceed.

The recommendations here build on the work completed across this project. The platform's information architecture and site structure are designed. The conceptual data model, glossary, and metadata standard are built. The baseline dataset and information product inventories are complete. Business cases exist for all nine planned services. A minimum dataset standard for disaster loss and damage has been drafted and tested against real records. What follows describes how that body of work moves into production, and who should carry each part of it.

---

## 1. How DCCE Should Develop Its Data Products and Services

DCCE should hold continuous ownership of the platform and everything on it, across contracts and across phases. That ownership sits with the department rather than with any party it hires, because DCCE is the party that sits closest to the people who depend on this data and is best placed to judge what they need.

In practice this means DCCE gathers the requirements, decides what gets built first, and writes down what each product and service is meant to do before development begins. A contractor builds well when it is told clearly what to build. DCCE should give that direction, review work while it is underway, and carry the same role into every phase that follows.

The work divides into seven stages. Planning, requirement analysis, and design have been completed in this project. Development, testing, deployment, and ongoing maintenance come next. DCCE's ownership runs across all seven, including the last one, since a platform earns its value in the years after launch rather than on the day it opens.

Development should not wait for a finished product before it is tested by the people who will use it. This is standard practice in government digital delivery elsewhere. The UK government's digital service guidance structures a build into discovery, alpha, beta, and live phases, where alpha tests candidate approaches, beta releases a working version to real users first in a private group and then more widely, and each phase closes with an assessment before the next begins. A contract for this platform can require the same shape directly — asking for two build iterations rather than one, with a beta milestone partway through the project where a working version reaches real users. That version runs for a period with the audience it is meant to serve, and the feedback gathered through surveys, workshops, and interviews becomes the prioritized backlog the contractor addresses in the following build cycle. This suits data platform work particularly well now, when the pace at which usable software can be built and revised has shortened considerably.

DCCE should also position itself as the party that sets standards and certifies climate information for Thailand. Raw observations and modelling stay with the agencies that already produce them well, including the meteorological department and GISTDA. DCCE's contribution is to decide what gets certified, what gets built into a usable product, and what a planner or a bank can rely on when they take a figure from the platform and act on it.

---

## 2. Data Governance and Accountability

Every data domain on the platform should have two named roles. A Data Owner, appointed at Group Director level, holds the authority to approve what gets published from that domain. A Data Steward, appointed by that Data Owner from operational staff, handles day to day quality checking and keeps the documentation current.

This structure serves both sides of the platform. It covers the products and services DCCE builds itself, since each one needs someone who can confirm what it claims. It covers the datasets that arrive from other agencies, since those need named ownership once they sit inside DCCE's system and get presented under DCCE's name.

Certification follows from this. Once a domain has an owner and a steward, it can begin producing datasets marked as official and citable references. DCCE should establish a governance committee drawing on the Data Owners themselves, with the authority to review datasets and grant that status. The platform's catalog currently holds 260 entries, all of them awaiting exactly this kind of review, so there is a well defined body of work ready for the committee once it convenes.

The same approach extends outward to the agencies DCCE depends on. Six organisations together hold about half of everything in the catalog, including the meteorological department, GISTDA, the disaster prevention department, the national statistics office, and the national economic and social development council. DCCE should work toward standing agreements with these partners, settling in advance what data moves, on what schedule, and in what form. Agreements at that level free staff on both sides from negotiating each request individually and give the platform a dependable supply.

Governance of this kind is what allows a platform to stay trustworthy for years rather than months. Named ownership keeps data current. A published standard governs what automated tools may draw on when they generate summaries or answer questions, which keeps the platform's outputs defensible as those tools become more common in government service delivery.

---

## 3. Datasets, Products, and Services. What Comes Next

This project produced four bodies of work that are ready to be carried forward. Each needs a specific next step and a named role to take it.

### Service definitions

A business case now exists for each of the nine services identified through this project as high signal, in that each addresses more than one use case, covering the problem, the evidence behind it, the value of solving it, and what currently stands in the way. The next step is a functional specification a developer can build from. A business analyst should produce this, and DCCE's own owner for each service should review and approve every requirement it contains. That review is what keeps the built service aligned with what the department actually intends.

Four decisions would strengthen this work if taken early. The scope of the non-financial loss categories, covering mental health, biodiversity, and cultural heritage, shapes what the loss and damage service is specified to do. Whether to extend the existing national monitoring platform or build a replacement shapes the policy tracking service. Where the impact based warning service belongs in the site structure shapes both its design and its content. Each of these is a decision for DCCE rather than for an analyst to settle.

### Website content

The site structure is designed and approved, and all 73 content requirements across it have been checked against DCCE's existing material. Twenty one are ready to publish today. Twenty four have supporting material that is missing a specific piece. Twenty eight need to be created. A content lead working alongside a designer should turn this into a production plan naming who writes each piece and by when, sequenced so that the pages with material ready go live first.

### The data catalog

The baseline dataset and information product inventories are complete and organised against the international risk framework the platform uses throughout. Bringing these to certified status is continuing work rather than a single task, and it belongs to the Data Stewards described in section 2, working domain by domain. Access conditions deserve attention alongside certification, since a large share of the catalog is currently restricted at dataset level and a majority is restricted even at the level of its description.

### Loss and damage recording

The minimum dataset standard and reporting form are the furthest developed outputs of this project. Both have been tested against ten years of village level disaster records from the Department of Disaster Prevention and Mitigation. That test showed the standard works for event and impact records, and identified one specific piece of engineering still to do. Financial disbursement records are held in aggregate form and cannot yet be matched to individual disaster events. A data engineer, working with someone who can coordinate directly with that department, should build the ingestion pipeline and resolve that link. Because this work starts from a tested standard rather than a design on paper, it is the shortest path from this project to something running in production.

One question sits ahead of the calculation side of that service. A national methodology for valuing disaster losses is under development elsewhere in government, and confirming whether it can serve as this platform's official calculation method would let the engineering proceed with certainty.

---

## 4. System Development and Technical Standards 

The conceptual data model, the shared glossary, and the metadata standard are complete. The metadata standard defines twelve required fields aligned with ISO 19115 and with the Digital Government Development Agency's national guideline. The next step is to make these operate automatically. A Technical Steward should turn them into validation rules enforced by the content management system, so that meeting the standard becomes part of publishing rather than a separate review. Changes to the underlying model should go to the Data Governance Committee for approval, which keeps the model stable as the platform grows and different teams contribute to it.

Written data exchange agreements with source agencies follow from that foundation. Each agreement should state what data moves, how often, in what format, and who to contact when something changes. These are governance instruments rather than technical ones, so the committee should approve their content.

Two clarifications would make this work more precise. Deciding how datasets should be classified for licensing determines how much of the catalog can be shared and under what terms, and it is a prerequisite for opening a meaningful share of it. Confirming whether the formats recorded in the catalog describe how data is delivered today, or a target not yet reached everywhere, would let pipeline design proceed on firm ground.

Alongside these, DCCE should publish national technical standards in the areas where a specific service is already waiting on one. This is not the full list of methodology work ahead, and none of it needs to land at once. The order in which these four areas, and the further gaps described in the accompanying gap analysis, get taken up is a decision for the Data Governance Committee to sequence against the platform's build timeline.

- **Interoperability.** Standards covering automated interfaces, data exchange formats, version management, and access control let other agencies pull data into their own systems reliably.
- **Risk assessment methodology.** A national catalog of risk assessment methods, with guidance on which method suits which context, keeps local planning from resting on an unsuitable approach.
- **Converting science into decision inputs.** Methods for turning climate variables into engineering parameters and economic loss values give every sector a common reference to work from.
- **Communicating uncertainty.** Standards requiring confidence ranges, model limitations, and a plain language explanation of what a projection does and does not say help institutional users act on probabilistic information with appropriate confidence.

These four are not the only methodology gap. The gap analysis also identifies missing methods for weighing costs against benefits, classifying climate-related spending, and valuing avoided losses, none of which is covered above. Committee sequencing should draw on that fuller list rather than stopping at these four.

This work needs capabilities DCCE should build up. Specialists in risk engineering, environmental economics, and data science are needed to keep translating climate data into products people can use. The platform will need cloud infrastructure sized for genuine interface traffic. International climate finance is worth pursuing as a route to fund that infrastructure across the longer term.

---

## 5. Sequencing

The strongest early investment is in standards and ownership rather than in acquiring new data. Data added before the structure is ready meets the same handling constraints as everything already in the catalog. Standards and named ownership first, then access and machine readability, then targeted expansion of supply gives each stage something solid to build on.

### First six months

- Publish the metadata standard, the data model, and the glossary as departmental standards.
- Appoint Data Owners at Group Director level, and have each of them assign Data Stewards.
- Formally establish the Data Governance Committee.
- Complete an inventory of the datasets and data products each work group currently holds.

### Beyond the first year

- Bring the internal data catalog into live use, so that assets and services support routine work such as report preparation and new product development.
- Write data governance requirements into the scope of future development work, so that anyone building for DCCE delivers to the department's standards.
- Use the published standards as the basis for the standing agreements with source agencies described in section 2.
- Extend technical data management policy to cover the full data lifecycle across every climate domain.

Budget allocation should reflect this order. Setting aside funding for product research and design work, covering methodology development, engagement with the people who will use each service, and prototyping to a working state, ahead of software construction gives the development work a firm specification to build against and reduces the amount of rework later.

---

## Appendix. Internal Traceability

*For project use. Not required reading for the recommendations above.*

- Section 1 draws on the Strategic Alignment Deck of 11 June 2026, slides 7, 8, 10, 15, and 16, and carries forward the strategic positioning argument from section 5 of the June recommendations draft.
- Section 2 carries forward sections 1 and 4 of the June recommendations draft, with the role structure and lifecycle phases confirmed against the WP5 Data Management Framework report and slide 17 of the Strategic Alignment Deck.
- Section 3 draws on the WP6 Service Business Narratives, the WP4 Content Source Gap Analysis (73 requirements, 21 full, 24 partial, 28 gap), the baseline and information product inventories at report sections 5.3.4 and 5.3.5, and the minimum dataset pilot test at report section 5.3.7. It carries forward section 2 of the June recommendations draft.
- Section 4 carries forward sections 3 and 6 of the June recommendations draft, with the metadata field count and standards alignment taken from report section 5.3.4.
- Section 5 carries forward section 7 of the June recommendations draft, with the sequencing rationale drawn from the gap prioritisation analysis prepared alongside it.
- Open decisions referenced in sections 3 and 4 are recorded in full in the gap analysis report of 16 August 2026, section 5. Only those that gate a specific next step are named here.
