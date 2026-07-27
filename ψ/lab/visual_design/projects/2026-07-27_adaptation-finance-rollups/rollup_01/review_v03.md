# Review v03 — text fidelity and language coverage

## Finding

Draft 3 contains generated English copy that differs from the approved Markdown and introduces unsupported content. It also embeds typography in the image. Thai editable layout copy was absent.

## Decision

- Image-generation briefs must be text-free and must not name or render display copy.
- `layout_text_en.md` and `layout_text_th.md` are the only approved sources for final display text.
- All text, route labels, numbers, and source notes are added in the design application after image generation.

## Do not use in the final layout

- Any wording, criteria, process stages, or source note rendered in Draft 3 unless it matches the layout-copy files exactly.
