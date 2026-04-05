# Foresight 2590 – Operational Grounding and Citation Process (Numeric Version)

This document defines the standard procedure for grounding and citing any part of the Foresight 2590 report. It ensures that every factual claim is traced back to a credible **external source** while maintaining a consistent and professional citation surface.

---

## Grounding & Citation Rules

To ensure a credible, audience-facing report, the following rules apply:
1. **No Internal Citations:** Do NOT cite internal project files (e.g., team input `.md` files, synthesis notes, or internal draft logs) in the final report.
2. **Trace to Original Sources:** If a claim requires backing, you must trace it back to the *original external source* (e.g., academic paper, news article, official data source, NGO report).
3. **Logic vs. Evidence:** Original team logic, synthesis claims, or framework definitions developed by the project team do not require external citations. Only factual claims about the world or specific data points require backing.
4. **Numeric Inline Citations:** Use numeric markers in square brackets (e.g., [1], [2]) for all inline citations. This decouples substantive drafting from bibliographic perfection.

---

## The Core Operational Loop (A -> B -> C)

This workflow is the standard operating procedure for grounding any chapter, sub-chapter, or section.

```mermaid
flowchart TD
  Start[Start section grounding] --> StepA[Step A: Extract claims needing backing]
  StepA --> Verify[Verify claims with Human]
  Verify --> StepB[Step B: Search Evidence Library]
  StepB --> EvidFound{Evidence found?}
  EvidFound -- yes --> Insert[Insert numeric inline citation [n] in prose]
  EvidFound -- no --> StepC[Step C: Dig for External Source]
  StepC --> Trace[Trace internal notes to original source]
  Trace --> ExtFound{External source found?}
  ExtFound -- yes --> LogNew[Log in Evidence & Citation Libraries]
  LogNew --> Insert
  ExtFound -- no --> MarkGap[Mark gap or weaker support]
  Insert --> UpdateBib[Update Works Cited with numeric mapping]
  UpdateBib --> NextClaim[Move to next claim]
  MarkGap --> NextClaim
  NextClaim --> Done{Section Done?}
  Done -- no --> StepB
  Done -- yes --> Review[Final style & logic check]
```

### Step A: Claim Extraction & Human Verification
- Identify specific factual claims that require external backing.
- **Action:** Present the list to the user and ask: *"Are these the claims you want me to find actual external sources for?"*

### Step B: Search Evidence Library
- For each confirmed claim, first search [`ψ/lab/foresight-report-wrting/citations/evidence-library.md`](ψ/lab/foresight-report-wrting/citations/evidence-library.md).
- If a match is found that references an **external source**, proceed to citation insertion.

### Step C: Trace to External Sources (via internal notes)
- If no match in Step B, consult internal synthesis/deep research files to locate the *original external source* (e.g., if a synthesis note mentions "IPCC 2023", find the actual IPCC report details).
- **Rule:** Do not cite the internal file. Only cite the original external source.
- Update [`citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md) and [`evidence-library.md`](ψ/lab/foresight-report-wrting/citations/evidence-library.md) with new external findings.

### Prose Insertion & Style Benchmarking
- Insert numeric citations: `[n]`.
- Benchmark against [`plans/foresight-report-writing-style-pack.md`](plans/foresight-report-writing-style-pack.md).

---

## Global Consistency, QA, and Final Clean-up

Once the grounding loop has been applied to all required sections, conduct a final global check before completion:

1. **Citation Surface QA:** Review the entire document for consistent numeric formatting and verify no orphaned or broken references.
2. **Works Cited Reconciliation:** Ensure every numeric marker `[n]` has a corresponding entry in `works-cited.md`.
3. **Zero-Internal-Citation Audit:** Perform a final scan to guarantee that NO internal project files (e.g., `.md` notes) are cited in the audience-facing text.

---

## Operational TODO Checklist

- [x] **Update Plan:** Shift to numeric citation standard.
- [ ] **Infrastructure Check:** Verify `citation-library.md` and `evidence-library.md` are ready for external source logging.
- [ ] **Grounding Loop (Step A):** Extract claims for the current section and verify with Human.
- [ ] **Grounding Loop (Step B):** Search `evidence-library.md` for confirmed claims.
- [ ] **Grounding Loop (Step C):** Trace missing claims back to external sources via internal notes (strictly no internal citations).
- [ ] **Insertion:** Update prose with numeric citations `[n]` and sync `works-cited.md`.
- [ ] **Style & Logic:** Final section-level benchmark and human review.
- [ ] **Final QA:** Global consistency check and final clean-up across all sections.
