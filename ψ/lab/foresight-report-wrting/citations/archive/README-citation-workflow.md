# Foresight 2590 – Citation System (Template Workspace)

This folder provides a markdown-first, append-friendly citation workflow for the foresight report.

The system is designed to support a trace chain:

> **Report claim / paragraph → Artifact paragraph → Local reference number in artifact → Works-cited entry → Canonical source record**

Use the files in this folder together:

1. **Canonical source registry** – long-lived record of all sources
   - [ψ/lab/foresight-report-wrting/citations/citation-registry.md](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md)
2. **Artifact → source mapping** – how each artifact paragraph and local ref number connects to sources
   - [ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md)
3. **Report claim → evidence mapping** – how each report claim is backed by artifacts and sources
   - [ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md)

All tables are designed for incremental filling by humans and agents.

---

## 1. Canonical source registry

File: [ψ/lab/foresight-report-wrting/citations/citation-registry.md](ψ/lab/foresight-report-wrting/citations/archive/citation-registry.md)

- One row per *canonical* source (report, article, dataset, transcript, law, interview, etc.).
- Each source gets a stable **`SRC_ID`** (e.g. `SRC-TH-LAW-2542-EDU`, `SRC-UNICEF-2024-YOUTH-SB`).
- This file is the backbone for all other mappings.

Suggested workflow:

1. When a new source is accepted into the evidence base, mint a `SRC_ID` and add a row.
2. Use the same `SRC_ID` in:
   - artifact local-reference mappings, and
   - report claim mappings.
3. At report layout time, generate the **Works Cited** section by exporting or copying from this registry.

---

## 2. Artifact paragraph → source mapping

File: [ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md)

Purpose:

- Make each *artifact paragraph* (or block) traceable back to canonical sources.
- Maintain a mapping between any **local reference numbers** used inside an artifact (e.g. `[1]`, `[2]`, `(a)`) and canonical `SRC_ID`s.

Typical usage pattern:

1. Assign a stable **`ART_ID`** to each artifact file you care about.
2. As you annotate the artifact (manually or with an agent), give key paragraphs an **`ART_PAR_ID`** (e.g. `CH2-P05`, `SCEN-B-PAR-03`).
3. If the artifact uses local numbers (e.g. `[1]`, `[2]`), map them to `SRC_ID`s in this file.
4. Record how each paragraph is supported (direct quote, summary, synthesis).

This file makes it possible to answer: *“Where did this artifact paragraph come from, and which sources does it rely on?”*

---

## 3. Report claim → artifact → source mapping

File: [ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md)

Purpose:

- Track how each important **report claim or paragraph** is backed by artifacts and canonical sources.
- Enable a clean audit trail before finalizing the edited draft.

Typical usage pattern:

1. Assign a **`CLAIM_ID`** to each high-stakes claim or paragraph in the report draft (e.g. `C1-TRUST-ACCESS-01`).
2. Link each `CLAIM_ID` to one or more `ART_PAR_ID`s from the artifact map.
3. Pull the corresponding `SRC_ID`s (and, where relevant, local reference numbers) into the row.
4. Mark whether the claim is currently **evidence-backed**, **synthesis-backed**, or **unsupported**.

This mapping allows you to see, for any report claim:

- which artifacts were used to construct it, and
- which canonical sources ultimately support it.

---

## 4. Minimal workflow example

1. **Source entry** – Add a new report on youth livelihoods to `citation-registry.md` with `SRC_ID = SRC-YOUTH-LIVELIHOODS-2024`.
2. **Artifact annotation** – In an evidence artifact, tag a paragraph about youth migration as `ART_PAR_ID = CH2-P07` and record that it draws on `SRC-YOUTH-LIVELIHOODS-2024`.
3. **Report claim** – When drafting chapter 2, assign `CLAIM_ID = C2-MIGRATION-01` to a paragraph describing youth out-migration.
4. **Link chain** – In `report-claim-evidence-map.md`, link `C2-MIGRATION-01 → CH2-P07 → SRC-YOUTH-LIVELIHOODS-2024`.

Later, inline citations in the public report can be generated from `SRC_ID` entries, and the Works Cited section can be assembled from `citation-registry.md`.

---

## 5. Conventions

- **IDs**
  - `SRC_ID` – canonical source (global across the project)
  - `ART_ID` – artifact file identifier
  - `ART_PAR_ID` – paragraph/block identifier within an artifact
  - `CLAIM_ID` – report claim/paragraph identifier
  - `LOC_REF` – local reference number/label inside an artifact (e.g. `1`, `2`, `a`, `b`)
- **Status flags**
  - Use short status codes such as `todo`, `draft`, `checked`, `disputed`.
- **Append-friendly**
  - Prefer adding new rows at the bottom of tables.
  - Avoid renaming IDs once minted.

