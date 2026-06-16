# Pattern: Semantic Precision in Denominator Selection for Impact Indices

**Context**: Comparing historical climate risk indices across different project phases (e.g., Pilot vs Phase 1).

## The Problem
Indices often shift massively between phases even if the "formula" remains the same. Without explicitly auditing the denominators (Population, GPP), these shifts might be incorrectly attributed to changes in disaster events rather than mathematical boundary shifts.

## The Pattern
1. **Denominator Audit First**: Before analyzing rank shifts, calculate the ratio of denominators between phases.
2. **Sectoral Alignment**: Verify if GPP is "Agricultural" (Pilot/OAE) or "Total" (Phase 1/NESDC). A shift from Agricultural to Total GPP can dilute economic risk by 1000x+ in industrial provinces (e.g., Bangkok).
3. **Population Boundaries**: Discrepancies in population (e.g., >20% in border provinces) often indicate a shift in data sources (e.g., Thai-only vs Total Registered Residents).
4. **Schema Transparency**: Rename columns to reflect their specific sectoral or boundary context (e.g., `gpp_agri_pilot` vs `gpp_total_p1`) rather than generic names like `gpp`.

## Impacts
- Prevents misdiagnosis of provincial "improvement" or "worsening" when the change is purely denominator-driven.
- Provides a clear mathematical bridge for stakeholders to understand why urban centers suddenly rank lower/higher in risk.

**Concepts**: [cri, gpp, normalization, methodology, automation]
**Project**: Arun_Creagy
