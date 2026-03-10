---
status: current
tags:
  - FGD2
  - NCAIF
  - slide-deck
created: 2026-02-27
last_updated: 2026-03-06
project:
  - DCCE_CRDB
type: artifact
---

# FGD2 slide deck guide (2h30) — structure + speaker notes

## Objective (what the deck must accomplish)

1. Create continuity with FGD1 (“you said → we did”).
2. Demonstrate **progress** on CDM/NCAIF using tangible activities (A1/A2).
3. Collect **feedback** on internal operational use cases and governance phasing.
4. This session does **not** finalize decisions.

**Update note (2026-03-05):** This guide now includes:

- interview plan + status (Slide 5)
- CDM explanation with design principles + key decisions (for buy-in)
- exact Mentimeter questions (multiple choices)
- one-slide-per-journey user-journey demos (3 personas)
- governance phasing narrative integrating DGA recommendations

## Deck pacing (map to agenda)

Use this as a timing checklist; the deck is a facilitation tool, not a report.

- 0:00–0:20 Context recap + continuity bridge
- 0:20–0:45 A1: Mentimeter CDM activity
- 0:45–1:10 A2: Internal use-case walkthrough
- 1:10–1:25 A3: Governance phasing plan (data quality framing)
- 1:25–1:45 Feedback capture + close

## Suggested slide outline (with speaker notes)

### Slide 1 — Title + outcomes

**Title:** FGD2 — Internal progress demo + feedback

**Show:** 3 bullets only:

- Demonstrate CDM/NCAIF progress
- Collect feedback on internal use cases
- Surface gaps and next steps

### Slide 2 — Why we are here now

**Speaker note:** FGD2 exists to share progress and gather feedback before formal decisions.

### Slide 3 — Constraints (Phase 1 reality)

**Show:** 4 constraints, plain language:

- Data is not real-time
- Boundaries differ
- Technical literacy varies
- Some data is sensitive

Source anchors: [`src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md`](01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md)

### Slide 4 — FGD1: what you said (pain points)

**Show:** 6–8 bullets (terminology mismatch, language too technical, preview, QA/QC, PR review, etc.)

Source: [`FGD 1 result.md`](src/01_Projects/2025-11_DCCE-CRDB/output/FGD 1 result.md:56)

### Slide 5 — Interviews: plan + current status (and how they feed the design)

**Purpose:** make the evidence trail explicit: “who we talked to → what we changed”.

**Show (visual):** 1 simple table + a progress bar.

**Suggested table (example wording; update counts as needed)**

| Category                                | Agencies                  | Status    | What we extract                                                                   |
| --------------------------------------- | ------------------------- | --------- | --------------------------------------------------------------------------------- |
| Data governance + national platforms    | DGA                       | Completed | Open vs non-open rails (data.go.th/GDX), classification service, KPI implications |
| Local operations + post-event reporting | DDPM, DLA                 | Completed | Event reality (lag/noise), schema needs, boundary pain                            |
| Baselines + statistics                  | NSO                       | Completed | Link-first stance, baseline references                                            |
| Planning + projections                  | OTP, NESDC, NXPO          | Completed | Official baselines, uncertainty-safe publishing, investment workflows             |
| Private-sector advanced users           | Thai Bankers' Association | Completed | Probabilistic data semantics + misuse risk                                        |

**Speaker note:** “We don’t treat interviews as anecdotes; we translate them into workflow patterns + MVPs + governance gates.”

Sources:

