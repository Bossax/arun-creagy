# Trace/Seal Skill Behavior Capture Guide

Use this guide to capture the observable behavior of [`/trace`](../../.gemini/skills/trace/SKILL.md:9) and [`/seal`](../../.gemini/skills/seal/SKILL.md:10) in a way that avoids context contamination and makes runtime behavior auditable.

## Core rule

No parallel sub-agent is needed for this task. The scope is narrow, the skills are tightly coupled, and the main risk is contamination rather than throughput. A single isolated pass is cleaner and easier to audit.

## Procedure

1. Freeze the scope.
2. Create or reuse a sandbox.
3. Use a unique sentinel string.
4. Capture baseline state.
5. Test one skill at a time.
6. Separate artifact from motive.
7. Record contamination explicitly.
8. Use a fixed report structure.
9. Judge against contracts, not intentions.
10. End with a verdict.

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

## Verdict rule

Use one of:
- Pass
- Pass with warnings
- Fail
- Not execution-proven

For first-pass audits, “Not execution-proven” is usually the correct default.

