# Trace/Seal Skill Test Sandbox

This sandbox contains isolated fixtures and a report scaffold for testing the local `/trace` and `/seal` skills without touching active CRI/CRDB ledgers.

## Isolation rule

All fixture evidence uses the sentinel `TEDA_TEST_ALPHA`. Any test result that consumes files outside this directory must be recorded as a contamination finding in `test-report.md`.

## Contents

- `fixtures/evidence/` — synthetic evidence artifacts.
- `fixtures/ledgers/` — append-only sandbox ledgers.
- `fixtures/traces/` — synthetic trace logs for seal intake simulation.
- `test-report.md` — tester-facing report scaffold.