- Use cases inventory: [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)
- DGA summary: [`Interview Summary - DGA.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - DGA.md:1)

### Slide 6 — What we changed: “You said → we responded” (continuity bridge)

**Show:** 1 table (FGD1 feedback → design responses).

Suggested rows:

- Terminology mismatch → Glossary + definitions authority + limitations statements
- Need preview-before-download → Data catalog preview standard (schema + sample + owner)
- Data not real-time → freshness + revision history + validation flags
- Boundary confusion → canonical boundaries + crosswalk guidance (spatial reference module)
- PR/publishing bottleneck → draft → review → publish workflow

Source anchor (continuity): [`FGD2_plan_2026-02-26.md`](src/01_Projects/2025-11_DCCE-CRDB/notes/FGD2_plan_2026-02-26.md:1)

### Slide 7 — CDM explained (design principles + key decisions)

**Purpose:** secure buy-in by showing that the CDM is a *pragmatic engine* that supports workflows.

**Show (visual):**

1) the updated ERD diagram (Subject Areas 1–2) and
2) a small “design principles” box.

**Exact wording (speaker notes):**

- “The CDM is not a database implementation; it’s a **shared blueprint** for what we must be able to record consistently.”
- “We structured domains this way because it mirrors how decisions are made: **Cause → Map/Assessment → Products**.”

**Design principles (bullet box):**

- **Observed vs modeled separation:** hazard maps can be modeled or observed (satellite).
- **Dual-path risk assessment:** physical maps and index-based assessment both fit the same structure.
- **Loss-driven attribution:** attribution is only asserted when loss evidence exists.
- **Governance-visible outputs:** every published indicator includes limitations/uncertainty.

References:

- Key decisions + logic: [`Detailed_CDM_Design.md`](src/01_Projects/2025-11_DCCE-CRDB/output/Artifact%20v1/Detailed_CDM_Design.md:276)
- Human-readable decisions context: [`Conceptual Data Model for climate risk and adaptation data system.md`](src/01_Projects/2025-11_DCCE-CRDB/task/Conceptual Data Model for climate risk and adaptation data system.md:10)

### Slide 8 — A1 Mentimeter activity: CDM domain prioritization (exact questions)

**Purpose:** collect prioritization signals, not finalize the model.

**Set-up line (exact):**

> “If we can only make 1–2 domains work well this year, which domains must be correct first to unlock real value?”

**Mentimeter question set (pick 3–5)**

1) **Ranking (mandatory)**
   - “Rank these from most urgent to least urgent for Phase 1:”
     - Hazard maps (observed + modeled)
     - Risk assessment outputs (indices + metrics)
     - Post-event impact reporting (event + impact schema)
     - Boundaries + spatial reference (canonical boundary + crosswalk)
     - Data catalog + recommended baselines

2) **Multiple choice**
   - “Which statement best matches your experience?”
     - A) Our biggest pain is *finding* datasets.
     - B) Our biggest pain is *trusting* datasets.
     - C) Our biggest pain is *interpreting* datasets correctly.
     - D) Our biggest pain is *publishing* datasets safely.

3) **Scale (1–5)**
   - “How risky is it if a probabilistic hazard layer is interpreted deterministically?” (1 low → 5 high)

4) **Open text**
   - “Name 1 dataset you think should be a ‘recommended baseline’ for Phase 1, and why.”

5) **Open text**
   - “What boundary unit do you actually use for decisions (province / district / LAO / EA / other)?”

---

### Design-choice polling bank (NCAIF + CDM + MVPs + governance) — 2026-03-10

Goal: questions that produce answers you can directly use to justify **design choices** for:

- NCAIF entry/navigation option
- CDM scope priorities + boundary stance
- MVP prioritization + MVP-2 scope realism
- Governance gates + rails model

**Format target:** 8 polls total (7 closed + 1 open text). Keep each poll < 30 seconds.

---

### Sitemap-only poll set (4 questions) — use when validating the proposed structure

These 4 are designed to validate (or falsify) the proposed **Hybrid / workflow-pattern-first** structure (Option 3 in [`ψ/incubate/DCCE/CRDB/Artifact v1/NCAIF_Sitemap_Options.md`](ψ/incubate/DCCE/CRDB/Artifact%20v1/NCAIF_Sitemap_Options.md)).

**S1) Agreement check (structure-level)**

**Scale (1–5)**

“How much do you agree with this Phase 1 structure: **Home → ‘I need to…’ (workflows) + ‘Browse topics’ (thematic)**, plus visible **Data & Governance**?”

- 1 Strongly disagree
- 2 Disagree
- 3 Neutral / depends
- 4 Agree
- 5 Strongly agree

**S2) Different perspective: time-pressure entry (what is the default click?)**

**Multiple choice**

“If a user has **30 seconds** and only one ‘Start here’ button can be primary on Home, what should it be?”

- A) I need to do… (briefing pack / post-event / find official dataset)
- B) Browse topics (hazard/sector)
- C) I am a… (policy / local / disaster / analyst)
- D) Search data catalog (preview-before-download)

**S3) What must be one-click (reveals priority content placement)**

**Ranking (top 3)**

“Which **3 shortcuts** must be one-click on the Home page?”

- Recommended baselines (official dataset list)
- Data catalog search (preview-before-download)
- Briefing packs (downloadable)
- Spatial reference / boundaries + crosswalk guidance
- How to interpret probabilistic maps (uncertainty guidance)
- Post-event impact reports

**S4) Governance visibility tradeoff (different perspective: transparency vs simplicity)**

**Multiple choice (mandatory)**

“Where should ‘Data & Governance’ live in Phase 1 navigation?”

- A) Top-level menu (always visible)
- B) Under Data & Resources only
- C) Only linked from each product page (no global menu)
- D) Internal-only (not visible to external users)

---

### Governance-only poll set (4 questions) — buy-in + practicality

These 4 questions are intended to test whether Phase 1 governance is **acceptable to operate** (not just correct on paper), aligned with the rails + gates approach in [`ψ/incubate/DCCE/CRDB/Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/incubate/DCCE/CRDB/Feature-Driven%20Data%20Governance%20Strategy%20v3%20%282026-03-05%29.md:58).

