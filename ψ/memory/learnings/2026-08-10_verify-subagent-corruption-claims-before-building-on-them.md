---
title: Verify a subagent's "confirmed via direct inspection" claim before building expensive work on it
date: 2026-08-10
project: Arun_Creagy (CRDB)
tags: [verification, subagent-trust, data-integrity, scope-drift]
---

## The pattern

A background diff subagent reported that `data_catalog_v4.csv` had ~55,700 Thai characters corrupted into literal `?` runs, explicitly claiming this was "confirmed via raw byte inspection... not a rendering issue." That claim was accepted at face value and used to design and execute a full downstream scoring pipeline (a v3-fallback-join mechanism, then an entire Stage B agent run scoring signals against the catalog).

The claim was completely false. Direct byte-level inspection (`xxd`/`od`, counting literal `0x3F` bytes across the whole file) found zero corruption — the file was, and had always been, clean UTF-8. The actual cause was that the `Grep` tool's content-display path was silently mangling multi-byte Thai UTF-8 sequences into `?` on this Windows/Git-Bash environment, while `Read` and raw hex tools rendered the same bytes correctly. The original subagent almost certainly inspected the file through the same broken display path and mistook a rendering artifact for real data corruption — while describing its own (wrong) finding as directly byte-verified.

## Why this matters

The failure wasn't that a subagent made a mistake — that's expected and why review exists. The failure was that a *strong, specific verification claim* ("confirmed via raw byte inspection") was treated as sufficient grounds to skip independent spot-checking, when the check itself (`xxd` on a handful of rows) would have taken under a minute and would have caught the error immediately, before any downstream work was built on it.

## The generalizable rule

When a subagent (or any tool output) reports a surprising finding *and* describes its own verification method in confident, specific terms, that description is itself a claim, not a substitute for independent verification — especially when:
- the finding is surprising (silent, large-scale data corruption in a project file is surprising)
- the downstream cost of acting on a wrong finding is high (launching another agent run, redesigning a data pipeline around a workaround)

The fix is cheap relative to the risk: one direct, independent spot-check of the specific claim (not a full re-audit) before treating it as ground truth for anything expensive downstream.

## Related

This session also surfaced a second, structurally similar failure: treating a Stage A document's stated purpose ("identify the top 10 most business-critical datasets") as current scope, when a later project decision had already superseded it. Both failures share a root cause — trusting a written claim over checking the underlying current reality directly — even though one was a technical/data claim and the other was a scope/process claim.
