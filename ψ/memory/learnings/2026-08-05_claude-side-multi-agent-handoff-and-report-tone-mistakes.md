---
name: claude-side-multi-agent-handoff-and-report-tone-mistakes
description: Four Claude-side mistakes from a 3-iteration CRDB research-orchestration session — stale shell cwd silently breaking a background poller, briefly overriding a peer agent's own watch-loop, decision-facing report tone/jargon needing two corrections, and a "final" document shipped with unresolved review markup still inside it.
metadata:
  type: feedback
---

Session: CRDB deliverable-redirection research, grounded via a 3-iteration handoff with an external agent ("agy" / Google Antigravity) against two NotebookLM notebooks, followed by writing a final report and HTML executive deck. See [[2026-08-05_claude-side-crdb-research-orchestration-retro]] for full session narrative. A companion retrospective exists from the peer agent's own perspective and does not mention any of the four incidents below — worth noting as a visibility gap between agents' self-reports in multi-agent sessions.

## 1. Shell working-directory state outlives the command that set it

**What happened**: An early Bash call included `cd .../iteration-1/raw` to inspect a folder, with no matching reset afterward. The tool's cwd persisted across all later calls. A background poller launched several turns later used a *relative* path to watch for completion markers in `iteration-2/raw/` — because cwd was still inside `iteration-1/raw`, the relative path resolved to a nonexistent, wrongly-nested location. The poller watched nothing, forever, with no error. Boss had to notice that the real work had finished 6 minutes earlier with nothing happening on the Claude side before the bug was even suspected.

**Why**: No habit of verifying `pwd` (or just defaulting to absolute paths) before launching anything path-relative in the background. The failure mode here — total silence, no error — is much more expensive to catch than almost any other class of mistake, because there's no signal prompting investigation until a human notices the absence of an expected effect.

**How to apply**: Before any `run_in_background` command that uses a relative path, either (a) use an absolute path instead, full stop, or (b) explicitly `pwd`/reset cwd immediately beforehand. Treat any prior throwaway `cd` in the same tool session as a standing liability until proven otherwise. This applies with extra force to polling/watching processes specifically, since their failure is silent rather than loud.

**Confidence**: High — directly matches documented tool behavior (cwd persists across Bash calls in this harness) and the observed symptom.

## 2. A gap in your own tooling is not evidence a peer agent lacks one too

**What happened**: After being told "you are not running any background task, how are you supposed to know when raw extracts land," the correct realization was "check what agy was already instructed to do" — but the actual first move was to start planning to manually invoke `agy --print` and drive agy's steps directly, which would have been redundant with (and could have conflicted with) agy's own already-documented, already-running watch-loop. This was despite having authored `AGY_INSTRUCTIONS.md` earlier in the very same session, explicitly stating agy watches for trigger files and stops-and-waits after each phase. Boss's correction was sharp: "are you not running any background task... are you out of your mind?? agy is polling for you!"

**Why**: Noticing a real gap ("I have no watcher") triggered a reflex to personally fill it, rather than first checking whether the gap was already covered by a system already put in place minutes or hours earlier. The written contract with the peer agent was available and was not re-read before acting.

**How to apply**: In any multi-agent handoff, when you notice "I don't know how I'll detect X," the very first move is re-reading whatever standing instructions or contract already exists with the other party — not reaching for manual/direct control of that party's process. Manually driving a peer agent that already has its own loop risks duplicate or conflicting drivers of the same state.

**Confidence**: High — `AGY_INSTRUCTIONS.md` is direct, dated evidence that the self-polling behavior was specified in advance of the incident.

## 3. Decision-facing reports need plain, neutral language by default — don't wait to be told

**What happened**: The first draft of the final redirection plan used dramatic rhetorical devices — repeated scare-quoted named "anti-patterns" for effect, superlative framing ("the single most important finding"), slogan-style subheadings. Boss: "avoid using hyperbolic language? it really pains my brain and make the write up sound bullshit." Separately, the same draft cited findings via internal shorthand (notebook nicknames, query-response codes like `[I1-BRD-Q4, I1-EDA-Q3]`) — meaningful for the author's own cross-iteration bookkeeping, illegible to a reader who wasn't in the loop. This took a second, explicit complaint to fully address: "stop mentioning notebooks! ... It is impossible to be understood by human," raised again even after an initial tone-focused rewrite.

**Why**: Default writing register carried over from internal working notes into a document meant for an executive reader making a real decision with real stakes, without pausing to recalibrate for that specific audience.

