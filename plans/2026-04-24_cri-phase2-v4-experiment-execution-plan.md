# CRI Phase 2 v4 Linkage Experiments - Execution Plan

## 1. Objective

Design and run a controlled three-experiment program to refine the asset-to-governance activation linkage logic for [`CRI_Capacity_Tagging_Dictionary_v4.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v4.md), while preserving the kernel structure of [`CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md:18).

The goal is not to generate one immediate final taxonomy. The goal is to produce three auditable linkage variants, compare them on a common benchmark, and then choose or hybridize the strongest design.

## 2. Design principles

1. **Reuse first**  
   Existing v3 concepts are always tested before concept expansion.

2. **Loose but functional linkage**  
   Linkages must identify the specific governance job and primary bottleneck without collapsing into a massive process audit.

3. **Controlled expansion only**  
   A new governance concept may be added only when no existing concept, interpretation note, or combination of existing concepts can carry the activation burden.

4. **Evidence before survival**  
   Any new concept that survives a round must be grounded by external evidence plus an internal rationale note.

5. **Comparison before freeze**  
   The final v4 structure is selected only after cross-experiment comparison.

## 3. Fixed benchmark inputs

All three experiments must use the same benchmark base.

### 3.1 Fixed kernel
- [`CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md:32)
- [`CRI_Phase2_Methodology_Synthesis_Report.md`](ψ/incubate/DCCE/CRI/output/CRI_Phase2_Methodology_Synthesis_Report.md:20)
- [`CRI-Phase2-Synthesis-Journey-and-Decision-Audit.md`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI-Phase2-Synthesis-Journey-and-Decision-Audit.md:33)

### 3.2 Fixed asset-concept universe
The experiments must cover the full 11 hardened asset concepts from [`CRI_Asset_Concept_Summary_v1.md`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:11).

Canonical concept set:
- [`HC-01`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:22) Urban green ecological cooling stock
- [`HC-02`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:23) Urban stormwater and flood-routing stock system gray plus nature-based
- [`HC-03`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:24) Coastal protection and accommodation built stock
- [`HC-04`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:25) Coastal socio-ecological buffer and EbA stock
- [`HC-05`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:26) Urban ecological form-function stock biodiversity plus ventilation corridors
- [`HC-06`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:27) Built-form thermal safety and inclusive public-realm stock
- [`HC-07`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:28) Infrastructure resilience architecture stock robustness redundancy flexibility
- [`HC-08`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:29) Energy utility mobility and communication enabling networks
- [`HC-09`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:30) Food-system and productive bio-resource stock
- [`HC-10`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:31) Financial and economic resilience buffer stock system
- [`HC-11`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/CRI_Asset_Concept_Summary_v1.md:32) Human and social capability stock skills literacy connectedness collective assets

These 11 concepts are the justification target for the methodology. The experiment program is no longer framed as a narrow pilot; it is framed as a controlled full-coverage refinement process.

### 3.3 Fixed scoring rubric
Each final variant must be scored against the same dimensions:
- Concept growth
- Coverage across pilot assets
- Bottleneck clarity
- Category purity
- Evidence strength
- Cross-asset reusability
- Administrative readability

## 4. Shared round structure

Each experiment runs **3 rounds**.

### Round 1 - Reuse-first mapping
For each of the 11 hardened asset concepts:
- define asset stock
- define expected function
- define stress context
- attempt linkage using only existing v3 concepts
- allow interpretation-note clarification
- log unresolved failure points

### Round 2 - Controlled refinement
For each unresolved failure point:
- test whether combining existing concepts resolves it
- if not, consider a new concept under that experiment's control parameters
- attach evidence and rationale immediately
- revise the activation chain

### Round 3 - Prune and stabilize
- remove weak or redundant additions
- merge duplicative additions back into existing concepts where possible
- verify category purity
- verify one primary bottleneck per asset chain
- lock one final linkage variant for that experiment

## 5. Reuse-first decision ladder

Every unresolved linkage must pass through this ladder in order:

1. Reuse existing v3 concept as-is
2. Reuse existing v3 concept with interpretation note
3. Combine two or more existing v3 concepts into one activation chain
4. Add a new concept provisionally
5. Keep the new concept only if it survives evidence and pruning review

## 6. Experiment families

### Experiment A - Strict kernel preservation
Purpose: test how far the v3 kernel can go with minimal expansion.

Control parameters:
- max new concepts per round: 1
- semantic relaxation: low
- evidence bar: high
- pruning aggressiveness: high
- expected risk: underfitting true missing concepts

### Experiment B - Balanced diagnostic growth
Purpose: allow limited expansion while preserving kernel integrity.

Control parameters:
- max new concepts per round: 2
- semantic relaxation: medium
- evidence bar: medium-high
- pruning aggressiveness: medium
- expected role: likely default candidate

### Experiment C - Exploratory stress test
Purpose: identify hidden missing concepts and test the outer boundary of taxonomy need.

Control parameters:
- max new concepts per round: 4
- semantic relaxation: medium
- evidence bar: medium
- pruning aggressiveness: very high in round 3
- expected risk: concept inflation if not pruned tightly

## 7. Control parameter definitions

### 7.1 Max new concepts per round
Upper bound on the number of truly new governance concepts admitted provisionally during one round.

### 7.2 Semantic relaxation
How far an existing concept may be stretched before it is judged inadequate.

- Low: reuse only if function is closely aligned
- Medium: reuse allowed with interpretation note
- High: not recommended for this workflow

### 7.3 Evidence bar

- High: at least 2 grounded external sources plus 1 internal rationale note
- Medium-high: at least 1 strong external source plus 1 internal rationale note, with clear statement of insufficiency of existing concepts
- Medium: at least 1 grounded external source plus 1 internal rationale note

### 7.4 Pruning aggressiveness
How strongly round 3 removes weak, duplicate, or single-use concepts.

## 8. Recording template for each asset-chain evaluation

Every asset in every round should be documented with these fields:

- Asset name
- Asset function
- Stress context
- Selected governance blocks
- Causal order
- Primary bottleneck
- Failure signature
- Reuse status
- New concept requested Y or N
- Evidence basis
- Reviewer note

## 9. Evidence-gathering protocol for the agent

The agent must gather evidence in an external-first order so concept additions and linkages are grounded in literature and source retrieval rather than inferred from project-internal notes.

### 9.1 External evidence comes first
For every asset concept and every proposed governance linkage, the agent must begin with external source gathering.

Primary evidence channels for this workflow:
Start from 1. if additional information is needed, continue down the list
1. [`brave_web_search`](mcp--brave-search--brave_web_search:1)
2. [`mcp--notebooklm--ask_question`](mcp--notebooklm--ask_question:1) across both CRI notebooks
3. [`perplexity_ask`](mcp--perplexity--perplexity_ask:1)
4. [`perplexity_search`](mcp--perplexity--perplexity_search:1)

The purpose of this stage is to establish:
- the expected function of each asset stock under stress
- the governance conditions that literature or notebook sources describe as necessary for activation
- the plausible bottlenecks linking asset failure and process failure
- whether an apparent concept gap is truly new or already covered by an existing governance concept

### 9.2 External evidence extraction questions
For each linkage attempt, the agent must answer:
- What service or resilience function does this asset stock enable?
- What governance process or institutional condition activates that stock into realized function?
- What failure mode appears when the asset exists but the process is weak?
- Is the candidate linkage already representable with the current governance concept set?

### 9.3 Internal materials are for alignment, not evidence generation
Project-internal artifacts may be used only after external evidence is gathered, and only for these limited purposes:
- aligning terminology with existing CRI naming conventions
- recording local rationale notes
- checking whether a proposed linkage or concept has already been drafted internally

Internal project files must not be treated as the primary evidentiary basis for deciding that a linkage or new governance concept is valid.

### 9.4 External evidence workflow

Permitted external evidence workflow:
1. Search narrowly for the specific unresolved activation problem
2. Prefer empirical, framework, or review sources over generic commentary
3. Extract only the minimal claim needed to justify the concept or linkage
4. Record the claim in a rationale note before using it in v4

The agent should use these tools in that order of preference depending on the unresolved need:
- use [`brave_web_search`](mcp--brave-search--brave_web_search:1) to find candidate source surfaces quickly
- use [`mcp--notebooklm--ask_question`](mcp--notebooklm--ask_question:1) for source-grounded extraction from the CRI notebook corpus
- use [`perplexity_ask`](mcp--perplexity--perplexity_ask:1) for concise grounded explanation or synthesis checks
- use [`perplexity_search`](mcp--perplexity--perplexity_search:1) when specific URLs, papers, or recent source discovery are needed
  
The tool list is in priority order. If the condition is satisfied already, you do not need to use all tools. 

### 9.5 Minimum evidence package for any new concept
A new concept may survive only if the agent records:
- one explicit statement of why existing v3 concepts are insufficient
- one local rationale note documenting the logic of admission
- one grounded external source at minimum
- the affected asset concepts that require this addition

When the new concept depends primarily on literature interpretation rather than project-internal reconstruction, the preferred evidence package is:
- one local rationale note
- one notebook-grounded extraction from a CRI notebook
- one corroborating external web-grounded source from [`brave_web_search`](mcp--brave-search--brave_web_search:1), [`perplexity_ask`](mcp--perplexity--perplexity_ask:1), or [`perplexity_search`](mcp--perplexity--perplexity_search:1)

### 9.6 Evidence logging rule
Every addition, reinterpretation, or concept-combination decision must be written into the experimental output folder as:
- source used
- claim extracted
- reason for reuse or addition
- affected asset concepts
- status after pruning review

### 9.7 NotebookLM guardrail requirements
Before any use of [`mcp--notebooklm--ask_question`](mcp--notebooklm--ask_question:1), the agent must apply the [`notebooklm-rules`](.roo/skills/notebooklm-rules/SKILL.md) guardrail.

Mandatory NotebookLM preflight:
1. Read and apply the rules in [`notebooklm-rules`](.roo/skills/notebooklm-rules/SKILL.md)
2. Use explicit notebook selection rather than relying on an active default
3. Treat NotebookLM as extraction-only, with harmonisation performed locally afterward
4. Save raw outputs verbatim before local reshaping
5. Use browser settings with:
   - `headless: false`
   - broswer_timeout: 360000`
   that's it. dont need to put other parameters

For this CRI workflow, the agent should consult both CRI notebooks when needed and record for each run:
- notebook used
- session id
- extraction objective
- exact prompt packet
- raw output file path

## 10. Comparison logic after all experiments

After the three experiments finish, prepare a comparison memo with:

1. Final concept inventory delta versus v3
2. Coverage summary across all 11 hardened asset concepts
3. List of surviving new concepts and why they survived
4. Bottleneck clarity comparison
5. Category-purity issues by experiment
6. Evidence-strength comparison
7. Recommendation:
   - choose Experiment A, B, or C
   - or produce a hybrid variant with explicit rationale

## 11. Convergence and stopping rules

Within each experiment, a round is considered converged when:
- no additional concept survives the evidence review, or
- all remaining gaps can be addressed by interpretation notes or concept combinations only

An experiment is considered stable after round 3 when:
- every hardened asset concept has a readable activation chain
- every chain has one primary bottleneck
- no category-purity violations remain unresolved
- no surviving new concept is weakly evidenced

The cross-experiment program is ready for final selection when:
- all 3 experiments have final round outputs
- the same scoring rubric has been applied to all 3 final variants
- a compromise or preferred model can be justified from evidence rather than preference

## 12. Proposed output folder structure

Experimental outputs should be stored under:

- [`ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/)
- [`experiment_A/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/experiment_A)
- [`experiment_B/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/experiment_B)
- [`experiment_C/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/experiment_C)
- [`comparison/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/comparison)

Recommended artifact types:
- round logs
- asset-chain worksheets
- concept-addition register
- pruning decisions
- final experiment summary
- final comparison memo

## 13. Implementation sequence

1. Create the experimental output folder scaffold
2. Initialize the expected run artifacts before execution, including per-experiment round logs, asset-chain worksheets, concept-addition registers, pruning decision logs, and final summary placeholders under [`experimental_runs/`](ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/README.md)
3. Draft [`CRI_Capacity_Tagging_Dictionary_v4.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v4.md) by mirroring v3 structure
4. Add the linkage-rule layer without altering the six-pillar kernel
5. Prepare the full 11-concept working matrix and scoring rubric
6. Run Experiment A through rounds 1 to 3
7. Run Experiment B through rounds 1 to 3
8. Run Experiment C through rounds 1 to 3
9. Produce the comparison memo
10. Select or hybridize the preferred v4 design

## 14. Mode recommendation for execution

Best execution mode: [`orchestrator`](orchestrator:1)

Reason:
- the work is multi-stage
- it involves repeated comparative runs
- it benefits from controlled sequencing across experiments, rounds, and output artifacts

Secondary mode: [`code`](code:1)

Use [`code`](code:1) if the task is narrowed to directly drafting [`CRI_Capacity_Tagging_Dictionary_v4.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v4.md) and writing the experiment artifacts after the workflow is already fixed.

## 15. Approval gate

Do not execute the experiment program until the human approves:
- the experiment families
- the control parameters
- the pilot asset basket
- the output structure
- the execution mode
