---
id: learning_2026-08-31_dashscope-maas-gateway-git-bash-utf-8-gotcha-pr
type: learning
title: "DashScope MaaS gateway + Git Bash UTF-8 gotcha: private DashScope MaaS gateway e"
concepts: [dashscope, qwen, api-integration, git-bash, utf-8, windows, curl, env-vars]
tags: [dashscope, qwen, api-integration, git-bash, utf-8, windows, curl, env-vars]
created: 2026-08-31
indexed_at: 2026-08-31T14:56:18.407Z
updated_at: 2026-08-31T14:56:18.407Z
hash: sha256:d38515674fecc71e41f7b85b8171df3a7651f62cb6fa7d883944ed63138c5395
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-31_dashscope-maas-gateway-git-bash-utf-8-gotcha-pr
arra_type: learning
arra_concepts: [dashscope, qwen, api-integration, git-bash, utf-8, windows, curl, env-vars]
arra_created: 2026-08-31T14:56:18.407Z
---

# DashScope MaaS gateway + Git Bash UTF-8 gotcha: private DashScope MaaS gateway e

DashScope MaaS gateway + Git Bash UTF-8 gotcha: private DashScope MaaS gateway endpoints (e.g. workspace-specific *.maas.aliyuncs.com) don't follow the public docs' /api/v1/chat/completions path — working paths found by testing were /compatible-mode/v1/chat/completions (OpenAI-compatible) and /api/v1/services/aigc/text-generation/generation (native format). Separately, Git Bash on Windows silently mangles non-ASCII (e.g. Thai) text passed inline via `curl -d '...'` — the call still returns HTTP 200 but the payload is corrupted, so the model responds in the wrong language or complains about unrecognized characters with no error surfaced. Fix: write the JSON payload to a file and send via `curl --data-binary @payload.json -H "Content-Type: application/json; charset=utf-8"`. Always inspect the actual response body, not just HTTP status, when testing non-ASCII API calls from Git Bash on Windows. Also: PowerShell's [Environment]::SetEnvironmentVariable(...,"User") persists to the registry but does not propagate to already-running shell sessions, including a Bash tool call within the same agent session.

---
*Added via Oracle Learn*
