# CRDB Consultation Workshop — Master Design v2

## Purpose

This document reframes the CRDB consultation workshop after the DCCE internal review captured in [`ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md:59).

It replaces a heavy co-creation assumption with a more realistic **guided validation + guided expansion** format:

- participants validate what already exists
- participants react to 4 prepared MVP/service concepts
- participants add missing service or product ideas from their own operational reality
- participants hear peer ideas and refine their own proposals

This is a **working design v2** for review before detailed facilitation materials are produced.

---

## Strategic shift from the previous design

### Previous risk

Earlier designs leaned too heavily toward full co-creation or system-engineering behavior, which assumed:

- participants were comfortable thinking like service designers
- participants had enough technical confidence to invent new system concepts from scratch
- the room could move directly from ecosystem framing to structured platform/service generation

### Updated stance

The updated workshop should instead behave like a **guided learning circle**:

1. show what data and information products already exist
2. validate and correct that picture with participants
3. show 4 prepared MVP/service concepts grounded in real use cases
4. let participants extend, critique, and add to those concepts
5. compare proposals across groups and surface common priorities and barriers

This matches the new meeting note direction in [`ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md:61).

---

## Core design principles

### 1. Use-case first

Every discussion must be anchored in practical jobs, decisions, or workflows rather than abstract technology choices.

### 2. Validate before inventing

Participants should first react to visible assets and prepared concepts before proposing new services.

### 3. Mixed-literacy safe

The design must work for a mixed room of technical, managerial, and sectoral participants.

### 4. Service layers, not just datasets

The workshop must help participants see the difference between:

- raw or underlying data assets
- visible products and services
- guidance, workflow, and policy-support layers

### 5. Peer learning is required

Each group should not only produce ideas; they should also review and respond to peer proposals.

---

## Proposed workshop logic

## Morning sequence

### Morning Activity 1 — Existing Data and Information Product Landscape Validation

#### Objective

Help participants understand the current ecosystem of:

- data assets
- information products
- dashboards and visual tools
- data catalog or discovery services
- operational and decision-support services

Then validate what is missing, misclassified, duplicated, or weak.

#### Why this activity matters

