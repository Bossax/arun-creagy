# Plan: Phase 1 vs Pilot Comparison Audit

This plan outlines the next phase of the CRI Hardening project, focusing on reconciling the Phase 1 results with the original Pilot project.

## Summary of Accomplishments (Current Session)
- **Terminology Fix**: Global refactor from "Eco-Loss" to **"Government Advance Payment"**.
- **Analytical Alignment**: Updated scoring weights to match Pilot methodology (22.5% mortality rate, 37.5% loss/GPP).
- **Score Hardening**: Implemented final re-normalization (0.0 - 1.0) for provincial comparability.
- **Strategic Mapping**: Detailed Service 4 (Historical Impact Dossier) in the roadmap.

## Pending Tasks
- [ ] **Audit TEI Pilot Data**: Inspect `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/tei_pilot/` to understand historical semantics.
- [ ] **Compare Results**: Join current Phase 1 Gold facts with TEI Pilot results by `province_code`.
- [ ] **Pinpoint Differences**: Analyze why rankings shift (e.g., Bangkok's Director-General budget, population denominator shifts).
- [ ] **Methodology Report**: Draft a short memo explaining the "Delta" between Pilot and Phase 1.

## Cleanup
- [ ] Stage and commit terminology changes (once user confirms).
- [ ] Remove `tmp/check_sheets.py`.

## Next Session: Pick Your Path

| Option | Command | What It Does |
|--------|---------|--------------|
| **Continue** | `/recap` | Pick up the comparison analysis |
| **Clean up first** | See cleanup list above, then `/recap` | Commit terminology refactor, then continue |
| **Fresh start** | `/recap --quick` | Skip comparison, focus on Roadmap implementation |
