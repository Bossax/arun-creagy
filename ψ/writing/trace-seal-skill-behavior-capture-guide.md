# Trace/Seal Skill Behavior Capture Guide

## Purpose

Use this guide to capture the observable behavior of [`/trace`](../.gemini/skills/trace/SKILL.md:9) and [`/seal`](../.gemini/skills/seal/SKILL.md:10) in a way that avoids context contamination and makes runtime behavior auditable.

## Recommendation on sub-agents

No parallel sub-agent is needed for this task. The scope is narrow, the skills are tightly coupled, and the main risk is contamination rather than throughput. A single isolated pass is cleaner and easier to audit.

## Behavior capture procedure

### 1. Freeze the scope

Record:
- skill under test
- in-scope behavior
- out-of-scope behavior
- run mode: read-only, dry-run, or live

### 2. Create or reuse a sandbox

Use a dedicated namespace such as [`ψ/lab/trace-seal-skill-test/`](../ψ/lab/trace-seal-skill-test/README.md:1).

Keep all fixture material there:
- synthetic evidence
- synthetic traces
- sandbox ledgers
- report scaffold

### 3. Use a unique sentinel

Use one sentinel string across the whole test run, for example:
- [`TEDA_TEST_ALPHA`](../ψ/lab/trace-seal-skill-test/fixtures/evidence/TEDA_TEST_ALPHA-source-note.md:1)

If that string appears outside the sandbox, treat it as contamination.

### 4. Capture baseline state

Before testing, record:
- file list
- hashes of target files
- git status if relevant
- current context already loaded

This proves whether the skill mutated anything and whether later changes are attributable.

### 5. Test one skill at a time

For [`/trace`](../.gemini/skills/trace/SKILL.md:9), capture:
- discovery behavior
- search breadth
- trace log creation
- T-E-D-A hypothesis block
- whether it avoids ledger mutation

For [`/seal`](../.gemini/skills/seal/SKILL.md:10), capture:
- intake behavior
- proposal structure
- approval gate
- append-only writes
- database bonding behavior
- rejection-path behavior

### 6. Separate artifact from motive

Check whether the skill:
- treats a file path as Evidence only
- treats the conceptual reason as Trigger
- refuses or corrects poisoned output

If a file path appears in Trigger, mark it as a defect.

### 7. Record contamination explicitly

Note every outside-sandbox read or write, including:
- unrelated project files
- prior-session bleed-through
- unexpected memory reuse

Do not hide contamination; log it as a finding.

### 8. Use a fixed report structure

1. Objective
2. Environment and isolation controls
3. Test cases
4. Observed behavior
5. Contamination findings
6. Safety findings
7. Defects
8. Verdict

### 9. Judge against contracts, not intentions

Ask for each skill:
- Did it do what the instruction says?
- Did it avoid what the instruction forbids?
- Did it fail safely on bad input?
- Did it preserve history?

### 10. End with a verdict

Use one of:
- Pass
- Pass with warnings
- Fail
- Not execution-proven

For first-pass audits, “Not execution-proven” is usually the correct default.

## Minimal capture template

- Skill under test:
- Sandbox:
- Sentinel:
- Expected behavior:
- Observed behavior:
- Side effects:
- Contamination check:
- Verdict:
- Notes:

## Practical rule

Treat every run of [`/trace`](../.gemini/skills/trace/SKILL.md:9) or [`/seal`](../.gemini/skills/seal/SKILL.md:10) as a behavioral audit:

1. isolate
2. observe
3. compare
4. document
5. verdict

