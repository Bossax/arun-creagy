---
from: local:arun
to: creagy-writing
team: knowledge-structure-learning
timestamp: 2026-10-07T12:54:30.000Z
subject: "Knowledge Storage Architecture Proposal: High-Signal Memory via Files & Vector Database"
status: dispatched
target_file: "C:/Users/sitth/OracleWorkspace/creagy-writing/ψ/inbox/2026-10-07_knowledge-structure-proposal-from-arun.md"
---

# Knowledge Architecture Proposal for creagy-writing

**Prepared by**: Arun (Central Orchestrator)  
**Contributors**: Keth (Public Administration Specialist), Jiu (Climate Risk & Resilience Specialist)  
**Target Entity**: `creagy-writing` Oracle & Team  
**Date**: 7 October 2026  

---

## 1. Executive Summary

Following a comparative audit of knowledge management patterns in `Keth-goverment-agent` and `Jiu-climate-risk-and-resilience`, this document outlines the recommended architecture for storing long-term, domain-specific, high-signal writing knowledge in `creagy-writing`.

The core principle established across the fleet is **"Right-Sizing Knowledge Storage: Match storage format to entity scale and query pattern."** 

To avoid vault clutter while enabling both deterministic verification and nuanced stylistic emulation, `creagy-writing` should implement a **Tri-Layer Knowledge Model**:
1. **Modular Markdown (`ψ/memory/`)**: High-level rules, tone/register rubrics, and editorial principles (< 100 conceptual notes).
2. **Relational / Tabular Store (`src/data/lexicon.sqlite`)**: Mass uniform terminology, forbidden expressions, and regex lint pairs (> 1,000 entries).
3. **Oracle Vector Database (`bge-m3` Embeddings)**: Golden reference paragraphs, before/after editing diffs, and rhetorical cadence exemplars.

---

## 2. Comparative Analysis: Keth vs. Jiu

### 2.1 Keth's Pattern (Public Administration & Statutory Mandates)
* **The Rule of Scale**: Formally codified in `ψ/memory/learnings/2026-09-21_right-sizing-knowledge-storage-architecture.md`.
  * **Relational Store (`bureaucrazy.sqlite`)**: Retains 417 line agencies, 2,432 statutory duty clauses, and ministerial decrees. Kept out of raw Markdown to avoid polluting the search space.
  * **Modular Markdown (`ψ/memory/knowledge/`)**: Structures conceptual frameworks (< 50 items like M&E cycles and ADLI rubrics) with YAML frontmatter and Mermaid diagrams for human inspection in Obsidian.
* **Key Takeaway for Writing**: Do not store thousands of vocabulary definitions in individual Markdown notes. Use a structured database for mass terminology.

### 2.2 Jiu's Pattern (Climate Risk, Models & Multi-Source Evidence)
* **The 5-Stage Curated Pipeline (`ψ/active/incoming_cri_curation/`)**:
  * Raw benchmark papers (`01_literature`) $\rightarrow$ Micro-query lab extractions (`02_lab`) $\rightarrow$ Canonical packages (`03_canonical`) $\rightarrow$ Operational rules (`04_heuristics`) $\rightarrow$ Production data (`05_data`).
* **Forensic Traces & Distilled Learnings**:
  * Ephemeral scraped responses are quarantined to `ψ/active/` and `.oracle-data/`.
  * Only verified principles and atomic patterns enter `ψ/memory/learnings/`.
* **Key Takeaway for Writing**: Separate raw drafting iterations / model reviews from permanent editorial guidelines. Never allow temporary project scratch notes to contaminate permanent style packs.

---

## 3. Proposed Tri-Layer Architecture for creagy-writing

