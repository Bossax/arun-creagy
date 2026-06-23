# NotebookLM Phase 1 Error-Handling Workflow

## Purpose

This note records the practical error-handling workflow used in this session for Phase 1 extraction under [`Collaborative_Writing_Plan-TOR5.5.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/Collaborative_Writing_Plan-TOR5.5.md:78).

The goal is to preserve a stable operating pattern when NotebookLM MCP is slow, times out, or returns incomplete results.

---

## Core Principle

Do **not** bundle large extraction requests into one prompt.

Instead:
- keep each NotebookLM query **atomic**
- allow one subtask to run a **packet** of atomic queries in sequence
- write the packet outputs into an intermediate artifact such as [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART03_PLOS_Infectious_Diseases/raw-copy.md:1)
- synthesize the canonical [`01_Raw_Extraction.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART03_PLOS_Infectious_Diseases/01_Raw_Extraction.md:1) only after the packet is complete

This preserves source discipline while reducing orchestration overhead.

---

## Session Pattern Used

### 1. Exact source anchoring

Always resolve the paper title from [`TOR5.5_Articles_Summary_Table.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/TOR5.5_Articles_Summary_Table.md:1).

Do not invent or paraphrase the source name.

---

### 2. Atomic query packet

Phase 1 was decomposed into atomic queries such as:

- exact-title gate + section outline only
- variables by section only
- tables only
- figures only
- core hypothesis + named labels only
- adaptive deepening query A
- adaptive deepening query B
- limitations / uncertainties / model parameters / data gaps only

Each query asked for **one thing only**.

---

### 3. One subtask may run many atomic queries

The inefficient pattern was one subtask per query.

The improved pattern is:

1. one query-runner subtask opens one fresh NotebookLM session
2. it runs the ordered atomic packet in that same subtask
3. it writes all raw outputs to [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART0xxx/raw-copy.md:1)
4. it closes the session
5. a second synthesis subtask creates [`01_Raw_Extraction.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART0xxx/01_Raw_Extraction.md:1)

This is the preferred operational model going forward.

---

## Timeout Handling Rule

If NotebookLM MCP times out:

1. assume the query was **likely sent successfully**
2. do **not** keep retrying immediately
3. record the timeout state in [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART03_PLOS_Infectious_Diseases/raw-copy.md:1)
4. let the human manually paste the returned NotebookLM content into the same intermediate artifact
5. continue synthesis only from what is actually present in the pasted raw artifact

This avoids duplicate probing and reduces wasted MCP cycles.

---

## Session Controls Used

For NotebookLM query subtasks in this session:

- create a **new NotebookLM session** per query-runner subtask
- use **typing speed minimum 400** when supported
- close the NotebookLM session after the packet finishes

This keeps runs isolated and makes timeout behavior easier to reason about.

---

## Intermediate Artifact Rule

[`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART0xxx/raw-copy.md:1) is the working intake surface for raw NotebookLM outputs.

It should contain:

- clearly labeled packet sections such as `Step 1A`, `Step 1B`, `Step 1C`, etc.
- raw pasted NotebookLM outputs
- timeout placeholders where response capture failed

It should **not** be treated as the final canonical artifact.

---

## Canonical Synthesis Rule

Only after the packet is complete should the agent write [`01_Raw_Extraction.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/ART0xxx/01_Raw_Extraction.md:1).

When synthesizing:

- follow the schema defined in [`Collaborative_Writing_Plan-TOR5.5.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghographic/Collaborative_Writing_Plan-TOR5.5.md:152)
- use only evidence explicitly present in [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic/ART0xxx/raw-copy.md:1)
- leave unsupported fields empty rather than inferring
- preserve failed early artifacts for traceability

---

## Practical Lessons from This Session

1. Large bundled prompts degrade reliability.
2. Atomic prompts improve control and make failure localized.
3. The right efficiency unit is **one packet subtask**, not one query subtask.
4. Manual paste fallback is necessary when NotebookLM MCP times out after send.
5. [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic/ART0xxx/raw-copy.md:1) should be treated as the durable bridge between NotebookLM execution and canonical JSON synthesis.

---

## Recommended Reusable Workflow

For each new paper folder under [`TOR5.5_article_and_infoghographic`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic:1):

1. resolve exact source title from [`TOR5.5_Articles_Summary_Table.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic/TOR5.5_Articles_Summary_Table.md:1)
2. run one query-runner subtask with an ordered atomic packet
3. capture outputs in [`raw-copy.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic/ART0xxx/raw-copy.md:1)
4. use manual paste fallback for timed-out steps
5. run one synthesis subtask to produce [`01_Raw_Extraction.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infographic/ART0xxx/01_Raw_Extraction.md:1)
6. preserve any failed raw artifacts as audit evidence

This is the stable error-handling and execution workflow established in this session.
