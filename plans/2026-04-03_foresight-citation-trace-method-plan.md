# Plan: Foresight report citation trace method from research note to report claim

## Goal

Define an exact, repeatable method to trace evidence across the foresight workspace from:

`research note phrase` → `source number mark` → `works cited URL/title` → `SRC_ID` → `ART_PAR_ID` → `CLAIM_ID` → inline citation candidate in the report.

This plan treats [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md) as one example artifact, but the method is designed for all research material notes used in [[artifacts]]

## Core principle

The current chain in [`ψ/lab/foresight-report-wrting/citations/README-citation-workflow.md`](ψ/lab/foresight-report-wrting/citations/archive/README-citation-workflow.md) is close, but for deep-research notes it needs one more explicit internal step.

Operational chain:

1. `Quoted or paraphrased phrase` inside a research note paragraph
2. `Local reference number` attached to that phrase in the note
3. `Works cited entry` inside the same note
4. `Canonical source row` in [`ψ/lab/foresight-report-wrting/citations/citation-registry.md`](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md)
5. `Artifact paragraph row` in [`ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md`](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md)
6. `Report claim row` in [`ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md`](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md)
7. Inline citation or HOLD decision in [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md)

## Exact tracing method

### Step 1. Identify a candidate note paragraph

Input artifact:
- [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md)

Unit of work:
- one paragraph or paragraph-cluster that expresses one usable proposition for the report.

Example paragraph:
- public schools, state curriculum, cultural relevance, bilingual Thai-Melayu effort in [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md)

Rule:
- Do not map an entire note at once.
- Break into paragraph-level units only when the paragraph supports one coherent report-use claim.

### Step 2. Extract phrase-level evidence anchors

Within the paragraph, isolate phrase-level propositions and attach each to the cited number marks that immediately support it.

Example from [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md):
- `public schools under OBEC are the main vehicle of Education for All` → `8`
- `schools follow national curriculum and O-NET aligned standards` → `1`
- `curriculum often lacks cultural relevance for Malay-Muslim majority` → `1`
- `bilingual Thai-Melayu effort in about 15 primary schools` → `4`

Rule:
- A paragraph may map to multiple sources.
- The mapping must be phrase-aware, not only paragraph-aware.
- If a phrase has no number mark, it cannot be treated as source-backed just because adjacent phrases do.

### Step 3. Resolve source numbers to works-cited records

For each local number mark in the note:
- find its corresponding record in the note’s `Works cited` section.
- capture:
  - local number
  - displayed title
  - URL
  - access date if present

Example resolutions in [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md):
- `1` → `Transforming Islamic Education through Lesson Study LS A Classroom-Based Approach to Professional Development in Southern Thailand` → MDPI URL
- `4` → `Muslims in Southern Thailand` → MFA PDF URL
- `8` → `MAKE LEARNING COUNT` → UNICEF Thailand PDF URL
- `15` → `UNICEF and SBPAC join forces to promote well-being of children in Southern border provinces` → UNICEF press URL

Rule:
- The note’s local numbering is only local to that note.
- Never treat `1` in one note as the same source as `1` in another note.

### Step 4. Mint or reuse canonical `SRC_ID`

For each works-cited record:
- search [`ψ/lab/foresight-report-wrting/citations/citation-registry.md`](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md) by title or URL.
- if found, reuse existing `SRC_ID`.
- if absent, mint a new `SRC_ID`.

Recommended `SRC_ID` convention:
- `SRC-[ORG OR AUTHOR]-[YEAR OR ND]-[SHORT-SLUG]`

Example candidates:
- `SRC-MDPI-2024-LESSON-STUDY-SOUTH-TH`
- `SRC-MFA-ND-MUSLIMS-SOUTH-TH`
- `SRC-UNICEF-2024-MAKE-LEARNING-COUNT`
- `SRC-UNICEF-2026-SBPAC-WELLBEING`

Registry row must include:
- `SRC_ID`
- short label
- full citation text in target style or near-final placeholder form
- source type
- year
- primary access path as URL
- language
- notes on relevance

Rule:
- Canonical source de-duplication happens only in the registry.
- Artifact maps and claim maps must never create ad hoc bibliographic variants.

### Step 5. Mint or reuse `ART_ID` for the research note

Each research material note needs one stable artifact row in [`ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md`](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md).

Example:
- note file: [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md)
- proposed `ART_ID`: `ART-LEARNING-PATHWAYS-NOTE`

