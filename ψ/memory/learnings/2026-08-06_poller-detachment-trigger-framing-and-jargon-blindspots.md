---
name: poller-detachment-trigger-framing-and-jargon-blindspots
description: Three Claude-side mistakes from the CRDB Phase B research and /seal session — a detached (nohup+disown) poller giving a false-positive completion signal, three failed attempts to correctly frame a /seal T-E-D-A trigger before landing on artifact-level causality, and jargon that read as invisible from the inside despite an already-completed hyperbole pass.
metadata:
  type: feedback
---

Session: CRDB Phase B research (iterations 4-5), rewriting the redirection plan as v2, and a `/seal` pass registering the result into the project ledgers. Continues directly from [[2026-08-05_claude-side-multi-agent-handoff-and-report-tone-mistakes]], which flagged a stale-cwd poller bug in the same project one session earlier.

## 1. A detached poller's quick completion is not evidence it worked

**What happened**: A background poller was launched as `nohup bash -c '...loop...' & disown`, wrapped inside a single synchronous Bash tool call. That outer call returned almost immediately (it only had to background the loop and echo a PID), and the harness reported it as "completed" — which was technically true of the *launcher*, but was mistaken for the *poll condition* being met. The actual watch loop was detached from the harness's own process tracking via `disown`, and when checked, had not survived at all; the raw folders it was supposed to be watching were still empty.

**Why**: The mental model was "background a long-running loop so I don't block," but `nohup`+`disown` solves a different problem (surviving a *shell session* ending) than what was needed here (a notification when a *condition* is met, tracked by *this* harness). Using `run_in_background: true` directly on the loop itself is the correct primitive — it does both survival and tracked-completion natively, without a detachment layer that severs the harness's ability to observe the real process.

**How to apply**: Never wrap a poller intended for harness notification in `nohup`/`disown` or any other detachment mechanism. If a Bash tool call with `run_in_background: true` returns "completed" almost immediately, treat that as a signal to double check what actually finished — the launcher, or the condition — before reporting anything to the user as done.

**Confidence**: High — directly observed (empty raw folders, no live process matching the loop) immediately after the false-positive notification.

## 2. Re-derive causality from artifacts, not from what's freshest in your own context

**What happened**: Running `/seal`, the Trigger (the "why" in a T-E-D-A chain, explicitly meant to exclude file paths per the skill's own hard rule) was proposed incorrectly twice before Boss corrected it to the right framing. First attempt: "Boss's 6/10 critique of v1" — substituting feedback-about-the-work for the actual motivating cause. Second attempt: "comparing v1 against the TOR70 failure-mode analysis" — closer, but still centered on my own most recent artifact (the rewrite) rather than the two independent, pre-existing artifacts that actually caused the reconsideration. The correct framing, which Boss had to state directly: the trigger was the combination of TOR70's already-validated structural flaws (an artifact) and a separate CRDB deliverable-drift audit trace (another artifact) — two facts that existed independently of any critique or rewrite, and whose combination is what motivated the decision.

**Why**: When asked to reconstruct "why did this happen," the first things available are the most recent, most self-referential explanations (my own critique, my own most recent work product) — those are easy to reach for and *feel* like an answer, but they are downstream restatements, not the underlying cause. The actual causal artifacts predate and are independent of anything I produced this session.

**How to apply**: For any causality-tracing task (T-E-D-A, root-cause analysis, retrospective triggers), explicitly ask "what two or more things existed independently, before my own analysis or output, that together produced this" — and prefer that answer over whatever framing is most recently sitting in context, even if the recent framing sounds more complete or eloquent.

**Confidence**: High — directly evidenced by two rejected proposals and Boss's explicit correction on the third.

## 3. Tone review needs a separate pass for coined/metaphorical jargon, not just hyperbole

**What happened**: A hyperbole-removal pass had already been run on the redirection plan report (removing dramatic phrasing like "the entire value of..." and "the correction that most changes v1"). Despite that, Boss later named four specific terms — "boiling-the-ocean," "spine," "next wave," "dual-seal" — as jargon that read as made-up, context-specific words rather than common English. None of these had been caught by the hyperbole pass, because they aren't dramatic or superlative in register; they're quietly coined compound/metaphorical labels absorbed from the source literature or invented as shorthand while writing, and read as perfectly normal descriptive language from the inside.

**Why**: A single "does this sound hyperbolic/dramatic" self-check catches one category of tone problem (inflated register) but not a different one (jargon that sounds plain to the author because it's been used repeatedly during drafting, but is opaque to a first-time reader). These are different failure modes requiring different detection heuristics.

**How to apply**: Treat tone review as at least two distinct passes: (a) hyperbole/dramatic register — superlatives, rhetorical framing, scare quotes for effect; (b) coined/metaphorical compound terms — any label that isn't a standard, widely-recognized English word or an explicitly-defined technical term, especially ones absorbed from research sources during the same drafting session. When in doubt on pass (b), ask "would this word need a definition for a reader outside this project" — if yes, replace it with a plain descriptive phrase instead.

**Confidence**: High — four concrete examples named directly by Boss, none caught by the prior tone pass.
