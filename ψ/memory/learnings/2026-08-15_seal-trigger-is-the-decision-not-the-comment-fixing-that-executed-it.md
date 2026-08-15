---
name: seal-trigger-is-the-decision-not-the-comment-fixing-that-executed-it
description: When sealing work that followed a body of comment-fixing/hardening, check whether a higher-level decision actually caused that work before drafting the T-E-D-A Trigger — don't default to "the review comments" just because that's the most visible evidence in-session.
metadata:
  type: feedback
---

When a user says "let's seal these artifacts" right after watching a body of comment-driven revision happen, the natural (and wrong) move is to draft the seal's Trigger as "the user's review comments" — because that's the most recent, most visible causal thread in the conversation. In this session, the actual trigger was a separate, higher-level decision (standardize WP6's deliverable format to industry-standard BA convention, and drop the NFR Thresholds Table from scope entirely) that the comment-fixing work was executing, not the cause of it. The comments were real and got resolved, but they weren't why the work mattered enough to seal — the standardization decision was.

**Why**: Boss corrected an initial T-E-D-A proposal ("no the trigger is to standardize wp6 deliverable to align with industry-standard BA outputs. we decided to drop NFR") after I'd framed the Trigger around "Boss's iterative inline review comments." The seal skill's approval gate caught this before it hit the ledgers, but the correction cost a full extra round-trip. The underlying failure: I had good evidence for *what happened* in the visible conversation but hadn't asked whether something upstream of that visible work was the actual motive.

**How to apply**: Before drafting a T-E-D-A Trigger for `/seal`, especially when the work involved responding to a list of comments/corrections, pause and ask: is there a decision or scope change this work is downstream of, that isn't itself visible as one of the comments? If the answer isn't obvious from the conversation, ask rather than draft-and-wait-for-correction — a wrong Trigger framing tends to also produce a wrong Decision description and can miss real scope effects on other artifacts (in this case, a sprint-plan document that needed six separate amendments once the actual trigger was named). Related: [[seal-approval-gate-catches-scope-not-just-facts]] if that memory exists — the gate's value here wasn't verifying facts, it was verifying causality.