```
                       ┌──────────────────────────────────────────────┐
                       │           creagy-writing Knowledge           │
                       └──────────────────────┬───────────────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
┌──────────────────────────────┐ ┌──────────────────────────────┐ ┌──────────────────────────────┐
│  Layer 1: Modular Markdown   │ │ Layer 2: Deterministic Store │ │   Layer 3: Oracle Vector DB  │
│        (ψ/memory/)           │ │  (src/data/lexicon.sqlite)   │ │      (bge-m3 Embeddings)     │
├──────────────────────────────┤ ├──────────────────────────────┤ ├──────────────────────────────┤
│ • High-level style manuals   │ │ • Approved Thai terminology  │ │ • Golden exemplar paragraphs │
│ • Tone & register guidelines │ │ • Forbidden jargon pairs     │ │ • Draft-to-Edit before/after │
│ • Thai institutional rules   │ │ • Agency abbreviation tables │ │ • Rhetorical cadence search  │
│ • Inspection gates           │ │ • Fast regex/SQL linting     │ │ • Semantic style similarity  │
└──────────────────────────────┘ └──────────────────────────────┘ └──────────────────────────────┘
```

### Layer 1: Modular Markdown (`ψ/memory/`) — Editorial Rules & Frameworks
* **Content**: Editorial standards, stylistic rules, quality gates, and register expectations (e.g., Thai official memo, executive briefing, technical chapter).
* **Format**: Human-readable Markdown with standardized YAML frontmatter:
  ```markdown
  ---
  id: rule-bureaucratic-tone-th
  title: "หลักการร่างรายงานเชิงสถาบันและภาษาทางการ"
  type: writing-rule
  applies_to: [policy-brief, executive-summary]
  enforcement: deterministic
  tags: [thai-writer, register, institutional]
  ---
  ```
* **Storage Location**:
  * `ψ/memory/style/` — Style manuals and tone specifications.
  * `ψ/memory/gates/` — Deterministic checklists and delivery pass/fail criteria.
  * `ψ/memory/learnings/` — Lessons learned from past editor feedback.

### Layer 2: Relational Lexicon Store (`src/data/lexicon.sqlite`) — Uniform Vocabulary
* **Content**: Terminology pairs, official ministry translations, forbidden filler words, and acronym mappings.
* **Schema**:
  ```sql
  CREATE TABLE approved_terms (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      term_en TEXT,
      term_th TEXT NOT NULL,
      domain TEXT, -- climate, finance, governance
      context_note TEXT
  );

  CREATE TABLE forbidden_expressions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      bad_phrase_th TEXT NOT NULL,
      replacement_th TEXT,
      reason TEXT,
      severity TEXT -- error, warning
  );
  ```
* **Function**: Powers high-speed pre-delivery regex lint checks before presenting documents to Boss.

### Layer 3: Oracle Vector Database (`bge-m3` Embeddings) — Exemplar Memory
* **Content**: Golden reference paragraphs, polished drafts, and draft-versus-revision delta pairs.
* **Chunking Standard**:
  * **Granularity**: Logical paragraphs (150–300 tokens) rather than arbitrary sentence splits.
  * **Metadata Schema**:
    ```json
    {
      "source": "CRDB-2.3-Chapter6",
      "author": "Boss",
      "genre": "institutional-report",
      "register": "official-thai",
      "section_type": "problem-statement",
      "quality_tier": "gold"
    }
    ```
* **Operational Flow**:
  1. Teammate or Conductor requests a draft on a specific topic.
  2. Agent calls `oracle_search` on the vector database for semantically similar gold paragraphs.
  3. The agent conditions its prompt on the retrieved exemplars to mirror sentence cadence, transition words, and paragraph balance.

---

## 4. Implementation Steps for creagy-writing

1. **Initialize File Structure**:
   - Establish `ψ/memory/style/` and `ψ/memory/gates/` within `creagy-writing`.
2. **Seed Deterministic Lexicon**:
   - Compile initial Thai environmental and governance terms into `src/data/lexicon.sqlite`.
3. **Ingest Gold Paragraphs to Vector DB**:
   - Ingest approved writing exemplars into the `creagy-writing` Oracle embedding service (`bge-m3`).
4. **Wire Pre-Delivery Gate**:
   - Ensure the writing pipeline checks against Layer 2 (deterministic lint) and Layer 1 (editorial gates) before declaring a draft ready.
