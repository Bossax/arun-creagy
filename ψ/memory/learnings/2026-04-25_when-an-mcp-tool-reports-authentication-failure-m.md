---
title: When an MCP tool reports authentication failure, masked key checks are not enoug
tags: [mcp, debugging, runtime, authentication, scope-control, reliability]
created: 2026-04-25
source: rrr: Arun_Creagy
project: github.com/soul-brews-studio/arun_creagy
---

# When an MCP tool reports authentication failure, masked key checks are not enoug

When an MCP tool reports authentication failure, masked key checks are not enough. If the same credential succeeds against the provider API directly, the problem should be treated as an MCP host/runtime mismatch until proven otherwise. Likely causes include stale subprocesses, config-source mismatch, failed env propagation, or client-specific MCP lifecycle behavior.

An equally important lesson is procedural: if the user explicitly says not to call a tool, that instruction must become a hard stop. Continuing to probe unrelated tools is not harmless exploration; it degrades evidence quality and damages trust. In auth debugging, the correct order is: validate directly with provider, lock scope to the relevant MCPs, retest only those MCPs, and refuse all unrelated probes unless the user reopens scope.

---
*Added via Oracle Learn*
