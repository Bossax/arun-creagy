# TOR70 Amendment Recommendation — Briefing Deck for Director Toey

11 slides. Each heading is written to stand alone — reading only the 11 headings should give the executive summary of this deck. Clause numbers and detailed evidence are pushed to speaker notes throughout, matching plain-writing style for a non-technical audience. Director Toey is the Project Manager and has final approval authority — this deck asks him for a direct decision, not for help carrying a recommendation upward.

Source material: [2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md](./2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md) in this folder. All figures below are drawn from that file and, beneath it, from the CRDB `output/` deliverables it cites.

---

## Slide 1 — Title / Recommendation

**Heading:** We recommend amending TOR70 before it goes out for bid

**Subhead:** Based on our review of the current draft against how data and web platforms are normally built, and against what CRDB has already delivered

**Body (single centered block, no bullets — this is the whole ask in one place):**

> TOR70, as drafted, asks the incoming contractor to redo work DCCE has already paid for and completed, and it leaves out steps that make a platform maintainable after handover.
>
> We recommend restructuring the scope of work around the standard sequence for building data and web platforms, and requiring the contractor to build on CRDB's work instead of starting over.

**Visual layout:** Title top third. Recommendation statement centered, large type, two short paragraphs as shown — no bullet points on this slide. DCCE and consultant logos/names bottom corners.

**Speaker notes:** This is a recommendation for Director Toey's approval, not a finding being reported upward — he has final say on TOR70. Tone throughout: professional judgment offered for his decision, not a verdict on DCCE's prior work.

---

## Slide 2 — The standard

**Heading:** Data and web platforms are normally built in six stages, in a fixed order

