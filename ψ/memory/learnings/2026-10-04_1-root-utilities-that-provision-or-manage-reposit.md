---
id: learning_2026-10-04_1-root-utilities-that-provision-or-manage-reposit
type: learning
title: "1. Root utilities that provision or manage repositories belong in tools/; operat"
concepts: [rrr, shared-skills, node-js, intl-segmenter, multi-client, thai-writer, writing-th, fleet-propagation]
tags: [rrr, shared-skills, node-js, intl-segmenter, multi-client, thai-writer, writing-th, fleet-propagation]
created: 2026-10-04
indexed_at: 2026-10-04T01:17:49.544Z
updated_at: 2026-10-04T01:17:49.544Z
hash: sha256:73cb3510f83ee88595fb92dcc608f22a553f513f889d3ffecf949090b66bd365
source: rrr on 08.17_writing-th-v7-node-migration-and-fleet-propagation
arra_id: learning_2026-10-04_1-root-utilities-that-provision-or-manage-reposit
arra_type: learning
arra_concepts: [rrr, shared-skills, node-js, intl-segmenter, multi-client, thai-writer, writing-th, fleet-propagation]
arra_created: 2026-10-04T01:17:49.544Z
---

# 1. Root utilities that provision or manage repositories belong in tools/; operat

1. Root utilities that provision or manage repositories belong in tools/; operational scripts scoped to a workflow belong strictly in skills/<name>/scripts/. Mixing them at root causes taxonomy fragmentation.
2. In multilingual text processing (e.g. Thai word tokenization), native engine runtimes like Node.js ICU Intl.Segmenter eliminate heavy, OS-dependent Python virtual environments (.venv), ensuring zero-dependency, instantaneous execution across multi-agent environments.
3. Supporting multi-client AI agents (Claude Code, Google Antigravity, OpenAI Codex CLI) requires declarative top-level agent management in agents/ and a single provisioning pipeline (tools/sync-skills.ps1) that populates each client's specific agent directory and purges legacy definitions automatically.
4. When propagating changes across a fleet of submodules, automated scripts must anticipate dirty working trees in consumer checkouts (e.g. IDE/markdown auto-formatting) and cleanly reconcile them before checkout.

---
*Added via Oracle Learn*
