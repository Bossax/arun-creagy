---
id: learning_2026-07-01_style-pack-compliance-workflow-running-drafts-t
type: learning
title: # Style Pack Compliance Workflow: Running Drafts through Style Rules
concepts: [style-pack, workflow, compliance, translation]
tags: [style-pack, workflow, compliance, translation]
created: 2026-07-01
indexed_at: 2026-07-01T09:05:50.506Z
updated_at: 2026-07-01T09:05:50.506Z
hash: sha256:5c2e48818b914bda2284ee763019395e829e6b857b25a7bb83eb773ffc4597ca
source: Oracle Learn
project: bossax/arun_creagy
arra_id: learning_2026-07-01_style-pack-compliance-workflow-running-drafts-t
arra_type: learning
arra_concepts: [style-pack, workflow, compliance, translation]
arra_created: 2026-07-01T09:05:50.506Z
---

# # Style Pack Compliance Workflow: Running Drafts through Style Rules

# Style Pack Compliance Workflow: Running Drafts through Style Rules

This document outlines the systematic process developed to ensure that draft report prose strictly complies with custom style packs (specifically the `NCAIF-Institutional` guidelines).

## 1. The Compliance Process (Steps)

1. **Rule & Draft Alignment Audit**: View the style pack and draft files side-by-side. Understand the specific lexical bans, preferred terms, and structural rules (e.g., banishing English jargon, replacing DCCE with กรมฯ, using active Thai sentence shapes).
2. **Lexicon Extraction & Mapping**: Compile a comprehensive dictionary of target replacements based on style rules. This translates direct English jargon (like `use case` or `interoperability`) and acronyms into their approved Thai equivalents.
3. **Exhaustive Bulk Replacement (Automated Scripting)**: Run a script (e.g., PowerShell regex) to perform global, case-insensitive string replacements on the draft. This acts as a net to catch 100% of banned abbreviations and terms.
4. **Contextual Cleanup & Spacing Polish**: Perform manual edits to fix styling artifacts introduced by the automated replacement (e.g., cleaning up extra spacing around Thai characters, stripping duplicate parentheses like `(มาตรฐานข้อมูลกำกับ Standard)`, and fixing sentence flow).
5. **Quality Control Check**: Run a regex check for remaining English alphabetical characters (`[a-zA-Z]+`) to verify that no banned jargon slipped through.

## 2. Rationale: Why This Workflow?

* **Eliminating Recency Bias / AI Forgetfulness**: When merging new content pieces or writing extensive sections, LLMs often default to generic technical templates (reintroducing terms like `DCCE`, `CRDB`, `API`, or `use case`). An automated batch-replacement step acts as a safety gate.
* **Preserving Technical Precision vs. Institutional Registers**: Automated search-and-replace handles vocabulary perfectly, but it ruins grammar and rhythm. Step 4 (Manual Polish) ensures the report does not read like a mechanical word-for-word translation, maintaining the natural, authoritative Thai institutional voice.

## 3. Tools Utilized

* **`view_file`**: For reading the exact style pack parameters (`STYLE_PACK_NCAIF-Institutional.md`) and draft versions.
* **PowerShell (`run_command`)**: For running case-insensitive regex batch replacements to guarantee lexical compliance.
* **`multi_replace_file_content`**: For targeted manual edits, restoring sentence flow, and correcting spacing issues.

## 4. Assessment of Results

The result is highly successful. The workflow effectively converts drafts that feel like "AI-translated software specifications" into documents with a native Thai policy register. By using a hybrid approach—automated scripting for absolute coverage and manual polish for readability—we achieve both 100% lexical compliance and superior prose quality.

---
*Added via Oracle Learn*
