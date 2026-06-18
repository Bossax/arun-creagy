# Retrospective: Turning a High-Level Build Plan into an Executable Contract

## Session Summary

This session started with a seemingly simple request to prepare a next-step plan for a web app build. The work quickly revealed that a roadmap was not enough: the plan needed to become an execution contract with explicit source-of-truth references, frozen data shapes, read-only frontend boundaries, and design guidance that a builder could follow without inventing missing logic.

The main outcome was a progression from broad planning into a tighter, more operational build package:

- analytical rules were frozen
- methodology and wording were frozen
- a schema freeze was added to remove ambiguity from exported assets
- the orchestration plan was tightened into stage-by-stage build instructions
- a canonical design template was created for the app
- a next-session build handoff was prepared

## What Changed My Assessment of the Problem

### 1. The working notebook was the real source of truth

The first major turnaround was realizing that the plan must be grounded in the working implementation example rather than in planning prose. A plan that only names outcomes is too abstract for an autonomous builder. The notebook exposed the real formulas, grouping logic, and rendering assumptions that needed to be preserved.

### 2. Analytical decisions needed to be frozen before implementation could be safe

The affected-rate denominator decision, the two time-mode requirement, and the heat-map split were not just documentation details. They were implementation constraints. Once those were frozen, it became clear that the build could not proceed safely until the plan reflected them directly and consistently.

### 3. The exported data contract was the highest-risk gap

The biggest execution risk was not the UI or the deployment path; it was the shape of the data exchanged between stages. Without exact JSON structures, an autonomous agent could easily invent incompatible payloads or drift away from the notebook behavior. Adding a schema-freeze artifact closed that gap.

### 4. Frontend stages had to be explicitly read-only

Another important correction was realizing that the visualization stages must not recalculate analytics. They should consume frozen exports and spatial assets only. That distinction is critical for preventing silent logic drift in the frontend layer.

### 5. Design needed to be treated as an execution dependency, not an aesthetic afterthought

The build plan became materially better once the app-specific design template was introduced and tied back to the upstream warm, rounded design system. This removed ambiguity about visual tone, spacing, components, and typography.

### 6. Deployment had to be separated from local build readiness

The plan initially blurred local hardening with deployment. That was too coarse. The corrected sequence now treats local testing as a prerequisite checkpoint and deployment as a separate, later action that only happens when explicitly requested.

## Process Lessons

### Lesson 1: Start with the read model, not the roadmap

An execution plan should first define what inputs a builder is allowed to read and what outputs it must produce. Only after that should it define the stage ordering. In this session, the plan became stronger only after the source CSVs, working notebook, schema contract, and design template were named explicitly.

### Lesson 2: Every stage needs a source boundary

Each build stage should answer three questions:

1. What source logic does it follow?
2. What is it forbidden to recompute?
3. What exact files or UI outputs does it produce?

Without those boundaries, an agent tends to fill gaps with plausible but ungrounded behavior.

### Lesson 3: Separate analytics from rendering

The cleanest architecture in this session was to freeze analytics in one stage and make later stages read-only consumers. That separation reduces hidden coupling and makes debugging much easier.

### Lesson 4: A plan is not executable until it states completion criteria

A useful build plan must specify when a task is done in a way that a reviewer can verify. Qualitative terms such as “stable,” “clean,” or “client-ready” are too vague on their own. They need concrete checks, file outputs, or rendering conditions.

### Lesson 5: Design should be canonical early

The UI work became much more coherent once the app-specific design template was created. A canonical design file gives the builder a shared vocabulary for color, spacing, card patterns, and typography while still allowing iteration.

## What Worked Well

- The work moved from abstract planning into concrete contract-setting.
- The notebook remained the implementation anchor instead of being replaced by invented summaries.
- Important analytical choices were frozen before code generation could begin.
- The data contract was made explicit enough to reduce hallucination risk.
- The design system was documented as a starter template rather than a rigid final lock.
- A handoff path was created for the next build session.

## What Did Not Work Well

- The first iteration of the orchestration plan was too high-level.
- File-level and schema-level specificity came later than it should have.
- The plan needed stronger language about read-only frontend stages earlier.
- Deployment had to be separated from local build readiness only after the ambiguity was noticed.
- Some of the plan refinement had to be driven by repeated critique, which shows the initial contract was not yet tight enough.

## How to Do This Better Next Time

### 1. Freeze the contract before writing the roadmap

For a build like this, the order should be:

1. identify the working source logic
2. freeze the analytical decisions
3. freeze the export schema
4. freeze the design template
5. write the orchestration sequence
6. write the next-session handoff

### 2. Use explicit stage contracts

Each stage should include:

- source of truth
- logic to preserve
- output files or UI artifacts
- validation checks
- completion condition

### 3. Treat the frontend as a consumer, not a second analytics engine

Visualization stages should be read-only wherever possible. If a frontend stage starts recomputing metrics, the architecture is already leaking.

### 4. Make design implementation-grade, not inspirational

A design template should not only describe mood and color; it should also define starter tokens, component behavior, and layout rules that a builder can apply immediately.

### 5. Separate local readiness from deployment

Local verification should be a distinct checkpoint before any deployment consideration. That avoids conflating “works on my machine” with “ready to publish.”

## Generalizable Heuristics

1. If a builder could reasonably invent two different implementations, the plan is not specific enough.
2. If a visualization stage can recalculate the same numbers as the analytics stage, the contract is too loose.
3. If a design system is not named as a dependency, implementation will drift.
4. If deployment is included too early, local verification tends to be skipped.
5. If the handoff cannot be understood without project memory, it is not yet a proper handoff.

## Final Reflection

The key lesson from this session is that planning for an autonomous build is not the same as describing a desired product. The plan must become a chain of enforceable contracts: analytical, structural, visual, and operational. The more explicit the read model and output model become, the less room there is for hallucination, and the more confidently a future builder can proceed.
