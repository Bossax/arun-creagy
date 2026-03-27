# Plan — CRDB Interim Report v3: rewrite clause drafts into paragraph-first, v1-aligned prose (TOR-only headings)

## 1) Diagnosis (why the last session drifted)

### 1.1 The style pack template got treated as the final output structure
The template in [`ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25_writing-th-style-pack_crdb-interim-report-v3.md:163) is explicitly **partitioned and list-driven** (Summary bullets, Key points list, Evidence bullets, Implications bullets). Even though it says it is scaffolding, it shaped the drafts into bullets + subsections rather than report prose.

### 1.2 Unwanted subsections were injected
Example: [`ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md:3) includes `### สรุปสำหรับผู้บริหาร (ย่อ)` / `### ผลการดำเนินงานและหลักฐานอ้างอิง` / `### ประเด็นสำหรับภาคผนวก` / `### ข้อมูลที่ต้องยืนยัน/ยังขาด`. These read like internal working notes and don’t match the v1 narrative style.

### 1.3 Citation policy was violated (internal artifacts treated as sources)
Repo MD files (`ψ/...`) are project artifacts, not citable sources for DCCE. The drafts embed repo links directly in-body (example: [`ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md:4)).

## 2) Target output specification (what we will produce)

### 2.1 DCCE-facing clause drafts (public deliverables)
**Goal**: rewrite the existing clause drafts into paragraph-first Thai report prose aligned to v1 voice.

**Deliverable shape**: new topic-wise files (one file per TOR clause) in TOR order: `5.2.1` … `5.5.2`.

Hard rules:
- Paragraph-first. Bullets allowed only when:
  - the list itself is a TOR-required output (e.g., List A/List B), or
  - a short enumeration improves readability (<= 5 bullets).
- Remove template subsections (`### สรุปสำหรับผู้บริหาร (ย่อ)` etc). Keep headings limited to the chosen structure (see Section 3).
- No repo file paths (`ψ/...`) and no internal markdown links in the DCCE-facing drafts.
- Evidence is referenced only as **appendix signposting** with human-readable labels (or placeholders like **[ต้องชี้ภาคผนวก]**).
- All `ข้อมูลที่ต้องยืนยัน/ยังขาด` content is removed from the DCCE-facing drafts.

### 2.2 Explicitly rejected deliverables
You requested **no internal companion documents** for this rewrite round:
- No internal traceability map
- No internal QA gaps log

We will still *use* evidence artifacts as inputs when necessary, but we will not generate internal companion outputs as part of this pass.

## 3) Final structure (approved)

Approved choice: **Option A — TOR-only headings**

- Use only `5.2.1 … 5.5.2 …` headings in order.
- Paragraph-first prose under each clause.
- No internal subsections.
- Preserve v1 language and writing style as the primary voice reference.

## 4) Concrete rewrite workflow (repeatable per clause)

Inputs:
- v1 narrative base: [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md)
- v3 clause drafts: e.g., [`ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md)
- v3 plan: [`ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-CRDB-Interim-Report-Writing-Plan-v3.md)

### 4.1 Create new rewritten clause drafts (do not overwrite old drafts)

For each existing clause draft file:
- input: `ψ/incubate/DCCE/CRDB/output/5.x.x-Interim-Report-v3-draft.md`
- output: `ψ/incubate/DCCE/CRDB/output/5.x.x-Interim-Report-v3-prose-draft.md`

Each new file must start with a short provenance note linking back to the original draft, for traceability without creating a separate internal document.

Example header block (top of file):
- `อ้างอิงฉบับร่างเดิม: ...` linking to the old draft file
- `แนวทางการปรับแก้: ...` one paragraph describing “bullets → paragraphs, removed internal subsections, removed repo links”

### 4.2 For each clause draft (5.2.1 … 5.5.2)
For each file like [`ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md`](ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md:1):

1) Extract “real content”
   - keep factual statements, counts, and validated findings
   - drop/remove scaffolding subsections

2) Recompose into paragraph-first prose
   - 1 paragraph: TOR scope + what was done + status
   - 2–4 paragraphs: key findings + rationale + implications
   - keep bullets only where required (lists, counts, short enumerations)