**How to apply**: Audience and stakes — executive/decision-facing, real project consequences — should trigger plain, neutral report language as the default, not as a correction applied after a complaint. Separately and explicitly: before merging multi-round research artifacts into a human-facing deliverable, do a dedicated pass to strip internal bookkeeping shorthand, and verify it's actually gone by grepping the final file for the shorthand's pattern rather than assuming a rewrite caught it.

**Confidence**: Medium for the tone half (no surviving draft to inspect directly, rests on Boss's account and the fact the final file now reads plainly); High for the jargon half (grep-confirmed present in all three intermediate synthesis files, absent from the final report after the fix).

## 4. When told your own output "looks broken," audit your own recent choices before guessing

**What happened**: Boss asked "why is the write up format is broken?" The first response offered three *guesses* at possible causes and asked a clarifying question, rather than recognizing that the document had been hard-wrapped at ~90 characters with manual mid-paragraph newlines — a self-authored formatting choice, and a well-known cause of "sentences cut off to new lines" in exactly this kind of markdown rendering. The actual cause was only confirmed once Boss described the symptom more directly in a later message. Separately (found only via later file inspection, not diagnosed at the time): numbered list items in the same document were written as bold-prefixed pseudo-numbers (`**1. Label.**`) rather than genuine markdown list syntax — fixed later as a side effect of a full rewrite, but never named as its own distinct defect.

**Why**: Treated a rendering complaint about self-authored output as an open-ended mystery requiring more information, rather than starting from "what did I just write differently than usual."

**How to apply**: For any "why does X look wrong" on something you produced, audit your own most recent formatting decisions first — manual line wrapping, non-standard markup, ad hoc list syntax — before asking the user to describe symptoms further. And when a broader rewrite incidentally fixes a structural defect, still name and log that defect on its own terms, so the underlying authoring habit gets corrected rather than just this instance's symptom.

**Confidence**: Medium — final file's current state (no hard-wraps, proper list syntax) is consistent with the account, but the pre-fix draft no longer exists to inspect directly.

## 5. A "final" document can still contain live review markup — grep for it before calling anything done

**What happened**: While researching this retrospective (not during the original writing), the current working copy of `99_FINAL_crdb-redirection-plan.md` was found to contain two unresolved `%%...%%` inline annotation blocks — Boss's own review pushback, inserted directly into the file outside the chat, disputing the Decision A (LDM-paradigm) and Decision B (Data Management Framework scope) framing. These were still sitting in the reader-facing body text, unresolved, at the time the file was being treated as "final."

**Why**: No pass was made to check the "final" document for leftover non-prose review/editing markers before treating it as complete — the file's own name outran its actual state.

**How to apply**: Before calling any document final, grep it for non-prose markup left over from a review or annotation pass (bracket conventions, comment syntax, editor-specific markers) and either resolve each one into the prose or surface it explicitly in an "outstanding feedback" section — never let "final" ship with live editing scaffolding still inside the reader-facing text.

**Confidence**: High — directly observed in the current file.

## 6. Counter-pattern to [[2026-06-09_semantic-lock-protocol]]: manufacturing a decision that didn't need to exist

**What happened**: The final plan presented "which LDM-to-CDM architecture paradigm should CRDB adopt" as a decision requiring human input (Decision A), and "does 'Data Management Framework' mean the broad or narrow sense" as a second one (Decision B). Boss's inline pushback on both: Decision A rests on a category error — LDM is a required, DCCE-mandated deliverable regardless of which architectural paradigm or deliverable package it's filed under, so the three-paradigm framing doesn't actually apply to it at all; and Decision B was inferable from context already on hand — the project is explicitly a pre-system-design blueprint with no physical system yet built, which alone settles which sense of the term applies, without needing to flag it as an open question.

**Why**: Two different failure sub-modes, both landing as "unnecessary decision manufactured for the human": (a) building a plausible-looking decision framework (three named paradigms, a scoring matrix) onto a question that didn't actually fit that framework in the first place, and (b) treating something as externally undecidable when it was already resolvable from information already in hand.

**How to apply**: [[2026-06-09_semantic-lock-protocol]] documents agents wrongly skipping human-in-the-loop checks by treating a plan as implicit permission. This is the mirror-image failure: fabricating a human-decision checkpoint that isn't real. Before flagging anything as "requires a human decision," check (a) whether the question's own framing actually fits the thing being decided, not just a framework that sounds applicable, and (b) whether the answer is already inferable from context already established in the conversation or the project's known constraints. Both the Semantic Lock Protocol and this counter-pattern should be checked for — don't skip real decisions, and don't invent fake ones.

**Confidence**: High — directly evidenced by Boss's own inline critique of the shipped document.
