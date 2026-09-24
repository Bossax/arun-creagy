# Style-capture evidence — TH

**Timestamp:** 2026-09-25 00:31 (Asia/Bangkok)  
**Mode:** In-place single-file refinement  
**Edited file:** `ψ/incubate/drafts/crdb-full-report-2.3/draft-v2-2.3.1.md`  
**Baseline:** `HEAD` version of the same file  
**Focus:** Reader onboarding, causal transitions, and the introduction of technical concepts

## Computed diff record

The required word-level comparison was run before analysis:

```text
python .agents/skills/writing-th/scripts/diff_word_table.py --git ψ/incubate/drafts/crdb-full-report-2.3/draft-v2-2.3.1.md
```

It returned 150 change rows. The revisions are overwhelmingly structural rather than stable lexical substitutions: they replace short requirement-led passages with a staged explanation, add transitions between concepts, and add concrete examples of what a technical relationship must explain. No content-specific term pair is promoted from this capture.

## Disposition of the computed rows

| Computed-row groups | Change type | Disposition |
|---|---|---|
| Scope paragraph edits | Requirement wording and scope boundary | Not lexical — content/scope specific |
| NCAIF framing and website explanation | Reorders the reader's entry point around a visible function | Structural — promoted as reader onboarding |
| Data-platform and governance bridge | Explains why the visible artifact or dataset list is insufficient | Structural — promoted as causal transition |
| Conceptual-model and data-domain explanation | Defines each concept only after its work is made necessary | Structural — promoted as reader onboarding |
| Sitemap explanation and revised mapping table | Separates distinct artifacts before using them in analysis | Structural — retained as supporting evidence |
| Entity-relationship examples and framework introduction | Grounds an abstraction in the question it must answer | Structural — retained as supporting evidence |
| Adaptation-cycle, user-route, governance, metadata, and CCIC revisions | Changes report-specific content, terminology, and institutional claims | Not lexical — content correction; not promoted |

## Confirmed generalizable pattern

When a technical section introduces an unfamiliar model, classification, framework, or system component, write a reader path rather than a term sequence:

1. establish the visible function or problem;
2. state why the immediately preceding artifact, list, or view does not settle that problem;
3. introduce the next concept by the work it performs; and
4. only then define components and technical detail.

This confirmation was supplied by Boss on 2026-09-25: strip content-specific information and retain the narrative discipline that prevents skipped logic, missing introductions, and abrupt transitions.
