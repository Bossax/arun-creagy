---
type: draft
status: preliminary
version: 1
created: 2026-08-06
project:
  - DCCE_CRDB
---

> [!warning] Preliminary Draft — Not Sealed
> This draft is grounded **only** in DCCE's own TOR documents (CRDB-TOR §1/§2/§3/§5 and TOR70-TOR §1/§2/§3/§5) — no secondary sources (Strategic Alignment Deck, redirection plan) were used this pass, by design, to keep DCCE's original written intent visible before CRDB's own interpretive layer gets added back in. **This is the first cut. It gets polished together with Boss before it's considered final, and none of it is sealed into the project ledgers yet.** Claims not traceable to a TOR clause are flagged inline as `(gap — not in TOR, needs Boss's input)`.

# Item 1 — Business Objective / Platform Rationale

## 1. Why This Platform Exists

DCCE's own TORs describe **two nested problems**, at two different altitudes. They should not be collapsed into one "why" — CRDB and TOR70 are answering different questions.

**The deeper problem (CRDB-TOR §1): Thailand has no national climate-adaptation data governance capability.** Climate adaptation knowledge relevant to Thailand exists, but it is scattered across foreign and domestic sources (NAP Global Network, Santiago Network, IPCC, Germanwatch, DCCE's own past reports and policy documents) with no framework to synthesize or compare it systematically. DCCE explicitly names the consequence: data products don't get built to meet actual user needs, because no one has systematically inventoried what data exists, who needs it, or where the gaps are (CRDB-TOR §1, §2.2). This is a **capability gap**, not a communication gap — DCCE cannot yet answer "what data do we have, who owns it, and what's missing" for its own domain.

**The surface problem (TOR70-TOR §1): the public has no central, modern place to see any of it.** Once that underlying data and governance exist (or exist well enough), DCCE's second problem is that there is no unified "Data Hub" dashboard — no central, well-designed, easy-to-use platform that pulls together data from multiple sources and presents it in formats non-specialists can use (interactive visualization, infographics, storytelling-style articles). Academic reports and large studies currently just sit as documents; nobody translates them into something a policymaker or the public can act on quickly (TOR70-TOR §1, §5.3.10).

**Section 5 confirms this reading in both TORs, in ways §1 leaves implicit:**
- CRDB-TOR §5.2–§5.3 shows DCCE's own process for closing the *capability* gap before any system gets built: study foreign frameworks (Japan's A-PLAT, Germany's Klimadapt, the EU) → draft a National Climate Adaptation Information Framework → validate it through a structured sequence of focus groups and a public hearing → only then produce the Information Product & Baseline Data Inventory. This is DCCE deliberately sequencing governance-framework validation *before* content collection — it is not treating "what data do we even have" as a solved problem going in.
- TOR70-TOR §5.5 (CMS with a draft → review → approve → publish workflow, explicit reviewer/approver roles) and §5.4.13–§5.4.14 (RBAC, audit trail) reveal DCCE anticipated a **trust problem**, not just a display problem: content published under DCCE's name has to be checked before it goes live, and every change has to be attributable to a specific person. That's a safeguard against a fear that isn't stated outright in §1 but is clearly designed against in §5.

## 2. Who It Serves

The two TORs name meaningfully different audiences, and this gap should be surfaced rather than resolved silently — it likely reflects the difference between "who needs the underlying data capability" and "who visits the public dashboard."

**CRDB-TOR §3 — broad, institutional:**
- *Primary:* officials in other agencies working on National Adaptation Plan sectors; officials involved in project screening and budget review; officials developing climate information services; DCCE's own staff; academics and climate-change experts.
- *Secondary:* civil society and private-sector organizations; international organizations; financial institutions, state enterprises, and private-sector actors needing climate data for risk management.

**TOR70-TOR §3 — narrow, public-facing:** DCCE staff and the general public. Full stop.

`(gap — not in TOR, needs Boss's input)`: TOR70's scope of work (§5.10 dissemination activities) actually names a broader participant list for its outreach events — government agencies, the 6 NAP sectors, private sector, academia, cooperation networks, and "interested general public" — which is closer to CRDB-TOR's list than TOR70 §3's own two-line target-group statement suggests. Worth deciding whether TOR70 §3 was simply under-specified relative to its own §5, or whether DCCE genuinely intends the *system* to serve a narrower audience than the *outreach process* around it.

## 3. What's Lost Without It

Read as evidence rather than aspiration, DCCE's TORs show what they were afraid would happen, by what they explicitly built safeguards against:

- **Without the governance framework (CRDB-TOR §5.2–§5.3):** data stays fragmented and un-synthesized; agencies keep collecting and holding data independently with no shared inventory, so effort is duplicated and gaps go unnoticed. CRDB-TOR §2.2 names this outright as the reason a Gap Analysis and an Information Product & Baseline Data Inventory are required at all.
- **Without defined data ownership and an approval gate (TOR70-TOR §5.4.13–§5.4.14, §5.5.8–§5.5.9):** anyone could edit or publish under DCCE's name, with no accountable owner and no audit trail — a direct governance risk given DCCE is a government agency publishing to the public. The TOR's insistence on RBAC, an explicit draft→review→approve→publish state machine, and a full audit log is DCCE writing a defense against exactly that failure mode into the contract itself, not an incidental technical requirement.
- **Without mandatory training and handover (TOR70-TOR §5.9):** DCCE explicitly required on-the-job training for system administrators, content/data staff, and end users, plus delivered manuals — meaning DCCE anticipated the risk of receiving a system it doesn't know how to run once the consultant's contract ends, and built the requirement to prevent that into the TOR rather than leaving it to chance.
- **Without translation of academic/technical material into accessible formats (both TORs — CRDB-TOR §5.5, TOR70-TOR §5.3.10–§5.3.11):** the underlying research and data would continue to exist but stay unusable by the people who most need it — policymakers, other agencies, and the public — because it never gets converted out of report form.

## 4. How This Feeds the Rest of the Package

This rationale is the thing Item 6 (Gap Analysis) and Item 8 (Recommendations) get scored against, per the sprint plan (`plans/2026-08-06-crdb-final-sprint-implementation-plan.md`, WP1 row): Gap Analysis (DATER dimensions 1–6) should be assessed against the two-altitude problem stated in Section 1, not against an assumed single "why"; Recommendations should explicitly address the target-audience discrepancy in Section 2 rather than picking one list without acknowledging the other.

---

## Appendix: TOR Clause → Product-Language Translation

| Source | Clause | Literal ask | Implicit intent | Product-language translation |
|---|---|---|---|---|
| CRDB-TOR | §1 (Rationale) | Describe fragmentation of climate adaptation data across sources | DCCE cannot currently answer "what data exists, who owns it, what's missing" | **Problem statement (governance layer):** no shared data inventory or ownership model for climate-adaptation data across agencies |
| CRDB-TOR | §2.2 (Objectives) | Analyze demand, conduct Gap Analysis, build Information Framework + Inventory | The framework and inventory are prerequisites, not the end product | **Outcome:** a validated data governance framework + baseline inventory, not yet a system |
| CRDB-TOR | §3 (Target Groups) | List 5 primary + 3 secondary target groups | DCCE sees this as an institutional/multi-agency capability, not a single-audience product | **User segments (broad):** government officials (multiple functions), academics, civil society, international orgs, private sector/finance |
| CRDB-TOR | §5.2.1–§5.2.8 | Sequence of focus groups + public hearing to validate the Draft Framework | DCCE treats framework validation as a governed, staged, multi-stakeholder process — not a one-shot internal decision | **Process requirement:** the "product" (framework) must go through staged stakeholder validation before being considered final |
| CRDB-TOR | §5.3.5–§5.3.9 | Build Information Product Inventory + Baseline Data Inventory (≥100 datasets), categorized by international risk-assessment framework (Hazard, Exposure, Sensitivity, etc.) | DCCE wants the inventory structured against an internationally recognized taxonomy, not an ad hoc list | **Data model requirement:** inventory schema must map to standard risk-assessment categories, for external comparability |
| TOR70-TOR | §1 (ความเป็นมา) | Build a "Data Hub" dashboard central to climate-adaptation communication | Data/knowledge exists but is inaccessible and not synthesized for non-specialist use | **Problem statement (product layer):** no central, modern, accessible surface for climate-adaptation information |
| TOR70-TOR | §2.1–§2.3 (Objectives) | Central Data Hub; improved comms via infographics/storytelling; decision-support platform | Three distinct product goals bundled as one system | **Product goals:** (a) findability/access, (b) content accessibility for non-specialists, (c) analytical/decision support |
| TOR70-TOR | §3 (กลุ่มเป้าหมาย) | DCCE staff + general public | Narrower stated audience than the outreach activities in §5.10 imply | **User segments (narrow):** internal staff (operators) + general public (consumers) — flagged discrepancy vs. §5.10 |
| TOR70-TOR | §5.4.13–§5.4.14 | RBAC, audit trail, defined user roles (admin, data-entry, reviewer/approver, internal user, public) | DCCE anticipates unauthorized or unaccountable changes to public-facing government data | **Non-functional requirement → trust signal:** every content change must be attributable and reversible |
| TOR70-TOR | §5.5.1, §5.5.8–§5.5.9 | CMS with draft → review → approve → publish states; authentication + role-based permissions | DCCE does not trust unmoderated self-publish for government climate data | **Workflow requirement:** content governance is a first-class feature, not an afterthought |
| TOR70-TOR | §5.9.1–§5.9.4 | Mandatory on-the-job training for admins, content staff, and users; delivered manuals | DCCE expects to operate the system itself post-handover, not remain dependent on the contractor | **Sustainability requirement:** operational self-sufficiency is a delivery condition, not a nice-to-have |
| TOR70-TOR | §5.3.10–§5.3.11 | Synthesize academic reports into infographics, storytelling summaries, trend analyses, policy briefs | Raw research output is inaccessible to the platform's actual audience without translation | **User need:** non-specialist-readable content is a core deliverable, not a stretch goal |
| TOR70-TOR | §5.10 | Dissemination event naming government agencies, 6 NAP sectors, private sector, academia, cooperation networks, general public | Broader participant list than TOR70's own §3 target-group statement | **Discrepancy signal:** outreach process audience ≠ stated system target audience |