**G1) Buy-in on “rails” (practical operating model)**

**Multiple choice (mandatory)**

“Is the **rails model** practical for Phase 1 (Internal / GDX / Open Data via data.go.th)?”

- A) Yes — this matches how we already work
- B) Mostly yes — but needs clearer process/templates
- C) Not yet — too complex for Phase 1
- D) Not sure

**G2) Minimum gate (what is realistic, not ideal)**

**Multiple choice (mandatory)**

“For Phase 1, what is the *realistic* minimum before any output is shared externally?”

- A) Limitations/uncertainty statement only
- B) Draft → review → publish workflow only
- C) Both A and B
- D) Neither (publish quickly; correct later)

**G3) Operational capacity (who can actually run the review?)**

**Multiple choice**

“Who can *practically* act as the reviewer/sign-off for Phase 1 outputs (most of the time)?”

- A) A small central DCCE data/governance team
- B) Each domain team reviews its own outputs
- C) A cross-unit working group (rotating reviewers)
- D) Executive sign-off only (director/deputy)

**G4) Endorsement decision-rights (recommended baselines)**

**Multiple choice (mandatory)**

“Who should have authority to publish a ‘recommended baseline’ decision in Phase 1?”

- A) DCCE central data/governance team
- B) Joint working group (DCCE + key data owners such as NSO + NXPO)
- C) Executive sign-off (Director / Steering Committee)
- D) Each data owner agency only (DCCE does not endorse)

#### 1) NCAIF entry principle (supports sitemap choice: thematic vs journey vs workflow vs hybrid)

**Multiple choice (mandatory)**

“What is the best *default* way users should start in Phase 1?”

- A) **I need to do…** (briefing pack / post-event report / find official dataset)
- B) **I am a…** (policy / local / disaster / analyst)
- C) **Browse topics** (hazard/sector)
- D) **Hybrid** (A + C)

---

#### 2) Phase 1 MVP commitment (supports MVP shortlist)

**Pick 2 (mandatory)**

“If we publicly commit to only **2 MVPs** in Phase 1, which two create the most value?”

- A) MVP-1 Briefing packs (exportable)
- B) MVP-2 Post-event reporting (event/impact + revision)
- C) MVP-3 Recommended baselines (official dataset registry)
- D) MVP-4 Uncertainty publishing standard

---

#### 3) CDM focus (supports CDM scope priority)

**Pick 1**

“Which CDM subject area must be standardized first to reduce rework?”

- A) Physical Climate
- B) Risk & Impact Assessment
- C) Adaptation Planning
- D) Monitoring & Evaluation

---

#### 4) Canonical boundary stance (supports boundary + crosswalk governance)