Rule:
- The research note itself is an artifact.
- Draft assemblies and rewrite files are also artifacts, but they should not replace the original evidence note in the chain.

### Step 6. Create paragraph-level `ART_PAR_ID` rows

For each usable paragraph or paragraph-cluster in the note:
- mint an `ART_PAR_ID`
- add one row to the artifact paragraph table

Recommended format:
- `LP-P01`, `LP-P02`, `LP-P03`
or, if you want stronger uniqueness,
- `ART-LEARNING-PATHWAYS-P01`

Each row should capture:
- `ART_ID`
- `ART_PAR_ID`
- location anchor such as heading + opening phrase
- evidence summary
- `LOC_REF_Label` using all local source numbers used in that paragraph, such as `1;4;8`
- `SRC_IDs` resolved from those local numbers
- evidence mode such as `mixed` or `synthesis`
- status
- notes

Important rule:
- `LOC_REF_Label` must preserve the note-local numbering as evidence breadcrumbs.
- `SRC_IDs` is the canonical translation of those numbers.

### Step 7. Link artifact paragraph to report claim

Now move to the report-side claim layer.

For each paragraph unit, ask:
- Which claim in [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md) does this support?
- Is it supporting an existing `CLAIM_ID`, or does a new `CLAIM_ID` need to be minted?

Example claim candidates:
- chapter 2 claim on fragmented learning pathways
- chapter 2 claim on mismatch between curriculum and local cultural-linguistic context
- chapter 3 scenario-axis claim on `learning pathway connectivity`
- chapter 4 leverage-point claim on improving pathway recognition and smoother transitions

Rule:
- One artifact paragraph may support multiple claims.
- One claim may depend on multiple artifact paragraphs.

### Step 8. Decide citation-ready vs synthesis-only vs HOLD

After linking `ART_PAR_ID` to `CLAIM_ID`, classify the claim:

- `Inline_Citation_Ready = yes`
  - when the report wording can be directly supported by the mapped sources without overreach.
- `Inline_Citation_Ready = no`
  - when the claim is still broader than the available sources.
- `HOLD`
  - when the report wording currently asserts more than the sources actually show.

Decision rule:
- Specific empirical statements from the note can often become inline-citation-ready.
- Broad synthetic foresight statements often need multiple notes and multiple `SRC_ID`s before they are ready.

## Worked example using Learning Pathways

### Example evidence unit

Source paragraph in [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md):
- paragraph under `### Mainstream Public Schools and the State Mandate`

Phrase-level breakdown:
- phrase A: OBEC public schools are main vehicle for national Education for All → local ref `8`
- phrase B: national curriculum and O-NET alignment → local ref `1`
- phrase C: cultural relevance problem for Malay-Muslim majority → local ref `1`
- phrase D: bilingual Thai-Melayu effort in about 15 schools → local ref `4`

Canonical trace target:
- `ART_ID = ART-LEARNING-PATHWAYS-NOTE`
- `ART_PAR_ID = LP-P02-PUBLIC-SCHOOLS`
- `LOC_REF_Label = 1;4;8`
- `SRC_IDs = SRC-MDPI-2024-LESSON-STUDY-SOUTH-TH; SRC-MFA-ND-MUSLIMS-SOUTH-TH; SRC-UNICEF-2024-MAKE-LEARNING-COUNT`

Candidate report claims supported:
- a chapter 2 claim that children face structurally fragmented learning environments where state schooling does not always align with local language and identity realities
- a chapter 3 claim that future differences in `learning pathway connectivity` partly depend on whether institutions can bridge national standards with local cultural-linguistic relevance

Important caution:
- the paragraph does **not** by itself support a bigger claim like `learning pathways are the dominant determinant of all future youth outcomes`.
- that larger claim would require synthesis across multiple research notes and additional claim mapping.

## File updates needed

### 1. Update [`ψ/lab/foresight-report-wrting/citations/README-citation-workflow.md`](ψ/lab/foresight-report-wrting/citations/archive/README-citation-workflow.md)

Add one explicit subsection for deep-research notes:
- explain that local source numbers in research notes are note-local only
- require phrase-to-number extraction before paragraph-to-source mapping
- document the chain:
  - `note phrase` → `LOC_REF` → `works cited entry` → `SRC_ID` → `ART_PAR_ID` → `CLAIM_ID`

### 2. Update [`ψ/lab/foresight-report-wrting/citations/citation-registry.md`](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md)

