---
title: Roo Code on Windows can reliably pass API secrets to MCP servers by referencing 
tags: [roo-code, windows, mcp, environment-variables, secret-management, vscode]
created: 2026-04-26
source: User-confirmed fix from live incident: Roo Windows CMD env parsing for API keys
project: github.com/soul-brews-studio/arun_creagy
---

# Roo Code on Windows can reliably pass API secrets to MCP servers by referencing 

Roo Code on Windows can reliably pass API secrets to MCP servers by referencing VS Code environment substitution `${env:VAR_NAME}` in MCP config values, rather than embedding plaintext or relying on shell-specific expansion patterns. Ensure variable exists before launching VS Code so extension host inherits it. This avoids parsing drift and keeps secrets out of config files.

---
*Added via Oracle Learn*