**Subhead:** This is not a CRDB or consultant standard — it reflects how government and industry guidance (TOGAF, IBM, Australia's National Archives, standard web-development practice) converges on the same sequence

**Body — diagram is the content of this slide, minimal surrounding text:**

**Diagram** (six boxes left to right, stages 2 and 3 each split into two parallel lanes labeled "Data" and "Web," a return arrow from stage 6 back to stage 1):

```
[1. Find out what's       [2. Design the data       [3. Build the data
 needed and who        →   platform and the web   →   platform and the
 needs it]                 platform together          web platform in
                            (parallel)]                 parallel]
                                                              ↓
[6. Run it, watch it,  ←  [5. Hand it over and   ←  [4. Prove the finished
 and feed what you          bring it into use]         system actually
 learn back into the                                    works and meets
 next round]                                             the need]
```

**One-line caption under the diagram:** Each stage produces something the next stage needs. Skipping the order, or doing stage 3 before stage 2 is finished, is what causes rework later.

**Speaker notes:** Full stage table with purpose and output per stage lives here (not on slide): Requirements Elicitation & Analysis; Functional Analysis & Solution Design; Implementation; System Integration, Verification & Validation; Deployment & Operational Transition; Operations, Maintenance & Continuous Improvement. Cite: Australian National Archives current-state assessment guidance, TOGAF Phase C, IBM data architecture guidance, BrowserStack web development lifecycle — full citations in the storyline file's "Industry-practice basis" section.

---

## Slide 3 — Where TOR70 stands today

**Heading:** Measured against that standard, TOR70 covers less than half of what a complete platform project needs

**Subhead:** Overall: roughly 45%

**Body — horizontal bar chart, one bar per stage, ordered 1–6 left-to-right or top-to-bottom, percentage labeled on each bar:**

| Stage | Coverage |
|---|---|
| 1. Find out what's needed | ~35% |
| 2. Design | ~40% |
| 3. Build | ~45% |
| 4. Prove it works | ~65% |
| 5. Hand over | ~65% |
| 6. Run and improve | ~12% |

**Visual layout:** Bar chart is the dominant visual, roughly 2/3 of the slide. Stage 6's bar should read visibly shortest — that is the single number Toey should remember from this slide.

**Below the chart, one line, not a bullet:** TOR70 is strongest in the middle — building, testing, and installing — and weakest at both ends: understanding what's needed before building, and keeping the platform useful after handover.

**Speaker notes:** Full "what's present / what's absent" detail per stage lives in the storyline file's stage-coverage table. Key absences to have ready if asked: no measurable performance or uptime targets anywhere in the document; no development/test/staging environments or CI/CD mentioned anywhere; stage 6 is covered by only a one-year warranty clause, nothing else.

---

## Slide 4 — What DCCE already has

**Heading:** Most of what TOR70 asks the contractor to build from scratch, DCCE has already built

**Subhead:** None of this is reflected anywhere in the current TOR

**Body — two-column layout. Left column: icon + number + label. Right column: what it replaces in the TOR.**

| DCCE already has | This is what TOR70 currently asks the contractor to redo |
|---|---|
| **260** cataloged datasets, with source, quality and ownership information | Survey and re-catalog the same data |
| **75** detailed system requirements, most already marked ready to build | Analyze and write requirements from scratch |
| A complete data model (**45** entities) and a shared glossary (**73** terms) | Design the data structure and definitions from scratch |
| A designed and user-tested site structure (**38** pages, tested through nine rounds of revision) | Design the site structure from scratch |
| Business cases for **9** priority services | Hold one workshop to figure out what to build |
| A loss-and-damage data standard, already tested against 10 years of real disaster records | — |
| A governance model naming who owns and checks each type of data | — |

**Speaker notes:** Every figure here is counted directly from the CRDB output files, not estimated — sources: WP4 Developer-Ready Design Requirements v2, data catalog v4, CDM Entities v3, Glossary v5, NCAIF Sitemap v9, WP6 service business cases, WP9 loss-and-damage pilot. Have the exact file paths ready if asked, but do not put them on the slide.

---

## Slide 5 — The same benchmark, with CRDB counted

**Heading:** Requiring the contractor to build on this work instead of ignoring it raises coverage from 45% to 62% — at no added cost

**Subhead:** Same 270 days, same ฿12.5 million budget

**Body — before/after paired bar chart, same six stages as Slide 3, two bars per stage:**

| Stage | Before (TOR as written) | After (CRDB adopted as baseline) |
|---|---|---|
| 1. Find out what's needed | 35% | **70%** |
| 2. Design | 40% | **80%** |
| 3. Build | 45% | 50% |
| 4. Prove it works | 65% | 70% |
| 5. Hand over | 65% | 70% |
| 6. Run and improve | 12% | 30% |
| **Overall** | **45%** | **62%** |

**Visual layout:** Same chart as Slide 3 with a second, taller bar added next to each original — the visual pairing should make the "before" chart from Slide 3 instantly recognizable, so the jump reads as the same measurement, improved.

**Below the chart, one line:** The gain is almost entirely in stages 1 and 2 — the two stages CRDB was already commissioned to deliver. Stage 3, the actual build, barely changes, because building the platform is genuinely the next contractor's job.

**Speaker notes:** This last point matters if challenged — we are not claiming CRDB did the contractor's job for them. The additive work (the entire CMS, the frontend, installation, all testing, training) stays fully in TOR70's scope. Full "what's additive, not duplicated" list is in the storyline file's closing section, for use if Toey or his team wants the detailed boundary.

---

## Slide 6 — Five principles behind the redraft

**Heading:** Five shifts in how the TOR is written would fix most of what's missing

**Subhead:** These are principles for redrafting, not new work for DCCE

**Body — five stacked rows, each: bold one-line principle, one-sentence plain elaboration beneath, no further nesting:**

1. **DCCE owns the products; the contractor implements them.**
   The contractor should turn DCCE's intent into technical work — not decide, by default, what the platform is for.

2. **TOR70 continues from CRDB; it does not restart.**
   The contractor's first job is to understand and build on what already exists, not re-derive it.

3. **Every feature should trace back to a real user need.**
   Datasets, dashboards and pages are only valuable because of the decisions they support — not because they exist.

4. **Governance should show up in how the system behaves, not just in a document beside it.**
   Who approves data, who checks it, who can change it — these should be built into the system, not left as a policy on paper.

5. **TOR70 should hand over a capability DCCE can keep running, not just a finished website.**
   Ownership, monitoring, and a way to add the next product later need to be part of the contract, not an afterthought after handover.

**Speaker notes:** Full sentence-length version of each principle, with sourcing, is in the storyline file's "fundamental shift" section. The one-sentence summary of all five, if asked for the shortest possible version: "TOR70 should not procure a contractor-owned website containing DCCE data; it should procure the implementation of a DCCE-owned data-service capability built on the CRDB foundation."

---

## Slide 7 — A concrete path: five real products

**Heading:** Instead of one big platform built all at once, TOR70 should be organized around five named products

**Subhead:** Three exist today and need to be brought in; two are new and need to be built end to end

**Body — diagram: two labeled groups feeding into one shared platform box, with a five-step build order beneath.**

**Diagram:**

```
ALREADY EXISTS — bring in and govern        NEW — build end to end
 • Spatial climate-risk database             • A-BTR reporting service
 • Hazard and exposure maps                  • Disaster loss-statistics service
 • Climate Risk Index (CRI)

              \                                      /
               \                                    /
                v                                  v
                [ ONE SHARED DATA + WEB PLATFORM ]
        (common pipelines, catalog, permissions, APIs,
         built once and reused by all five products)
```

**Build order, five short steps below the diagram:**

1. Adopt CRDB's work as the approved starting point
2. Bring the three existing products into the new platform, governed and usable
3. Build the two new products from approved requirements, start to finish — not just a dashboard, but the full path from source data to the screen
4. Pull out what all five products share, and build that once as reusable platform capability
5. Put DCCE's ownership roles in place around all of it, and train DCCE using the real, working products

**Speaker notes:** The full "source data → governed ingestion → validation → data product → service → web interface → DCCE acceptance → operational responsibility" chain for the two new services is detailed in the storyline file's Step 3, for use if asked how a new service actually gets built end to end.

---

## Slide 8 — What DCCE receives

**Heading:** At the end of this contract, DCCE should have more than a website with thirty datasets

**Body — six-item checklist, single column, no sub-bullets:**

- Three existing analytical products, brought into one governed, maintainable service
- Two new policy-relevant products, working from real source data through to the screen
- One shared platform whose parts have been proven by building those five products
- Named DCCE ownership and a way to keep the products current
- Reusable standards and connections for adding the next product later
- A clear line between who manages content, who manages data, and who manages the technical system

**Bottom of slide, set apart visually (box or rule above it):** Success should be measured by whether DCCE can operate these five products and add a sixth — not by how many files or pages were delivered.

**Speaker notes:** This is the single sentence to return to if the conversation drifts toward feature-counting or scope-creep discussion.

---

## Slide 9 — What to add, stage by stage

**Heading:** The fix is one addition per stage — TOR70's structure and build scope stay mostly intact

**Subhead:** This directly answers Slide 3 and Slide 5's chart, stage by stage

**Body — six rows, matching the six stages from Slides 2, 3 and 5 in the same order, each one bolded headline sentence only:**

| Stage | Add this |
|---|---|
| 1. Find out what's needed | A step where the contractor proves it understands CRDB's work, turns it into technical requirements, and gets DCCE's formal sign-off before anything is designed |
| 2. Design | One coordinated design for the data and web platforms together, with clear agreements between them, instead of two disconnected designs |
| 3. Build | Build each priority product as one connected path from source data to the screen, not data upload and website display as separate tasks |
| 4. Prove it works | Test the finished system against DCCE's approved requirements and real measurable targets, in a test environment — not on the live servers |
| 5. Hand over | Hand over a running, monitored, supportable service — not just installed software — with DCCE's operating roles already in place |
| 6. Run and improve | A defined process for monitoring, fixing, and improving the platform after launch, feeding real usage back into what gets built next |

**Speaker notes:** Full detailed activity lists per stage (for drafting the actual TOR language) are in the storyline file's "What to add to each reference lifecycle stage" section — use only if the meeting moves into contract-drafting detail. Otherwise this table is the complete slide.

---

## Slide 10 — What this commits DCCE to

**Heading:** Approving this also means DCCE needs to make a few decisions of its own

**Subhead:** These are decisions only DCCE can make — no contractor or consultant can make them on DCCE's behalf

**Body — five items, flat list, no sub-bullets:**

- Formally establish the Data Governance Committee, and appoint the Data Owners and Data Stewards named in CRDB's governance model
- Decide how datasets should be classified for licensing — this is a hard prerequisite for the platform to share any meaningful share of its catalog
- Decide the scope of non-financial loss categories (mental health, biodiversity, cultural heritage) for the loss-and-damage service
- Decide whether to extend the existing national policy-monitoring platform or build a new one
- Assign which part of DCCE administers the database going forward

**Speaker notes:** Full list of ten Tier-2 decisions is in the CRDB trace log `ψ/memory/traces/2026-08-26/1602_crdb-final-sprint-precode-dcce-approval-gates.md` — these five are the ones with the clearest immediate bearing on TOR70's build scope. Frame this slide as "here's what's already on your plate either way" — these decisions are needed regardless of whether TOR70 is amended, so approving the amendment does not create new work for DCCE, it surfaces work that already exists.

---

## Slide 11 — The decision

**Heading:** We recommend approving this direction before TOR70 goes out for bid

**Body — three short blocks:**

**What we're asking for:**
> Approval to redraft TOR70's scope of work around the six-stage structure shown today, requiring the contractor to build on CRDB's work rather than starting over.

**What happens next if approved:**
> We prepare the specific clause language for your review, incorporating the additions shown on Slide 9.

**What we need from you today:**
> A yes/no on direction, and any concerns about the five decisions on Slide 10 that you want addressed before the redraft is written.

**Visual layout:** Same restrained centered-block style as Slide 1 — this is the bookend. No bar charts or bullets here; the deck should open and close on the same visual register.

**Speaker notes:** If Toey asks for time rather than a decision today, the fallback ask is a scheduled follow-up date — do not leave this slide without either a decision or a next meeting on the calendar.