**Multiple choice (mandatory)**

“For Phase 1, which boundary pairing best matches real work?”

- A) **National reporting:** Province | **Local/budget work:** Municipality/LAO
- B) **National reporting:** Province | **Local/budget work:** District
- C) **National reporting:** District | **Local/budget work:** Municipality/LAO
- D) One boundary only (no crosswalk investment in Phase 1)

---

#### 5) Catalog stance (supports link-first vs host-first architecture)

**Multiple choice (mandatory)**

“For Phase 1, what should NCAIF primarily be?”

- A) **Link-first clearinghouse** (recommend + point to authoritative sources)
- B) **Host-first repository** (copy data into one place)
- C) Mixed: host only a few flagship datasets, link everything else

---

#### 6) MVP-2 scope realism (supports ‘groundwork’ vs ‘automated pipeline’)

**Multiple choice (mandatory)**

“For post-event impacts (MVP-2), what is an acceptable Phase 1 operating model?”

- A) Manual/batch intake + revision history + timeliness labels (groundwork)
- B) Semi-automated pipeline for a pilot area + manual elsewhere
- C) Fully automated routine pipeline nationwide
- D) Not feasible in Phase 1

---

#### 7) Safe publishing gate (supports governance gate design)

**Multiple choice (mandatory)**

“Before any output is shared externally, what minimum gate is required?”

- A) Limitations/uncertainty statement only
- B) Draft → review → publish workflow only
- C) Both A and B
- D) Neither (publish quickly; correct later)

---

#### 8) Endorsement authority (supports governance decision-rights)

**Multiple choice (mandatory)**

“Who should have the authority to publish a ‘recommended baseline’ decision?”

- A) DCCE central data/governance team
- B) Joint working group (DCCE + key data owners such as NSO + NXPO)
- C) Executive sign-off (Director / Steering Committee)
- D) Each data owner agency only (DCCE does not endorse)

---

#### 9) Open text (1 sentence) — baseline seeding (supports MVP-3 backlog)

“Name **one baseline dataset topic** that must be endorsed first in Phase 1 (e.g., flood hazard / boundaries / population / etc.) and why.”

### Slide 9 — A2 User-journey demo (3 journeys; one slide each)

**Format:** same template for each journey.

#### Slide 9a — Journey: DCCE communication & engagement

**Title:** “Publish a safe briefing (no PDPA surprises, no misinterpretation)”

**Show:** (1) recommended baseline selection → (2) uncertainty guidance → (3) export pack → (4) review/publish

MVP anchors:

- MVP-3 Recommended baselines
- MVP-4 Uncertainty guidance standard
- MVP-1 Briefing pack generator

Reference: [`National Climate Adaptation Information Framework.md`](src/01_Projects/2025-11_DCCE-CRDB/task/National Climate Adaptation Information Framework.md:78)

#### Slide 9b — Journey: Adaptation measure development team

**Title:** “From risk context to project justification (export-first)”

**Show:** choose area → pick baselines → generate LAO/province justification pack.

MVP anchors:

- MVP-3 + MVP-1 (+ MVP-4 if probabilistic)

#### Slide 9c — Journey: International cooperation / reporting team

**Title:** “Answer a reporting request with auditable sources”

**Show:** recommended baselines (with versions) → limitations statements → export pack.

MVP anchors:

- MVP-3 + MVP-4 + MVP-1

### Slide 10 — A3 Governance phasing plan (with DGA integration)

**Purpose:** show the “minimum governance needed to publish safely” and explicitly state we will leverage national rails.

**Show (visual):** 3 lanes (Internal / GDX / Open Data) + Phase 1 gates.

**Exact wording (speaker note):**

> “We are not proposing to build duplicate infrastructure. We will use **data.go.th** for open data discoverability and **GDX** for non-open G2G exchange; our job is to define the rules and artifacts that make this safe and usable.”

**Phase 1 governance gates (bullets):**

- Dataset classification: Internal vs GDX vs Open Data
- Minimum metadata + preview (schema/sample/owner/cadence)
- Recommended baseline registry + endorsement authority
- Boundary + crosswalk governance
- Limitations + uncertainty statement standard