Add real source rows for the first batch of frequently reused citations from research notes.

Immediate first batch from [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md):
- MDPI lesson study source
- MFA southern Thailand overview source
- UNICEF Make Learning Count source
- UNICEF and SBPAC joint well-being source
- plus the already used vulnerability memo if retained as internal synthesis source

Recommended new columns if you want easier operations:
- `Canonical_URL_Key`
- `First_Seen_In_Artifact`

These are optional, but useful for de-duplication.

### 3. Update [`ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md`](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md)

Add artifact registry rows for all major research material notes, not just assemblies.

Immediate additions:
- `ART-LEARNING-PATHWAYS-NOTE`
- similar `ART_ID`s for:
  - [`ψ/lab/foresight-report-wrting/artifacts/Child and Youth Vulnerability in Thailand’s Southern Border Provinces.md`](ψ/lab/foresight-report-wrting/artifacts/source/Child%20and%20Youth%20Vulnerability%20in%20Thailand’s%20Southern%20Border%20Provinces.md)
  - [`ψ/lab/foresight-report-wrting/artifacts/Livelihoods in the Deep South.md`](ψ/lab/foresight-report-wrting/artifacts/source/Youth%20Livelihoods%20in%20the%20Deep%20South%20and%20Opportunity%20Structures.md)
  - [`ψ/lab/foresight-report-wrting/artifacts/Belonging, identity, and cultural capital.md`](ψ/lab/foresight-report-wrting/artifacts/source/Belonging,%20identity,%20and%20cultural%20capital.md)

Then add paragraph rows for the first 3 to 5 high-value paragraphs in each note.

Recommended table change:
- add a new column: `Phrase_Anchor`

Purpose:
- to capture a short quoted or paraphrased phrase inside the paragraph that was actually used to attach the local refs.

This is the missing granularity for deep-research notes.

### 4. Update [`ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md`](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md)

Add real claim rows tied to v3 sections that consume research-note evidence.

For the first pass:
- prioritize chapter 2 and chapter 3 claims that obviously depend on:
  - learning pathway fragmentation
  - transition bottlenecks
  - language and cultural relevance mismatch
  - access and trust mechanisms

Recommended table change:
- add a column: `Used_In_Report_Text`

Values:
- `yes`
- `planned`
- `no`

This helps separate:
- claims already stated in v3
- claims only present in evidence notes
- claims planned for future redraft

### 5. Update [`plans/2026-04-02_foresight-report-v3-citation-hardening-next-session-plan.md`](plans/2026-04-02_foresight-report-v3-citation-hardening-next-session-plan.md)

Append a concrete operational sequence:

1. populate registry from research-note works cited lists
2. mint `ART_ID` for each major research note
3. map top paragraph units with `ART_PAR_ID`
4. link paragraph units to chapter 2 and 3 `CLAIM_ID`s first
5. only then insert inline citations into [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3.md)

## Recommended execution order

### Pass A. Source normalization
- extract works cited rows from major research notes
- mint and deduplicate `SRC_ID`s

### Pass B. Artifact mapping
- add research-note `ART_ID`s
- add high-value `ART_PAR_ID`s with `LOC_REF_Label` and `Phrase_Anchor`

### Pass C. Claim alignment
- audit chapter 2 and 3 claims in the integrated draft
- link each high-stakes claim to one or more `ART_PAR_ID`s

### Pass D. Draft citation insertion
- only add inline citations where `Inline_Citation_Ready = yes`
- otherwise revise language or mark HOLD

## Best implementation mode

Best mode for execution is [`switch_mode()`](server.js:1) to `code` mode.

Reason:
- the work now is operational population of markdown tables and targeted edits across [`citation-registry.md`](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md), [`artifact-paragraph-source-map.md`](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md), [`report-claim-evidence-map.md`](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md), and possibly [`README-citation-workflow.md`](ψ/lab/foresight-report-wrting/citations/archive/README-citation-workflow.md).

## Approval checkpoint

If approved, the next implementation session should start by treating research material notes as first-class evidence artifacts, beginning with [`ψ/lab/foresight-report-wrting/artifacts/Learning Pathways.md`](ψ/lab/foresight-report-wrting/artifacts/source/Fragmented%20Learning%20Pathways%20and%20Systemic%20Discontinuities%20in%20the%20Southern%20Border%20Provinces.md) and the other major note files used in v3.
