# CRDB Citation Gap Audit — Master Report

Read-only audit. No draft, sidecar, contract, or ledger was modified. Covers all 17
executive-summary sections (chapters 1–4) and all four full-report writing plans in
`ψ/incubate/DCCE/CRDB/output/final_deliverable/`.

## Top-line pattern

1. **The citation gap is structural, not accidental.** Exec-summary prose deliberately
   omits in-text locators (a documented style choice in each `writing-contract.json`).
   The full-report writing plans *do* instruct authors to name frameworks directly in
   prose — but every "หลักฐานที่ใช้" (evidence used) line in those plans routes to an
   **internal CRDB document** (a `5.x.md` technical chapter, an FGD note, a slide deck),
   never to the actual external standard/framework being named. None of the plans use
   `E-xxx` Evidence Registry codes except Chapter 4's.
2. **Real external sources often already exist in the project** — mostly in
   `ψ/incubate/DCCE/CRDB/inbox_source/` — but they are **not wired into the evidence
   chain**. This is a linking gap, not always a research gap: someone already found or
   wrote a real source note; it just isn't cited from the place that needs it.
3. **A smaller number of claims have no real external source anywhere in the project**
   and would need new research before they can be cited (marked GAP below).
4. Two rows are outright **evidence-line errors** in the writing plans (Ch.3's Thai
   statute reference; Ch.4's CWE-840 citation pointing at the wrong E-codes) — these are
   easy, mechanical fixes once flagged.

## How to read the tables

- **SOURCED** — a real external source is recoverable in-project and verifiably
  supports the specific claim.
- **PARTIAL** — a source exists but is topically adjacent, low-authority (a blog/AI
  research note rather than a primary document), or supports only part of the claim.
- **GAP** — no real external source is recoverable anywhere in the project. Per this
  project's own established rule (`2026-03-29_chapter-separated-drafting-real-source-citations.md`),
  this should be flagged and marked HOLD in the report, not silently asserted.

---

## Chapter 1 — Intro / platform rationale, international benchmarks

### Exec-summary layer
| Claim | Section(s) | Status | Note |
|---|---|---|---|
| ISO 14090 (adaptation management cycle) | 1.1 | SOURCED | `inbox_source/2026-02-16-ISO 14090 2019.md` — real iso.org/iteh.ai URLs |
| Information scent / information foraging theory | 1.1 | SOURCED | UX design-principles note's works-cited #10 (Pirolli & Card) |
| U.S. Climate Resilience Toolkit, World Bank CCKP case studies | 1.1 | SOURCED | Same UX note, works-cited #71–77, live toolkit.climate.gov / worldbank.org links |
| WMO GFCS (climate-services co-production logic) | 1.1 | PARTIAL | Same UX note, footnote 7 (real WMO page) — supports co-production concept, not the full claim as framed |
| ISO 14091 (vulnerability/risk assessment) | 1.1 | PARTIAL | Only a secondary AI-research note (`2026-02-10-Architectural Blueprint...md`) names it correctly; no primary-source note like 14090 has |
| Progressive disclosure / front-end tool-vs-catalog separation | 1.1 | PARTIAL | Real URLs but low-authority (marketing blogs), not standards-grade |
| A-PLAT (Japan), KlimAdapt (Germany), Climate-ADAPT (EU) | 1.1, 1.2 | SOURCED (platforms real) | Citation needs an independent URL check before finalizing — not verified live in this pass |
| IPCC risk framework (hazard×exposure×vulnerability) | 1.1 | GAP | Underlying doc never cites an actual IPCC edition/chapter; no verified primary IPCC document in project for this specific claim |
| UNFCCC NAP reporting logic | 1.1 | GAP | No internal source cites an actual UNFCCC NAP technical guideline document |
| 1.2, 1.3, 1.4 | — | N/A | Purely internal findings; no external framework named |

### Full-report writing plan layer
| Claim | Status | Note |
|---|---|---|
| A-PLAT, KlimAdapt | PARTIAL→fixable | Plan's own evidence base (§9.1) claims "no document exists" — **false**. `output/draft_final_report/5.2/5.2.1...md` already has detailed primary-observation descriptions of both. This is a linking omission, not a sourcing failure. |
| Climate-ADAPT | SOURCED | UX doc's works-cited #26 links directly to the live EEA sitemap |
| IPCC / WMO / UNFCCC / ISO 14090+14091 "content-category framework" claim | GAP | The internal mapping note (`archive/National Climate Adaptation Information Framework.md` lines 407–480) cites none of the four frameworks with any bibliographic detail. Exactly the "internal artifact posing as final reference" pattern the project's own citation-hygiene rule warns against. |
| ISO 14090 (specifically) | PARTIAL | Real source exists (same as exec-summary layer) but not linked from the plan's §9.1, and documents a different claim (adaptation-cycle clauses, not content taxonomy) |
| ISO 14091 (specifically) | GAP | No document anywhere in the project even mentions it outside the internal mapping note |
| GFCS / WMO | PARTIAL | Real source exists but is linked to a different UX claim, not this one |
| UNFCCC (content-category framing) | GAP | Internal working note only, no primary UNFCCC document |

**Chapter 1 priority actions**: wire `5.2.1` into the evidence base for A-PLAT/KlimAdapt (cheap fix, source already exists); either find real IPCC/WMO/UNFCCC/ISO-14091 primary documents for the "content-category framework" sentence or mark it HOLD.

---

## Chapter 2 — Data inventory, metadata standards, service catalog

### Exec-summary layer
| Claim | Section(s) | Status | Note |
|---|---|---|---|
| มสพร. 1-2564 (DGA metadata standard) | 2.1 | PARTIAL | Real, named standard (agency + code) but no primary document/URL anywhere in the project to verify title |
| A-BTR / UNFCCC Enhanced Transparency Framework | 2.3 | SOURCED | UNFCCC Decision 18/CMA.1 — reached through 2 layers of secondary synthesis (UNDP interim report → NotebookLM extraction); light verification of the primary decision text recommended |
| A-PLAT / Climate-ADAPT (considered, deliberately not named as inclusion criteria) | 2.1 | N/A | Sidecar correctly declined to over-cite — evidence only supported metadata-field design, not inventory-inclusion criteria |
| 2.2, 2.4 | — | N/A | Purely internal statistics, no external claim |

### Full-report writing plan layer
| Claim | Status | Note |
|---|---|---|
| IPCC risk-chain framework (hazard/exposure/sensitivity/adaptive-capacity chain) | PARTIAL | Only adjacent real source found (`Processes of decision making - IPCC WGII Chapter 17.md`) is about decision cycles, not this taxonomy. If cited, should be AR6 WGII Ch.1/SPM or AR5 SREX instead. |
| มสพร. 1-2564 | GAP | No document embodying the actual standard (issuing date, version, DGA publication) exists in the project |
| ISO 19115 (geographic metadata) | GAP | Named in passing in internal drafts only; no standard document/edition/clause anywhere |
| GFCS / WMO (product-classification claim) | PARTIAL | Real WMO source exists (`WMO-NFCS/inbox_source/...CSIS.md`) but supports CSIS's data functions, not the specific 4-stage classification claim used here |
| A-PLAT, KlimAdapt (as named foreign comparators) | GAP | No document in this chapter's search path describes either platform — note Chapter 1's `5.2.1` *does* have this, it's just not cross-linked into Chapter 2's evidence base either |
| Climate-ADAPT | PARTIAL | AI-synthesized secondary note, not the primary EEA publication |
| Thailand's NAP (sector classification claim) | GAP | Neither `inbox_source` file about NAP is Thailand's actual primary NAP document |

**Chapter 2 priority actions**: มสพร. 1-2564 and ISO 19115 are named standards with zero primary document anywhere in this project — these need someone to actually pull DGA's and ISO's real publications before the chapter can cite them. A-PLAT/KlimAdapt sourcing already exists in Chapter 1's evidence base and just needs cross-linking.

---

## Chapter 3 — Loss & damage, DesInventar/DaLA/PDNA, MVD (the chapter Boss flagged)

### Exec-summary + full-report writing plan layer (combined — same underlying claims)
| Claim | Section(s) | Status | Note |
|---|---|---|---|
| **DesInventar** (UNDRR, local event registry) | 3.1 (exec + full) | **SOURCED** | Real source recoverable: `inbox_source/DesInventar as a Disaster Information Management System.md` (LA RED origin, UNDP/UNDRR sponsorship) + `inbox_source/Disaster_Loss_Standards_Analysis.md` References (UNDRR, *DesInventar Sendai 10.1.2 User Manual*, with live desinventar.net URLs). **Not currently linked** by either the exec-summary sidecar or the full-report plan's §9.1 — both cite only the uncited `5.3.6` prose. |
| **DaLA** (UNECLAC/World Bank, damage/loss split) | 3.1 (exec + full) | **SOURCED**, attribution caveat | Real source: `inbox_source/Disaster_Loss_Standards_Analysis.md` — Jovel & Mudahar (2010), *Damage, Loss, and Needs Assessment Guidance Notes*, World Bank; corroborated by ECLAC's own Disaster Assessment Portal. Draft credits DaLA solely to "UNECLAC" — historically accurate origin but now jointly stewarded with World Bank/EU; not wrong, worth a footnote. **Not currently linked** into either evidence chain. |
| DDPM's own PDNA phase framework (Phase 0/1–2/3–4) | 3.1 (exec + full) | SOURCED | DDPM's own commissioned report is the correct primary source (`inbox_source/Post Disaster Needs Assessment report by DDPM.md`) — publication year is blank in the source file's frontmatter, confirm before formal citation |
| PDNA phase-numbering specifically ("ระยะที่ 0–2/3/4") | 3.2 (full) | PARTIAL | A DDPM NotebookLM extraction with real primary PDFs exists, but its own generic 6-step breakdown doesn't cleanly match the plan's exact phase labels — needs direct verification against `Final_Report_PDNA60.pdf` |
| "Build Back Better and Safer" recovery principle | 3.1 | **GAP** | No document anywhere in the project traces this specific phrase to an origin (commonly associated with post-2004-tsunami UNISDR/World Bank guidance and the Sendai Framework, but that attribution is not established by anything in-project) — do not write with implied certainty |
| DesInventar/DaLA comparative-role sentence | 3.1 | PARTIAL | Reasonable synthesis of the two SOURCED items above; `Disaster_Loss_Standards_Analysis.md` lines 148–150/289–295 make exactly this comparison and would be a stronger anchor than the current uncited synthesis |
| ADLA/eDLA, ECLAC full guideline (deliberately excluded) | 3.1 exclusions | N/A — correct | Plan correctly flags this as unconfirmed and withholds it; real bibliographic detail exists in `Disaster_Loss_Standards_Analysis.md` if ever un-archived |
| พ.ร.บ. ป้องกันและบรรเทาสาธารณภัย พ.ศ. 2550 / แผน ปภ. แห่งชาติ 2564–2570 (Thai statute/plan) | 3.2 (full) | **GAP** | Real, publicly recoverable legal instruments, but no document in the project carries the actual citation detail (Royal Gazette date/volume, official URL) |
| `DS-08` / `REQ-049` internal codes appearing directly in prose instructions | 3.5 (full) | Process violation | Not a sourcing gap — this is the plan's own rule #2 (no internal locators in prose) being violated in its own drafting instructions. Flag for the writer. |
| 3.3, 3.4 | — | N/A | Purely internal empirical test / recommendations, no external claim |

**Chapter 3 priority actions — this is the highest-value fix in the whole audit.** DesInventar and DaLA both have real, specific, already-existing primary sources in `inbox_source/Disaster_Loss_Standards_Analysis.md` and the DesInventar note. Neither the exec-summary sidecar nor the full-report writing plan's evidence base points to them — both currently cite only the uncited `5.3.6` prose. Wiring these two sources in closes the gap you flagged for the chapter's two headline frameworks immediately, no new research needed. "Build Back Better and Safer" and the Thai statute reference are genuine GAPs needing new sourcing.

---

## Chapter 4 — A-BTR gap analysis, institutional roles, SDLC/roadmap

### Exec-summary layer
| Claim | Section(s) | Status | Note |
|---|---|---|---|
| Paris Agreement Art. 13 / A-BTR / UNFCCC focal-point role | 4.1 | SOURCED | Thailand's own draft 2nd BTR / 5th National Communication (UNDP-supported, 2026); Evidence Registry E-062/E-077 |
| NAP (referenced alongside A-BTR) | 4.1 | SOURCED | Same UNDP BTR2 draft, links to Thailand's official NAP document |
| "Reference Integrated Data and Web Platform SDLC" (TOGAF/IBM/Australian National Archives/BrowserStack) | 4.2 | SOURCED | Real named sources with live URLs; not named in exec-summary prose itself (deliberate, per altitude rule), but real if the full report needs it |
| UK GDS + 18F/USDS iterative-delivery precedent | 4.2–4.4 | SOURCED | Real GOV.UK publication (Oct 2021), independently fact-checked via WebSearch/Perplexity, logged as E-088. Best-grounded citation found in the whole audit. **Not currently reflected in the 4.2/4.3/4.4 sidecars' "Source" column**, which cite only the internal agile-delivery note. |
| NESDC loss/damage economic-valuation methodology | 4.3 | SOURCED | Real public workshop presentation (NESDC & TORCG, 18 June 2026) with actual formulas and named data sources |
| Generic "Agile"/MVP framing | 4.3, 4.4 | GAP (low-risk) | No external source cited for the general concept; defensible under house style's "well-understood theory" exemption — do not backfill with E-088, which supports a more specific claim |

### Full-report writing plan layer
| Claim | Status | Note |
|---|---|---|
| TOGAF/IBM/Australian National Archives/BrowserStack SDLC synthesis | SOURCED | Confirmed — mixed authority (TOGAF is a real standards body; IBM/BrowserStack are vendor pages, treat as illustrative not authoritative) |
| Paris Agreement Art.13/UNFCCC/A-BTR, NAP | SOURCED | Same E-062/E-077 grounding as exec-summary layer |
| UK GDS/18F-USDS (E-088) | SOURCED | Best-grounded citation in the audit; registry entry records its own verification method and date |
| CWE-840 "Business Logic Vulnerabilities" | **PARTIAL — evidence-line error** | Real, independently verifiable (MITRE CWE catalog). The plan's §4.4.4 evidence line cites E-038/E-040/E-068/E-074/E-075 — **none of which actually contain this material**. The real source is E-072, which exists but isn't listed for this claim. Mechanical fix: correct the citation line. |
| Loss/damage valuation methodology (academic partner) | **PARTIAL — evidence-line gap** | Real source exists (`inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md`, names Chulalongkorn Engineering as methodology partner) but §4.3.3's evidence line cites E-015/E-060, neither of which contains this content. Add the NESDC/TORCG slide as an explicit citation. |
| ISO 14090/14091 | N/A | Appears only as a style-guide example of how to phrase a citation, not an actual claim in the body — no action needed |

**Chapter 4 priority actions**: two evidence-line corrections (§4.4.4 CWE-840 → cite E-072; §4.3.3 → add the NESDC/TORCG slide) are quick, mechanical fixes. The A-BTR/Paris Agreement/UK-GDS grounding is already the strongest in the project and just needs surfacing into the sidecars that currently under-cite it.

---

## Overall priority list (highest leverage first)

1. **Chapter 3 — DesInventar & DaLA**: real sources already exist, zero new research needed, directly answers what Boss flagged.
2. **Chapter 4 — two evidence-line corrections** (CWE-840, loss/damage methodology): mechanical, sources already exist.
3. **Chapter 1 — A-PLAT/KlimAdapt**: source already exists (`5.2.1`), just needs linking; also feeds Chapter 2's same gap.
4. **Chapter 2 — มสพร. 1-2564 and ISO 19115**: genuine research gaps, no primary document anywhere in the project — these need to be fetched before they can be cited.
5. **Chapter 1 — IPCC/WMO/UNFCCC "content-category" claim** and **Chapter 3 — "Build Back Better and Safer"**: genuine GAPs, mark HOLD or find sources.
6. **Chapter 3 — Thai statute reference** (พ.ร.บ. 2550 / แผน 2564–2570): genuine GAP, needs the actual legal text or its citation.
