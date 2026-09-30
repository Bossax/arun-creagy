---
id: learning_2026-09-30_restoring-windows-host-ollama-connectivity-for-d
type: learning
title: "# Restoring Windows Host Ollama Connectivity for Dockerized Oracle MCP Services"
concepts: [docker, mcp, lancedb, ollama, win32, vector-search, troubleshooting]
tags: [docker, mcp, lancedb, ollama, win32, vector-search, troubleshooting]
created: 2026-09-30
indexed_at: 2026-09-30T03:30:13.450Z
updated_at: 2026-09-30T03:30:13.450Z
hash: sha256:434f168c41508b00c9f13c7ac2d312f77f2221ee9cee553ebdc4474376cf8b73
source: Arun Session - Windows Ollama Docker Vector Fix
project: github.com/sitth/arun_creagy
arra_id: learning_2026-09-30_restoring-windows-host-ollama-connectivity-for-d
arra_type: learning
arra_concepts: [docker, mcp, lancedb, ollama, win32, vector-search, troubleshooting]
arra_created: 2026-09-30T03:30:13.450Z
---

# # Restoring Windows Host Ollama Connectivity for Dockerized Oracle MCP Services

# Restoring Windows Host Ollama Connectivity for Dockerized Oracle MCP Services

When Oracle MCP containers (`oracle-arun-creagy`, `oracle-archon`, etc.) report vector search degradation due to Ollama probe timeouts:

1. **Retain Docker Host URL**: Keep `OLLAMA_BASE_URL=http://host.docker.internal:11434` in `docker-compose.yml`.
2. **Expose Host Network in Windows Ollama**:
   - In the Windows Ollama desktop app, enable **"Expose Ollama to the network"**.
   - Alternatively, configure `OLLAMA_HOST=0.0.0.0:11434` in Windows environment variables and restart Ollama.
3. **Behavior & Verification**:
   - Windows Ollama binds by default to `127.0.0.1:11434`, rejecting incoming bridge/gateway packets from Docker containers.
   - Enabling the network exposure toggle immediately unblocks host-gateway traffic.
   - Vector health recovers dynamically to `connected` / `vectorAvailable: true` on the next query without requiring container rebuilds.

---
*Added via Oracle Learn*
