# Learning: The Decision Utility Matrix for Climate Services

**Date**: 2026-05-05
**Topic**: UI/UX for Decision Support Systems (DSS)
**Status**: Experimental -> Verified in Prototype

## Pattern
When presenting high-uncertainty data (like climate projections) to non-expert administrative users, a single "Confidence Rating" is insufficient. The usability of data varies across the project lifecycle.

## Implementation (The 4-Tier Guardrail)
1. **Scoping**: High tolerance for uncertainty. Focus on identifying "Where to act".
2. **Budgeting**: Requires "Safety Buffers". Focus on "How much to reserve".
3. **Zoning**: Legal/Regulatory implications. Requires high confidence/Endorsement.
4. **Design**: Technical/Safety implications. Requires high-resolution, site-specific data.

## Why it Works
By showing all 4 tiers simultaneously, the system prevents the "Misuse" of data (e.g., using a 12km grid model for a 1-meter engineering spec) while still allowing the same data to be useful for high-level strategy.

## Source
rrr: Arun_Creagy (Session: 22.15_ncaif-prototype-polish.md)
