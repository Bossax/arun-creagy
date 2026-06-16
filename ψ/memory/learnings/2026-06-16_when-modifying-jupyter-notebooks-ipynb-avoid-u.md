---
title: When modifying Jupyter Notebooks (.ipynb), avoid using the `replace` tool for co
tags: [jupyter_notebooks, tool_usage, verification, causality]
created: 2026-06-16
source: Oracle Learn
---

# When modifying Jupyter Notebooks (.ipynb), avoid using the `replace` tool for co

When modifying Jupyter Notebooks (.ipynb), avoid using the `replace` tool for complex, multi-line edits due to the strict JSON formatting and escaping requirements, which often lead to silent failures. Instead, prefer `write_file` for complete rewrites to guarantee structural integrity. Most importantly, ALWAYS verify the result of a file modification (e.g., using `git diff` or by reading the file) before reporting success to the user to maintain trust and causality.

---
*Added via Oracle Learn*
