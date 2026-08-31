# Lesson: DashScope MaaS endpoint paths and Git Bash UTF-8 handling

**Context**: Setting up API access to Qwen models via Alibaba Cloud DashScope, using a private workspace MaaS gateway (`ws-pg8s7yunzcnexczp.ap-southeast-1.maas.aliyuncs.com`).

## Findings

1. **Endpoint paths**: The public DashScope docs describe `/api/v1/chat/completions`, but this private MaaS gateway 404s on that path. Working paths confirmed by testing:
   - `/compatible-mode/v1/chat/completions` — OpenAI-compatible chat format
   - `/api/v1/services/aigc/text-generation/generation` — native DashScope format
   Both returned HTTP 200 with valid completions using model `qwen-max`.

2. **Git Bash / Windows UTF-8 bug**: Passing non-ASCII (e.g., Thai) text inline via `curl -d '{"content":"..."}'` in Git Bash on Windows silently mangles the encoding. The API call still succeeds (200 status) but the model receives corrupted bytes and may respond in the wrong language or complain about unrecognized characters. This fails silently — no error, just wrong output. Fix: write the JSON payload to a file with proper UTF-8 encoding, then send with `curl --data-binary @payload.json -H "Content-Type: application/json; charset=utf-8"`.

3. **Windows env var propagation**: `[Environment]::SetEnvironmentVariable(..., "User")` via PowerShell persists to the registry but does not update already-running shell sessions (including a Bash tool call within the same agent session). New terminals/processes pick it up; the current session does not until restarted.

## Why this matters

Any future call to this Qwen/DashScope setup involving non-English text (Thai, for CRDB writing work) must use the file-based payload pattern, not inline `-d`, or output will be silently wrong rather than erroring.
