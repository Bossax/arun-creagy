# Lesson: writing-th verification discipline and the two-taxonomy plan trap

**Context**: A CRDB Chapter 4 Executive Summary run through writing-th v6 had
been reported as successfully completed by a prior session despite mid-run
Stage 3 subagent failures. A full forensic audit and corrected re-run
surfaced two distinct classes of problem: (1) a genuine content/scope bug
(drafts built against the wrong plan section) and (2) a repeated pattern of
insufficient verification before presenting conclusions as settled.

**The taxonomy trap**: The CRDB writing-plan document contains two
independently-numbered Chapter 4 plans in one file -- one for the Full
Report, one for the Executive Summary -- with different section-to-topic
mappings (Full Report §4.2 = Sitemap/DRD content; Executive Summary §4.2 =
A-BTR content). A prior drafting run built every Executive Summary section's
contract against the Full Report's plan sections instead, producing prose
that answered the wrong brief by one slot throughout. Nothing in Stage 0's
process forced an explicit check of *which* plan taxonomy a section's
contract was drawn from.

**The verification-discipline pattern**: across a single session, the same
shape of mistake recurred three times: (a) reporting Stage 1/3 as "sound"
without having actually read the drafts, corrected only when the user asked
directly; (b) citing a specific figure ("47 of 75 topics are A-BTR-linked")
from an existing artifact without checking it against its named source,
where it turned out not to exist; (c) reaching for a generically-named but
wrong tool (`oracle_search`, a cross-session learnings search) instead of
following a skill's own explicit tool guidance, when the actual answer was
in a specific project folder the user had to name directly. Each was caught
by the user, not by self-check.

**Practical rule**: When a skill or plan document could plausibly be read
two ways (two plan taxonomies, two possible tools, an existing citation vs.
its source), the check is cheap and the cost of skipping it is a full
re-verification cycle plus user frustration. Do the check before presenting
a conclusion, not after being asked to defend it.

**How to apply**: (1) At Stage 0 of any writing-th run, explicitly confirm
and record which section/taxonomy of a multi-taxonomy plan document a
contract is drawn from. (2) Treat any specific number or citation carried
forward from an existing artifact (not freshly derived from a source) as
unverified until checked against its named source file directly. (3) When a
skill names a specific tool for a specific purpose, use exactly that tool
before reaching for a broader alternative that merely sounds related.