The new meeting note explicitly expects a **Data Landscape Map** plus a visible discussion of existing analytics platforms and catalog-like systems in [`ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-04-30-meeting-note-on-crdb-workshop.md:21).

This activity gives all participants a shared baseline before discussing future services.

#### Inputs provided to participants

- a large wall poster showing the current landscape map
- a simplified product/service reference handout
- a simplified data-asset reference handout
- table worksheets for corrections and additions

#### Participant task

Each group reviews the current landscape and answers:

1. what services, products, or datasets do you already know or use
2. what is missing from this picture
3. what is wrongly categorized or misleadingly described
4. what is most useful already
5. where are the biggest blind spots or weak areas

#### Recommended table output structure

Each group should record findings in 4 capture columns:

| Item seen on the map | Keep / correct / add | Why | Owner or source if known |
|---|---|---|---|

#### Expected outputs

By the end of Activity 1, the workshop should produce:

1. a corrected current landscape of products and services
2. a corrected view of key data-asset families
3. a list of missing or under-recognized products
4. a shortlist of weak points in the current ecosystem

---

### Morning Activity 2 — Guided Service and Product Expansion

#### Objective

Use 4 prepared MVP/service concepts as anchors, presented as **alternative Service Levels (Level 1: Pragmatic Proxy vs. Level 2: Ideal Full-Service)**, to let participants:

- evaluate which level provides more **Decision Utility** for their specific tasks
- critique the technical logic (e.g., Climate Allowances vs. Risk Narratives)
- suggest missing add-ons or sectoral impact indicators (Agri, Health, Transport)
- identify practical barriers to adopting either level

#### Why this activity matters

This activity shifts the room from "feedback on a portal" to **"co-production of service standards."** It forces participants to define what level of detail they actually need to act with confidence.

#### Anchor concepts to present

Each MVP is presented using a coherent **"Three-Box" framework** (Problem-Concept-Journey):

1.  **MVP-1: Policy Briefing Service (The Exporter)**
    *   **Logic**: Level 1 (Provincial Qualitative Trends) vs. Level 2 (Municipality-level **Climate Allowance** safety margins).
2.  **MVP-2: Disaster Data Pipeline (The Intake)**
    *   **Logic**: Level 1 (Spreadsheet-based Reliability Flags) vs. Level 2 (**Common Sectoral Impact Schema** for automated Agri/Health/Transport L&D).
3.  **MVP-3: Endorsed Data Inventory (The Catalog)**
    *   **Logic**: Level 1 (Curated Link Directory) vs. Level 2 (Automated "Single Source of Truth" with official agency endorsement).
4.  **MVP-4: Uncertainty Data Shield (The Interpreter)**
    *   **Logic**: Level 1 (**Decision Readiness Labels**, e.g., "Verified for Budgeting") vs. Level 2 (Statistical Model Confidence Intervals).

#### Input provided to participants

- **MVP "Dummy" Artifacts**: 1 page per MVP showing both Service Levels side-by-side.
- Each dummy shows:
  - **Box 1 (The Pain Point)**: The "Operational Anchor" (the specific work-moment when this is used).
  - **Box 2 (The Concept)**: What the service provides at Level 1 (Pragmatic) vs. Level 2 (Ideal).
  - **Box 3 (The User Journey)**: A 3-step storyboard of "How I act with this output."

#### Activity flow

### Phase A — Framing and Service Level Presentation

Facilitator message:

- We are presenting two ways each service could look.
- **Level 1 (The Pragmatic)**: Works with today's data and administrative summaries.
- **Level 2 (The Ideal)**: High-resolution engineering and automated data flows.
- **Your Task**: Focus on **Decision Utility**. Which version allows you to make a decision with more confidence?

### Phase B — Table discussion on the 4 MVP anchors

Each group discusses each MVP using a **Decision Utility Matrix**:

| MVP Concept | Which Level is most useful? | Why? (Specific decision supported) | What technical logic is missing? |
|---|---|---|---|

### Phase C — New service/product proposal

Each group may propose up to **2 additional desired services or products**.

Every proposal must specify the **Service Level** it aims for:

| Proposed service / product | Intended users | Problem or task supported | Service Level (1 or 2) | Data or systems needed |
|---|---|---|---|---|


#### Allowed product forms

To keep ideation comparable, groups should choose from a limited set:

- dashboard
- map / GIS tool
- data catalog / discovery layer
- report / export pack
- workflow or reporting template
- alert / warning service
- guideline / methodology / support content

### Phase D — Peer review round

Each group posts its top proposals on the wall.

Other groups rotate and react with 3 types of feedback:

1. **Useful for us too**
2. **We know something similar already**
3. **Hard to implement because...**

This is essential because the revised design should allow each group to hear peer ideas and refine its own proposal.

### Phase E — Return and refine

Groups return to their own poster after peer review and revise their top proposal.

### Phase F — Short plenary reporting

Each group reports only:

1. one refined service/product idea they support most
2. one main blocker
3. one thing DCCE should do first

#### Expected outputs

By the end of Activity 2, the workshop should produce:

1. structured feedback on the 4 anchor MVPs
2. a shortlist of new or modified service/product ideas
3. cross-group signals on which ideas are shared, duplicated, or high-value
4. a first list of practical implementation barriers

---

## What must be prepared before the workshop

## Preparation block A — Materials for Activity 1

1. **Landscape map poster v1**
   - two-band structure: services/products on top, data-asset families underneath
2. **Condensed product/service handout**
3. **Condensed data-asset handout**
4. **Activity 1 correction worksheet**
5. **legend for the poster**
   - what color means
   - what shape means
   - how to mark missing / weak / incorrect items

## Preparation block B — Materials for Activity 2

1. **4 MVP/service concept cards**
   - simple, non-technical wording
   - one page or one slide each
2. **Activity 2 table worksheet — MVP reaction matrix**
3. **Activity 2 table worksheet — new service/product proposal sheet**
4. **peer review stickers or comment slips**
   - useful for us too
   - similar already exists
   - hard to implement because
5. **short reporting template for plenary**

## Preparation block C — Facilitation and room setup

1. group seating plan
2. printed instructions per table
3. clear timeboxing for each sub-round
4. rapporteur note template for facilitators
5. wall space for gallery review and refined concepts

## Preparation block D — Analytical prep still needed after this session

1. finalize the landscape map structure
2. normalize the product/service groupings from [`data_product_and_service_2026-2.csv`](ψ/incubate/DCCE/CRDB/inbox_source/data_product_and_service_2026-2.csv:1)
3. clean the encoding of [`data_product_and_service_2026.csv`](ψ/incubate/DCCE/CRDB/inbox_source/data_product_and_service_2026.csv:1) if detailed Thai labels are needed
4. define exactly what “validation” means operationally in the session
5. write the facilitator script and reporting instructions

---

## Boundary conditions and design cautions

### 1. Do not over-technicalize Activity 2

Participants should not be asked to design backend architecture or database logic.

### 2. Do not let new ideas become vague wish lists

Every proposed service/product must have:

- intended users
- practical task
- product form
- required inputs
- main implementation barrier

### 3. Do not let peer review become a second plenary

Peer exchange should happen through a tightly structured gallery or swap review, not through long speeches.

### 4. Keep the outputs comparable across groups

All groups must use the same worksheet logic, otherwise synthesis will become weak.

---

## Immediate deliverables from this design stage

This master design v2 should be used as the parent document for the next planning tasks:

1. landscape map poster structure
2. product/service handout structure
3. Activity 1 correction worksheet
4. Activity 2 MVP reaction worksheet
5. Activity 2 new service/product proposal worksheet
6. peer review prompt sheet
7. plenary reporting template

---

## Current status

This document is a **design freeze candidate for review**, not yet the final facilitation pack.

The next session should tackle the remaining to-do items one by one and convert this design into concrete workshop materials.
