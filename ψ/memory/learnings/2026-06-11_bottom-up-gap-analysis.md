# Learning: Bottom-Up Gap Analysis Strategy

**Context:** Writing the technical gap analysis (Section 3.4) for the NCAIF report.

**Insight:**
A "top-down" approach (defining technical categories like HPC or API first, then forcing services to fit) leads to generic, hallucinatory writing. For example, assigning PDPA compliance to S02 when the actual audited blocker is the Granularity Gap of exposure data. 

**Rule / Standard:**
- Always use a **Bottom-Up Architecture** for gap analysis:
  1. Analyze individual services first based on audited facts.
  2. Identify specific hurdles (e.g., S06 is blocked by the Manual Coordination Trap; S05 is blocked by a missing Translation Engine).
  3. Synthesize the findings into a shared matrix at the *end*.
- **Never artificially force a challenge onto a service** just to fill out a table. Let the data audit dictate the technical dependencies.