3) Replace repo links with appendix signposting
   - convert `(ดู [ψ/...])` into `ดูภาคผนวก: …` or placeholders like **[ต้องชี้ภาคผนวก]**

4) Remove “to verify / missing” blocks
   - everything under `ข้อมูลที่ต้องยืนยัน/ยังขาด` is removed from the clause draft
   - if essential, convert into a neutral statement of current status that does not read like internal QA (only when it is appropriate for DCCE-facing progress reporting)

### 4.3 Integration pass
After all clauses are rewritten:
- remove repetition introduced by clause boundaries
- normalize terms (DCCE / NCAIF / CRDB)
- verify List A/List B “≥10” claims are present where required (but not as internal links)
- ensure the public draft contains no `ψ/` strings

## 5) Citation policy (strict)

### 5.1 DCCE-facing draft
- No citing internal project artifacts.
- Only cite external sources when the org/author + year can be named with confidence.
- Otherwise write as “project progress” grounded statements (no pseudo-citations).
 
## 6) Evidence usage policy (inputs only)

Evidence artifacts (tables/notes) may be pulled in only when needed to correct/complete the prose, but:
- they are not referenced as `ψ/...` links
- they are described as appendices or supporting documents in human-readable terms

## 7) Acceptance checks (objective)

For the DCCE-facing main body:
- contains no `ψ/` file paths
- contains no template subsections (no `### สรุปสำหรับผู้บริหาร (ย่อ)` etc)
- bullet usage is limited to justified cases

If we want a mechanical check, we can run [`tools/crdb_style_diag.ts`](tools/crdb_style_diag.ts:1) once we’re in implementation mode.

## 8) Clause-specific content emphases (from human brief)

These points refine *what* each clause should emphasize in the rewritten prose (beyond style/structure):

- **5.2.1** — Benchmark of adaptation information platforms
  - Focus: how climate change adaptation information platforms differ in **design principles, target groups, and information architecture**.
  - Emphasize **lessons from T-PLAT** as the key contextual anchor for Thailand.
  - Keep the narrative on what these lessons imply for NCAIF design (not on every platform detail).

- **5.2.2** — Current DCCE website structure (pilot applied)
  - Focus: what the **existing DCCE website information architecture** looks like today.
  - Include analysis from **user experience and information architecture** perspectives:
    - how navigation, content grouping, and entry paths behave for real users;
    - where it falls short as an adaptation information architecture (fragmentation, buried content, lack of task-oriented paths).
  - Explicitly highlight **which existing content can be reused** in NCAIF as-is or with light adaptation.

- **5.2.3** — Deriving NCAIF structure
  - Focus: how the NCAIF structure was derived from **literature review + stakeholder interviews**.
  - Include the **full sitemap** from the "Sitemap vNext (interim report refinement) - superseded 2026-03-12 10:50" section in [`ψ/incubate/DCCE/CRDB/output/National\ Climate\ Adaptation\ Information\ Framework.md`](ψ/incubate/DCCE/CRDB/output/National\ Climate\ Adaptation\ Information\ Framework.md:181), adapted into paragraph narrative (not raw bullet dump).
  - Make clear how literature and interviews shaped the sitemap decisions.

- **5.2.4** — Focus group consultations
  - Focus: **objectives of the focus group discussions**, who participated, and what they were asked to react to.
  - Summarize **key outcomes** and how these outcomes were used to adjust NCAIF and related structures in this project.
  - Treat FGD content as a design input story, not as minutes.

- **5.2.5** — Revisions & data management structure
  - Focus: bring the **full sitemap structure that previously lived in a v1 appendix** into this section and explain it.
  - Clearly explain how this sitemap and data-management structure **differs from 5.2.3** (e.g., governance/data-structure view vs user-facing sitemap view).
  - Include full detail of the **data governance structure** (roles, responsibilities, rails), framed as narrative rather than internal checklist.

- **5.3.2** — Interview-based demand (content re-anchor)
  - Focus: **summarize the interview results** here in one place (counts, agencies, key themes).
  - Move **use cases and MVPs discussion** that currently lives elsewhere into this section, to keep “demand and use cases” tightly coupled.
  - Ensure the narrative makes clear how interview findings drive MVPs and NCAIF service design.

These emphases apply on top of the style and structural rules above and should guide the paragraph-level choices when rewriting each clause.
