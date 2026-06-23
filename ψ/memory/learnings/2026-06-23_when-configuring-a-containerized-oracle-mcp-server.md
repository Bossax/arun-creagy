---
title: When configuring a containerized Oracle MCP server (like oracle-v2 running on Bu
tags: [docker, mcp, lancedb, ollama, win32]
created: 2026-06-23
source: Arun Session rrr
---

# When configuring a containerized Oracle MCP server (like oracle-v2 running on Bu

When configuring a containerized Oracle MCP server (like oracle-v2 running on Bun) to connect to a host's Ollama instance on Windows, you must configure OLLAMA_BASE_URL to point to http://host.docker.internal:11434. LanceDB connections are serverless and open local directories instantly, but generating query or document embeddings will fail with connection errors if Ollama is not reachable or the model (like bge-m3) is not pulled on the host.

---
*Added via Oracle Learn*
