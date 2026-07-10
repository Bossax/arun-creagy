# Decision Log — Adaptation Division Semantic Governance

**Date:** 2026-07-10  
**Purpose:** Record design-governance decisions, unresolved questions, and follow-up notes while the semantic-governance design continues.

---

## Vocabulary Used in This Note

To avoid confusion, this note will use only these two terms:

- **Iteration** = one round of research work. An iteration may contain **multiple NotebookLM queries**, followed by synthesis and discussion.
- **Phase** = a stage of the actual DCCE implementation roadmap.

So:
- the earlier research work should be called **Iteration 1**, **Iteration 2**, and so on
- the DCCE roadmap should be called **Phase 1** and **Phase 2** only when referring to implementation stages

---

## Research Progress Snapshot

- **Current status:** We are at the **end of Iteration 2**.
- **Iteration 1:** broad architecture groundtruth + initial discussion of governance issues.
- **Iteration 2:** PDF-based semantic-governance hardening using multiple single-question NotebookLM queries.
- **Implementation phases:** separate from research iterations; they refer to the DCCE roadmap only.

---

## Iteration 1 Summary

This log should also preserve the key reasoning established before the explicit decision list was written.

### What Iteration 1 established
- The initial architecture groundtruthing concluded that the proposal was **directionally correct** on three major points:
  - loose coupling between source systems and the canonical layer
  - metadata-driven control / semantic mediation
  - separation between governed data assets and presentation / consumption layers
- The early concern was that the proposal did not yet make **governance and ownership mechanics** explicit enough.

### Your clarifications during discussion
- You clarified that **domain ownership was already proposed in FGD 3**, with data-owner roles assigned to sub-divisions under the Adaptation Division.
- You clarified that department-wide data strategy is related to the role of the **DCIO** in the DCCE governance manual, but that the current project should not over-claim a department-wide federated governance model yet.
- You stated that the current platform can instead serve as a **best-practice seed** for future wider governance adoption.
- You confirmed that the platform will likely need **its own glossary**, while also acknowledging the reality that the M&E platform already has another glossary.
- You raised the practical question of whether **content change responsibility can be assigned per topic**, similar to owner roles.

### What Iteration 1 left unresolved
- After your clarifications, the main unresolved issue was no longer "who owns each domain?"
- The actual unresolved issue became the **boundary between topic-level content editing and semantic-definition governance**.
- That reframed the next design discussion away from abstract governance theory and toward practical operating rules for:
  - glossary control
  - semantic versioning
  - topic-owner editing boundaries
  - committee approval flow

### Why Iteration 2 was needed
- The next workstream was therefore framed as an **implementation-hardening discussion**, not a re-justification of the architecture.
- The PDF query series was launched specifically to test:
  - canonical/shared semantic model logic
  - metadata / ontology mechanisms
  - governance layering
  - content-change-management implications

---

## Iteration 2 Summary

### What Iteration 2 did
- Iteration 2 used a **series of single-question NotebookLM queries** rather than one broad prompt.
- The purpose was to accumulate enough raw evidence for synthesis while staying compliant with the NotebookLM query discipline.

### Query packets completed in Iteration 2
- **Semantic model mapping**
  - grounded how heterogeneous source systems should map into a shared semantic model
- **Metadata / ontology mechanisms**
  - grounded what semantic support structures are required
- **Governance model**
  - grounded whether governance should be centralized, delegated, or layered
- **Content-change boundary**
  - grounded what can be delegated to topic-level editing versus what must stay under semantic governance

### What Iteration 2 concluded
- The strongest supported model is a **layered / federated semantic governance pattern**.
- The system should keep:
	- a shared division-level semantic model
	- domain-authored definitions
	- committee approval for model updates
	- distributed topic-content editing within semantic guardrails

---

## Iteration 3 Summary

### Focus of Iteration 3
- Iteration 3 was scoped to **Question Set A** only:
  - what should count as the **minimum viable semantic-governance stack** for the Adaptation Division
- The unresolved publishing-risk question was intentionally held aside.

### Query packets completed in Iteration 3
- **Minimum viable stack**
  - grounded what must exist before advanced semantic formalization is attempted
- **Minimum viable artifacts**
  - grounded which concrete governance artifacts or structures must exist first

