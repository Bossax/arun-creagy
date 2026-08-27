# Editorial Rubric v5.0.0

This rubric governs semantic review. It is not a replacement for source
verification or the mechanical linter.

## Core dimensions

Every review must decide each dimension with `pass`, `fail`, or, where allowed,
`not_applicable` and cite a location or concrete reason.

1. **section_job** — The section performs the one job approved in the contract
   and does not repeat adjacent sections or drift into excluded work.
2. **audience_decision_value** — The prose foregrounds what the intended reader
   needs to understand, decide, fund, govern, or do; it does not foreground the
   consultant's workflow without a reader-facing reason.
3. **evidence_payload** — Each substantive argument unit contains enough claim,
   concrete evidence, consequence, and mechanism to support its purpose. These
   elements may span more than one paragraph.
4. **causal_logic** — Evidence, interpretation, consequence, and response are
   connected without reversed causality, unsupported leaps, or decorative
   transitions.
5. **reader_facing_appropriateness** — No sourcing metadata, prompt residue,
   internal artifact locators, fake diagrams, or commentary about the document's
   upcoming structure remains in final prose.
6. **terminology_agency** — Terms remain stable and comprehensible; named actors
   perform the actions they actually own; project, consultant, client, and system
   are not substituted for one another.
7. **source_fidelity** — Required concepts, caveats, distinctions, quantitative
   values, and technical structures survive according to the contract. Only
   `new` mode may use `not_applicable`.
8. **form_readability** — Paragraphs, lists, tables, and figure placeholders
   match the information shape. No rule against rhetorical enumeration may be
   misapplied as a ban on useful lists.

## Executive-summary profile

Apply these additional dimensions when `profile` is `executive-summary`:

1. **altitude** — The section stays at decision-maker depth. It synthesizes
   detail instead of reproducing full-report methods, per-platform treatment,
   or evidence tables excluded by the contract.
2. **headline_conclusion** — The reader can identify the governing finding or
   decision consequence without reconstructing it from project activities.
3. **findings_over_process** — National or institutional stakes, findings, and
   resulting decisions take priority over descriptions of how the team worked.

An executive-summary opening should normally establish a concrete stake or
finding, interpret why it matters, and position the deliverable as the response.
Generic scene setting such as “ในปัจจุบัน...” is insufficient unless followed
immediately by concrete evidence that earns it.

## Other profiles

- **report** — Require complete technical distinctions, traceable evidence,
  explicit limitations, and sufficient implementation detail for the section's
  approved job.
- **article** — Require a clear thesis, reader-oriented progression, evidence
  attribution, and accessible explanation without weakening factual precision.
- **letter** — Require an explicit purpose, recipient-relevant context, requested
  action, responsible actor, and deadline or next step when applicable.

## Review protocol

1. Read the approved contract before the draft.
2. Read the draft once for the reader's experience, then again against every
   inclusion, exclusion, and required concept.
3. Locate findings precisely. Do not accept the drafting agent's summary as
   evidence of compliance.
4. Classify findings:
   - `critical`: fabricated evidence, wrong audience/artifact, reversed core
     logic, or content that makes the deliverable unsafe to use.
   - `major`: scope/altitude failure, missing governing conclusion, lost required
     substance, internal artifact leakage, or systematic reader confusion.
   - `minor`: local clarity, grammar, formatting, or terminology defect that does
     not change the governing meaning.
5. A `pass` receipt may contain only resolved critical/major findings. Minor
   findings may be unresolved only when their disposition explicitly accepts
   them for human review.
6. If the draft changes, discard the verdict and review the new hash.

