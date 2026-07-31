# Canva asset-generation delegation

## Attach to ChatGPT

1. `layout_prototype.png` — layout, zones, hierarchy, and asset placement authority.
2. `review_v03.md` — Thai content and illustration-reset authority.
3. A style-only illustration sheet, when available — object construction, line, and flat-fill authority only.

## Prompt

```text
Study the attached layout prototype and revision specification. You are preparing reusable illustration assets for Canva; do not redesign the rollup and do not generate a full poster.

First, think through the composition and identify the minimum set of reusable illustration assets needed to assemble the rollup in Canva. Do not assume every visible object needs to be a separate asset. Prefer fewer, meaningful, reusable assets. Keep all typography, Thai text, route labels, evidence, citations, and barriers editable in Canva rather than embedded in images.

Return only an asset manifest. For every proposed asset, state:
1. asset name;
2. purpose and exact placement in the layout;
3. aspect ratio and whether the background must be transparent;
4. which elements belong inside the asset and which must stay as Canva text;
5. the flat-vector style rules it must retain;
6. whether it is essential or optional.

Do not generate any image yet. Wait for my approval of the manifest.

After I approve the manifest, write the generation prompt for Asset 01 only and wait for me to say “generate Asset 01.” Then generate exactly one asset at a time, in the approved order. Every generated asset must be text-free, use the approved palette and flat-vector treatment, and must not invent claims, numbers, labels, citations, geography, logos, or a new layout.
```
