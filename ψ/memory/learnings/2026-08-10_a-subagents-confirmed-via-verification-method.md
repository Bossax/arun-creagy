---
id: learning_2026-08-10_a-subagents-confirmed-via-verification-method
type: learning
title: "A subagent's \"confirmed via [verification method]\" claim is a claim, not a fact"
concepts: [verification, subagent-trust, data-integrity, scope-drift, tool-reliability]
tags: [verification, subagent-trust, data-integrity, scope-drift, tool-reliability]
created: 2026-08-10
indexed_at: 2026-08-10T08:21:09.092Z
updated_at: 2026-08-10T08:21:09.092Z
hash: sha256:99b764a965161bb2b081a68679f59aab154ff837c5fa418c01a081afc8f7b438
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-10_a-subagents-confirmed-via-verification-method
arra_type: learning
arra_concepts: [verification, subagent-trust, data-integrity, scope-drift, tool-reliability]
arra_created: 2026-08-10T08:21:09.092Z
---

# A subagent's \"confirmed via [verification method]\" claim is a claim, not a fact

A subagent's "confirmed via [verification method]" claim is a claim, not a fact — spot-check it directly before building expensive downstream work on it, especially when the claim is surprising. In a CRDB session, a background diff subagent reported that a data catalog CSV had ~55,700 Thai characters corrupted into literal "?" runs, stating this was "confirmed via raw byte inspection... not a rendering issue." That claim was false: direct hex inspection (xxd/od, counting literal 0x3F bytes) found zero corruption. The actual cause was the Grep tool silently mangling multi-byte Thai UTF-8 display on a Windows/Git-Bash environment, while Read and raw hex tools rendered the same bytes correctly — the original subagent likely inspected the file through the same broken display path and mistook a rendering artifact for real corruption, while describing its own wrong finding as directly byte-verified. A full downstream Stage B scoring pipeline had already been designed and executed around this false premise before it was caught (only because the user asked "what decoder did you use," prompting an independent spot-check).

Generalizable rule: when a tool/subagent reports a surprising finding AND describes its own verification method in confident, specific terms, that description is itself a claim, not a substitute for independent verification — especially when the finding is surprising and the downstream cost of acting on a wrong finding is high (e.g. launching another agent run, redesigning a pipeline around a workaround). The fix is cheap relative to the risk: one direct, independent spot-check of the specific claim before treating it as ground truth for anything expensive downstream.

A structurally similar failure occurred in the same session: treating a Stage A document's stated purpose/goal as current scope, when a later project decision had already superseded it without updating that document. Both failures share a root cause — trusting a written claim over checking the underlying current reality directly.

---
*Added via Oracle Learn*
