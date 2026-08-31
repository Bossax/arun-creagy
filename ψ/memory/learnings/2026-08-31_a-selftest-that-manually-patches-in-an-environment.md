---
id: learning_2026-08-31_a-selftest-that-manually-patches-in-an-environment
type: learning
title: A selftest that manually patches in an environment variable does not prove a rea
concepts: [mcp-server, environment-variables, windows-session, testing-methodology, verification]
tags: [mcp-server, environment-variables, windows-session, testing-methodology, verification]
created: 2026-08-31
indexed_at: 2026-08-31T16:21:37.551Z
updated_at: 2026-08-31T16:21:37.551Z
hash: sha256:cecdb1a35e934be68c59eeabda8e28da5218585d944b16d32f2084ad8020b1b7
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-31_a-selftest-that-manually-patches-in-an-environment
arra_type: learning
arra_concepts: [mcp-server, environment-variables, windows-session, testing-methodology, verification]
arra_created: 2026-08-31T16:21:37.551Z
---

# A selftest that manually patches in an environment variable does not prove a rea

A selftest that manually patches in an environment variable does not prove a real launch path works — it proves the code's logic works given that value. Built an MCP server calling Alibaba DashScope (Qwen models); DASHSCOPE_API_KEY existed in Windows User env scope but was set after the current login session began, so the live process env didn't have it. A selftest that manually re-injected the key via System.Environment.GetEnvironmentVariable succeeded with a real API call, giving false confidence. The actual MCP tool call then failed, because Claude Code's MCP-spawned subprocess inherits environment differently than the manual test shell did — a fresh login is needed to propagate a User-scope env var set mid-session. Before declaring an integration verified, check whether the test's setup (process spawn path, inherited state, auth source) actually matches the real invocation's setup; if it doesn't, the gap needs to be stated, not glossed over by a passing but non-representative test.

---
*Added via Oracle Learn*