Reference: [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven Data Governance Strategy v3 (2026-03-05).md:1)

### Slide 11 — Feedback capture (exact prompts)

**Pick 6–10 prompts for facilitation**

1) “Which 2 MVPs should we prioritize for Phase 1?” (MVP-1..MVP-4)
2) “What is your top concern about publishing (accuracy, privacy, reputational risk, misinterpretation)?”
3) “Which boundary unit must be canonical for Phase 1 reporting?”
4) “Should Phase 1 be catalog-first (link-first) or host-first? Why?”
5) “Who (role/title) should endorse ‘recommended baselines’?”
6) “Which dataset should be ‘recommended baseline’ for flood hazard in Phase 1?”
7) “What is the minimum acceptable lead time/refresh for post-event impacts?”
8) “Which non-open dataset would be most valuable if accessible via GDX?”

**(Optional replacements to keep prompts non-technical)**

- “Which link would save you time most often: packs, recommended baselines, catalog preview, or post-event reports?”
- “What is the safest statement we must always show on published outputs?”
- “If we can only endorse 3 baselines in Phase 1, which topics?” (flood hazard / population / boundaries / economics / other)

### Slide 12 — Close + next steps

**Speaker note:** summarize feedback themes and confirm next-step timeline.

## Facilitation tips (to keep it non-technical)

- Replace “CDM entity” with “what we must be able to record consistently.”
- Replace “data governance” with “data quality rules that keep outputs safe.”
- When debate starts, ask: “Is this feedback for later decisions? Park it for the decision workshop.”

---

## Key-message-per-agenda (for slide design)

Use this as the “one thing to remember” anchor for each agenda block; design each block’s slides around the message.

### Opening + continuity bridge

**Key message:** “FGD1 feedback already changed the design; today we confirm what is feasible and safe for Phase 1.”

Source anchors:

- FGD1 continuity: [`FGD2_plan_2026-02-26.md`](src/01_Projects/2025-11_DCCE-CRDB/notes/FGD2_plan_2026-02-26.md:60)

### A1 — CDM literacy activity (Mentimeter)

**Key message:** “CDM is not an IT diagram; it is the shared blueprint for what we must record consistently to answer real questions.”

### A2 — Internal use-case walkthrough

**Key message:** “We design from workflows (use cases) and produce safe, reusable outputs—especially exportable packs for decision-making.”

Anchor:

- Use cases: [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:157)

### A3 — Governance phasing (quality gates)

**Key message:** “Governance is the minimum set of quality gates that makes publishing usable and safe; we will use national rails rather than duplicate infrastructure.”

Anchors:

- DGA rails: [`Interview Summary - DGA.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20DGA.md:18)

### Close + next steps

**Key message:** “Your feedback becomes updated artifacts (MVP v2 + NCAIF structure + governance gates) and reduces rework before April workshops.”

---

## MVP refinement prompts (aligned to literacy-grounded MVP v2)

Use these to replace or extend the generic prompts in Slide 11.

Reference MVP v2: [`NCAIF — Workflow patterns + MVP v2.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v2.md)

Updated framing note: if available, use MVP v3 language (“workflow patterns are steps; MVPs are deliverable entities”) from [`ψ/incubate/DCCE/CRDB/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md).

1) **Tiering (mandatory):** “For Phase 1, what must be Tier 1 (prescriptive for mixed literacy) vs Tier 2 (advanced and gated)?”
2) **Operator model:** “Who should be allowed to generate/publish Tier 1 packs (role/title)?”
3) **Endorsement authority:** “Who can publish ‘recommended baselines’ and accept accountability for it (role/title)?”
4) **Minimum publishable gate:** “Is a limitations + uncertainty statement mandatory for any public output?”
5) **Event data reality:** “What timeliness label is acceptable for post-event numbers (e.g., 1 week) and what revision policy is acceptable?”
6) **Boundary reality:** “Which boundary unit must be canonical for budget decisions (LAO/municipality) vs national monitoring?”
7) **Misuse risk:** “Which probabilistic map misuse is most common in your context, and what wording would prevent it?”
