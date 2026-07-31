# Agent Context for CRI Data System

## Strict Execution Guardrails

1. **[Scope] Active Development Directory**:
   All development, code edits, script executions, and local dev servers MUST remain strictly inside `output/cri_impact_app_v3/` (or the designated active development subfolder).

2. **[Protected] Outbox / Deployment Guardrail**:
   The agent MUST NOT write to, copy files into, or execute processes inside `ψ/outbox/` (including `ψ/outbox/cri_deploy/`) unless explicitly commanded to execute a deployment action by Boss in that turn.

3. **[Governance] Data Lineage & Score Display**:
   All CRI sub-indicator metrics ($S_1 \dots S_6$) rendered in the web application MUST bind to `normalized_score` ($0.0 \dots 1.0$) when score view is requested, maintaining strict alignment with the data specification.
