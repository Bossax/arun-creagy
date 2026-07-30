# Stage 1 research plan — Climate projection roll-ups

## Objective

Build a defensible content foundation for the two-roll-up series before creating any visual layout or HTML prototype.

Research will focus on:

- Climate projection data
- Scenarios and uncertainty
- Uses of projection data
- Statistical versus dynamical downscaling
- Why multiple models and scenarios are necessary
- The four products: GridData, WRF-Chem, RegCM5, and Statistical Downscaling

## Research tools and source hierarchy

Use the following research flow:

`Brave discovery → native web search → Perplexity synthesis → official-source verification → evidence map → content plan`

- Brave Search MCP for broad discovery and current platform pages.
- Native web search when Brave results are incomplete, outdated, or noisy.
- Perplexity MCP for focused synthesis and follow-up research questions.
- Official IPCC, CORDEX/WCRP, DCCE, and Thailand Climate Projection Platform sources as final evidence authority.
- Local file inspection and image viewing for the supplied designs, reference image, and project artifacts.
- Direct platform inspection for product names and metadata.

Search and synthesis tools are discovery aids; they are not evidence by themselves.

## Evidence work

- Use the supplied five images as claim leads, not final evidence.
- Verify definitions of projection, scenario, forecast, and uncertainty.
- Verify why climate projections use multiple models and scenarios.
- Verify the distinction between statistical and dynamical downscaling.
- Inspect official platform documentation or pages for each product:
  - official name and spelling
  - method or model type
  - spatial resolution
  - temporal coverage
  - variables
  - scenarios
  - model count or model source
  - intended analytical use
- Confirm whether the official product label is exactly `RegCM5`.
- Mark unavailable or contradictory metadata as unresolved; do not infer values from the supplied graphics.

## Roll-up 1 — Climate projection data

### Primary reader question

What is climate projection data, why does it matter, and how can it support decisions?

### Required sequence

1. Define climate projection data as model-derived estimates of possible future climate conditions.
2. Explain why it matters for Thailand and climate-risk decisions.
3. Explain that scenarios describe alternative plausible futures and are not weather forecasts or guarantees.
4. Compare scenario labels only after verification.
5. Show practical uses: risk assessment, adaptation planning, infrastructure, land use, agriculture, water, disaster preparedness, and policy or investment decisions.
6. State that interpretation depends on model, scenario, period, variable, and spatial scale.

### Required Insight Card

- Reader question
- Source-specific finding
- Mechanism
- Consequence
- Visual proof
- Evidence anchor

## Roll-up 2 — Downscaling and the four products

### Primary reader question

How does broad climate projection information become more locally useful, and why are multiple products, models, and scenarios needed?

### Required sequence

1. Explain the spatial-scale problem: global models cannot represent every local terrain and climate feature at decision scale.
2. Explain statistical downscaling using verified DCCE terminology.
3. Explain dynamical downscaling as regional modelling of atmospheric processes driven by broader model information.
4. Explain why multiple models and scenarios represent a range of plausible futures rather than one certain future.
5. Introduce the four products:
   - GridData
   - WRF-Chem
   - RegCM5
   - Statistical Downscaling
6. Compare products using verified differences in method, scale, variables, period, and use.

### Required Insight Card

- Reader question
- Source-specific finding
- Mechanism
- Consequence
- Visual proof
- Evidence anchor

## Stage 1 artifacts

Create or update only these content artifacts:

- `content_plan.md` — message hierarchy, Thai-first draft copy, text limits, caveats, prohibited wording, and one Insight Card per roll-up.
- `evidence_map.md` — claim-by-claim source mapping, confidence/status, exact source location, permitted visual treatment, and claims that must not be visualized.
- `series_map.md` — replace the old platform request-path framing with the revised two-rollup narrative.
- `source_inventory.md` — add newly verified sources or product documentation only where needed.

Do not create the HTML prototype, generation handoff, or final layout during Stage 1.

## Acceptance criteria

Stage 1 passes only when:

- Both roll-ups have a clear primary thesis.
- Each roll-up has a complete six-field Insight Card.
- Every quantitative, methodological, scenario, and product claim has an evidence anchor.
- Projection, scenario, forecast, and observation are distinguished accurately.
- Multiple models and scenarios are explained without implying equal probability or certainty.
- The four product names are verified or explicitly marked unresolved.
- Draft copy is concise enough for a vertical roll-up.
- Generic claims and unsupported numbers are removed.
- The evidence map identifies what becomes a comparison, sequence, map/grid, illustrated metaphor, editable text, or prohibited visual content.

Only after these checks pass will Stage 2 begin with an HTML layout prototype.

## Defaults

- Thai-first display language; retain English technical names where useful.
- Audience: public-sector planners, researchers, and climate-risk practitioners.
- Scenarios are plausible pathways, not predictions.
- Official DCCE/platform documentation takes precedence over text embedded in supplied images.
- The reference illustration style and five-color blue palette remain locked.
- The old user-request workflow is out of scope for both roll-ups.
