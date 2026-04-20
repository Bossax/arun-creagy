---
date: 2026-04-09T07:50:30Z
type: info
status: raw
significance: important
---

# Markdown table leading empty cell guardrail

When appending rows to a Markdown table in this repo, do not start data rows with an empty leading cell like:

| | 2026-04-09 | ...

The double pipe `| |` creates an empty first column and shifts all subsequent cells one position to the right, corrupting the table schema.

Instead, always start rows with the first real value:

| 2026-04-09 | learning | ψ/memory/... | ...

This keeps the column alignment consistent and preserves the table structure when adding new backfill rows or other entries.

Logged via /fyi --important