### What Iteration 3 established
- A minimum viable semantic-governance system does **not** need to start with the heaviest formal ontology implementation.
- The literature consistently points to a small set of prerequisites first:
  - a **clearly defined scope** (domain, purpose, target users, competency questions)
  - a review of **reusable existing ontologies / vocabularies** before inventing new structures
  - a **basic terminology / vocabulary list** for the most important concepts and properties
  - assigned **stewards** responsible for governing specific variables or concept areas
  - explicit **mapping tables** between local and global elements
  - explicit **source-mapping lists** connecting semantic elements to physical source structures

### Interpretation for the Adaptation Division
- This supports a **lightweight-first implementation path** for Phase 2.
- The minimum viable stack should therefore begin with:
  - division scope statement
  - domain ownership and steward assignment
  - glossary / controlled vocabulary
  - metadata minimum
  - mapping registry / crosswalk table
  - source-to-model mapping registry
  - committee approval workflow for updates
- More formal ontology-heavy structures can be deferred until the division-level semantic system is operational and stable.

---

## Locked Decisions

### 1. Governance scope
- **Decision:** Lock only an **Adaptation-Division governance model** for now.
- **Implication:** The semantic/data system scope is limited to domains under the Adaptation Division, not department-wide DCCE governance.

### 2. Content vs semantic authority boundary
- **Decision:** Topic owners may edit only the **content** of already established topics.
- **Implication:** Topic/page narrative maintenance is distributed, but semantic definitions, glossary terms, and core vocabularies are not freely editable at topic-owner level.

### 3. Pilot domain scope
- **Decision:** Use the domains already specified in the governance proposal.
- **Reference set:**
  - Physical Climate
  - Risk and Impact Assessment
  - Adaptation Planning (measures/planning)
  - Adaptation Planning (finance/policy)
  - Monitoring and Evaluation

### 4. Governance operating level
- **Decision:** In practice, sub-division / group-level owners define vocabularies and definitions first.
- **Committee role:** Division-level committee mainly approves vocabularies and definitions proposed from sub-division (`กลุ่ม`) / owner level.

### 5. Glossary strategy
- **Decision:** The glossary will eventually need to reconcile with the M&E glossary too, but that reconciliation belongs to a later project.
- **Implication:** Phase 2 can proceed with an Adaptation-Division glossary while anticipating a future crosswalk.

### 6. Canonical model strategy
- **Decision:** There should be **one single model at the Adaptation-Division level**.
- **Implication:**
  - Each domain owner may define domain-specific data models.
  - Those models must be approved by the committee before updating the system data model.
  - This model is for the Adaptation Division information and data system only, not department-wide DCCE standardization.

### 7. Procurement / TOR enforcement
- **Decision:** Do **not** rely on major TOR changes.
- **Implication:** Governance hardening should be carried through implementation detail, technical notes, and issue logs that can be raised when timing is appropriate.

### 8. Phase 2 success criterion
- **Decision:** Success means a **working frontend with full content supported by a backend data system**.

---

## Unresolved Decision

### 9. Publishing risk posture
- **Status:** Unresolved.
- **Open question:** Whether semantically ambiguous / partially verified assets may be shown with caveats, or whether only steward-reviewed assets should appear publicly.
- **Note:** This requires a recommendation before implementation policy is locked.

---

## Clarification Needed

### 10. Semantic implementation depth
- **Status:** Not yet decided.
- **Why this needs clarification:** There are at least two realistic implementation styles:

#### Option A — Lightweight operational model
- metadata minimum
- glossary
- mapping registry / crosswalk tables
- controlled tags and approval workflow
- simpler to implement inside current project constraints

#### Option B — More formal semantic model
- explicit ontology-oriented structures
- stronger machine-readable semantic relations
- more future-ready for federation and automated reasoning
- heavier to design, govern, and maintain

- **Practical interpretation:** This is not about changing the architecture direction. It is about how formally the semantic layer is implemented in Phase 2.

---

## Current Reading

At this point, the emerging stance is:
- **division-scoped governance**
- **single adaptation-division model**
- **domain-authored but committee-approved semantic changes**
- **distributed content editing within fixed topic boundaries**
- **future reconciliation with M&E, but not yet full cross-project harmonization**

This is closer to a **controlled federated model inside one division** than to either total centralization or free-for-all domain autonomy.

---

## Suggested Next Discussion Items
1. Resolve the semantic implementation depth question.
2. Recommend a publishing risk posture for unresolved / partially verified assets.
3. Convert these decisions into implementation notes for the project delivery phase.
