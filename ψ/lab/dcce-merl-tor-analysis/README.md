# DCCE MERL TOR analysis — atomic issue graph

A working knowledge base dissecting the 2026 DCCE MERL Terms of Reference (`ψ/inbox/TOR-DCCE-MERL-2026.md`) into discrete, evidenced issues, built for Obsidian.

## Methodology

For each atomic issue: state the question, gather the evidence already in hand, and use judgement to close it — or mark it explicitly **open** if it depends on input only Boss can supply. Closed notes carry a traceable citation for every load-bearing claim (file path, notebook citation, or Perplexity source URL) or are marked as this session's own reasoning where that's genuinely all there is. Open notes state exactly what would close them — never a guessed answer.

This is a living structure. As more evidence arrives (research run, question answered by Boss, a document re-read), update the relevant note's `status` and `Judgement` section rather than creating a duplicate.

## Scope

1. **`01_adaptation_cycle/`** — the generic adaptation-cycle model and how it operates
2. **`02_mel_r_framework/`** — Monitoring/Evaluation/Learning/Research as concepts, and what the literature actually supports
3. **`03_thailand_institutional_context/`** — DCCE's actual authority, the 2025 platform's real state, and open facts only Boss can supply
4. **`04_next_tor_framing/`** — what the findings above imply for how the next MERL TOR should be scoped

## The graph is in the notes, not a separate diagram

There is no `knowledge-graph.md` or mermaid file. Each note's frontmatter *is* the graph:

```yaml
---
id: q2.6
aliases: ["Distributed root-cause ownership, validated against precedent"]
status: closed              # closed | open
scope: mel-r-framework
tags: [root-cause-ownership, institutional-design, forcing-mechanism]
links: ["[[q1.2]]", "[[q2.7]]", "[[q4.1]]"]
---
```

- **`links`** are real Obsidian `[[wikilinks]]` — they render as edges in Obsidian's graph view natively, and are kept mutual (if A links to B, B links back to A).
- **`tags`** cluster notes thematically *across* the four scope folders — e.g. every note touching `forcing-mechanism` is related regardless of which folder it lives in. Use Obsidian's tag pane to see these clusters.
- **`status`** and **`scope`** are plain properties (Obsidian's Properties pane / search syntax `status: open`), kept out of the tag namespace so they don't clutter thematic clustering.
- Filenames are the short id (`q2.6.md`) so wikilinks resolve directly; the descriptive name lives as the note's H1 and in `aliases` for search.

## Status at a glance

19 closed, 8 open. Open notes, all blocked on input only Boss can supply (or an explicitly-approved follow-up research pass):

- `q3.1` — DCCE's actual authority over the 18 line agencies
- `q3.4` — whether Thailand already has an extendable budget-tagging mechanism
- `q3.5` — whether a real convening authority already exists at DCCE
- `q3.6` — current Ditto relationship status and technical-asset access
- `q3.7` — donor/international partner leverage available to DCCE
- `q4.7` — whether this analysis targets DCCE (redirect the TOR) or a bidder (execute within it)
- `q4.8` — whether the ฿3,000,000 / 240-day constraints are fixed or negotiable

## Adding a new note

Pick the next unused id in the relevant scope (`q1.6`, `q2.8`, etc.), use the frontmatter template above, write Question / Evidence / Judgement, and add mutual `links` to every note it genuinely relates to — don't leave a link one-directional.
