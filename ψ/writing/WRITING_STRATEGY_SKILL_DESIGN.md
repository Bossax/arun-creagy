# Design Doc: Human-Centric Writing Strategy Skill (v1.0)
**Context**: NCAIF Structural Data Gap Analysis & Policy Recommendations
**Objective**: Redesign the AI drafting process to eliminate "robotic neutrality" and replace it with "narrative ballistics" and "strategic persuasion."

## 1. Problem Statement: The "Robot" Trap
Standard AI drafting fails in high-stakes policy reporting because:
- **Sequentiality over Causality**: It piles up information (1, 2, 3) instead of chaining consequences.
- **Neutrality over Intent**: It informs the reader but doesn't "sell" the stance.
- **Contextual Laziness**: It uses only the immediate context, resulting in "dry" prose lacking empirical bullets.
- **Signposting Obsession**: It uses connectors like "Furthermore" and "In conclusion" which signals AI-generation and breaks the flow.

## 2. Core Pillars of the Redesign

### Pillar 1: The "Buy-In" Gate (Narrative Strategy)
Every drafting task must start with a **Victory Condition**.
- **The Stance**: What is the core argument?
- **The Fear**: What bureaucratic or legal risk are we solving for the decision-maker?
- **The Ask**: What action must the reader take?

### Pillar 2: The "Bullet Warehouse" (Evidence Foraging)
A section cannot be drafted until the "Ammunition" is gathered.
- **Forced Research**: The agent must list specific empirical "bullets" (e.g., specific regulations, audit codes, engineering return periods) before writing.
- **Trace Grounding**: Use the **`trace` skill** to find evidentiary anchors in session transcripts, project memory, and past human decisions to ensure the narrative is "forensically sound."
- **Multi-Layered Search**: Use **`brave_web_search`** and **`perplexity_search`** for external policy benchmarks and **`grep_search`** for deep-tissue internal discovery.
- **Source Grounding**: Bullets must be tethered to specific ground-truth files in `ψ/`.

### Pillar 3: Causal Connective Tissue (Narrative Ballistics)
Eliminate robotic signposting in favor of **Impact-Driven Transitions**.
- **Rule**: Every paragraph must justify the existence of the next.
- **Banned List**: "Furthermore," "In addition," "Additionally," "Lastly," "In summary."
- **Replacement**: Causal bridges (e.g., "Because of this technical failure, the subsequent financial risk becomes unavoidable...")

### Pillar 4: The Shadow Persona (Strategic Voice)
Inject a **Secondary Intent** into the writing.
- **Primary Persona**: Formal Thai Institutional Author (Surface Vocabulary).
- **Shadow Persona**: **The Strategy Consultant / Executive Protector** (Internal Intent).
- **Voice Check**: Does this sentence help the Minister defend this budget? If not, delete it.

## 3. The New Drafting Workflow

### Step 1: Strategy Phase (The "Buy-In" Memo)
- **Input**: User topic + TOR + Source files.
- **Output**: A one-page "Strategic Stance" defining the Buy-In and the "Fear" being addressed.
- **STOP**: User must approve the stance.

### Step 2: Foraging Phase (The "Bullet Warehouse")
- **Action**: Agent uses search/read tools to populate a "Warehouse of Evidence" based on the stance.
- **Output**: A list of high-fidelity facts, numbers, and causal links.
- **STOP**: User must approve the ammunition.

### Step 3: Architecture Phase (The Causal Outline)
- **Action**: Map the narrative arc as a **Chain of Consequences**, not a list of topics.
- **STOP**: User must approve the "Flow of Persuasion."

### Step 4: Drafting Phase (Shooting the Bullets)
- **Action**: Write the Thai prose using the **Shadow Persona**.
- **Constraint**: Strict adherence to the Banned Connector list. Use **Causal Bridges** only.

## 4. Measuring Success (The "Human Test")
- Does the report sound like it was written by someone who has **"skin in the game"**?
- Does the evidence feel **"heavy"** and hard to ignore?
- Is the narrative **"uninterrupted"** by AI-signposting?
