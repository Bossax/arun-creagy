# Framework: The Anatomy of a High-Signal MVP Pitch

To prevent confusion and maximize feedback during the workshop, each MVP "Dummy" will be explained through five layers of "Concrete Reality."

---

## Layer 1: The Operational Anchor (The "When")
*   **Definition**: The specific moment in the user's work-week when this product is used.
*   **Example (MVP-2)**: "It is 48 hours after the flood receded. The Health, Agriculture, and Transport officers are all trying to fill out their respective loss reports simultaneously."

## Layer 2: The Functional Scope (The "What")
*   **MVP-1 (Policy Briefing)**: 
    *   *Stance*: Provincial-level trends + Municipality-level **Climate Allowance**.
    *   *Rationale*: High-level perils tell them "what is happening," but the Climate Allowance tells them "how much to over-build by" (the actionable engineering margin).
*   **MVP-2 (Sectoral L&D)**:
    *   *Stance*: A "Common Impact Schema."
    *   *Rationale*: Instead of just "Flood depth," the system intakes "Hectares of Rice" (Agri) and "Road Kilometers" (Transport) and translates them into a unified **Economic Loss** profile.
*   **MVP-4 (Uncertainty Shield)**:
    *   *Stance*: "Decision Confidence Labels."
    *   *Rationale*: A non-expert planner doesn't need a probability curve; they need a label like: *"Verified for Budgeting"* vs. *"Speculative: For Preliminary Discussion Only."*

## Layer 3: The Data Granularity (The "Scale")
*   **Rule**: Always specify the **Administrative Resolution**.
*   **MVP-1/2**: Must resolve at the **Municipality/LAO level** because that is where the budget is spent and the damage is felt. Provincial level is for summary only.

## Layer 4: The Step-by-Step Logic (The "How")
*   Instead of "The system calculates risk," we explain:
    1.  Intake [Hazard Layer X].
    2.  Apply [Vulnerability Factor Y].
    3.  Output [Actionable Value Z].

## Layer 5: The "Dummy" Visualization (The "Look")
*   A Mock-UI or Mock-Report that shows exactly what they get.
    *   *Example*: A 2-page PDF with a big red watermark for "Uncertainty" if the data quality is low.

---

# Proposed Research Plan (To be approved)

If you agree with this framework, I will use **NotebookLM** and **Oracle** to hunt for these specific technical details:

1.  **Extraction (NotebookLM)**: How exactly is "Climate Allowance" quantified in Norway? (Percentages? Return periods?)
2.  **Extraction (NotebookLM)**: What are the standard "Sectoral Impact Indicators" (Agri, Health, Infrastructure) used in international L&D frameworks?
3.  **Synthesis (Oracle/Local)**: Match these benchmarks against our `NCAIF_Use_Cases.md` to ensure they fit the Thai administrative context (LAO vs. Province).

**Does this framework meet your standard for a "Pitchable MVP"?**
