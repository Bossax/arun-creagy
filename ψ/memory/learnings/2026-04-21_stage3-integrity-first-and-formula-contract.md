# Learning: Stage 3 Integrity-First Execution and Formula Contract Requirement

## Context
During CRI Phase 1 Stage 3 implementation, the pipeline reached high delivery completeness across baseline audit, crosswalks, policy constraints, denominator/numerator generation, redistribution, multi-level outputs, and final integrity checks.

## What happened
- A corrupted raster source caused repeated spatial read failures and blocked downstream denominator reliability.
- Bangkok handling required policy-first controls because lower-level join certainty was not equivalent across sources.
- Even after technical completion, stakeholders still lacked an explicit mathematical contract for numerator/denominator and rate equations.

## Durable lesson
In governance-grade spatial risk pipelines, implementation must prioritize integrity over throughput, and mathematical definitions must be published as a first-class contract.

## Pattern to reuse
1. Fail closed when canonical linkage is uncertain.
2. Preserve unresolved blockers explicitly in validation artifacts.
3. Treat row-level evidence as higher precedence than narrative summaries.
4. Publish a compact formula contract (numerator, denominator, scaling factor, exclusions) for each analysis level.

## Application
For future CRI stages, pair every module milestone with:
- a machine-readable validation artifact,
- a human-readable constraint summary,
- and a mathematical-definition section to prevent interpretation drift.

