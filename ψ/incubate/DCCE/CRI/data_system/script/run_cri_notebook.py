#!/usr/bin/env python3
r"""
Execute a Jupyter notebook inside the CRI data_system venv and save the executed copy.

Usage:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\run_cri_notebook.py
"""

from __future__ import annotations

import json
from pathlib import Path

import nbformat
from nbclient import NotebookClient


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[6]
DATA_SYSTEM_ROOT = PROJECT_ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system"
NOTEBOOK_PATH = DATA_SYSTEM_ROOT / "script" / "analysis_notebooks" / "cri_province_impact_demo.ipynb"
OUTPUT_PATH = DATA_SYSTEM_ROOT / "script" / "analysis_notebooks" / "cri_province_impact_demo.executed.ipynb"
REPORT_PATH = DATA_SYSTEM_ROOT / "script" / "analysis_notebooks" / "cri_province_impact_demo.execution_report.json"


def main() -> None:
    if hasattr(__import__('sys').stdout, 'reconfigure'):
        __import__('sys').stdout.reconfigure(encoding='utf-8')

    if not NOTEBOOK_PATH.exists():
        raise SystemExit(f"Notebook not found: {NOTEBOOK_PATH}")

    with NOTEBOOK_PATH.open("r", encoding="utf-8") as fp:
        notebook = nbformat.read(fp, as_version=4)

    client = NotebookClient(
        notebook,
        timeout=300,
        kernel_name="python3",
        resources={"metadata": {"path": str(DATA_SYSTEM_ROOT)}},
    )
    client.execute()

    with OUTPUT_PATH.open("w", encoding="utf-8") as fp:
        nbformat.write(notebook, fp)

    report = {
        "script_path": str(SCRIPT_PATH),
        "notebook_path": str(NOTEBOOK_PATH),
        "executed_notebook_path": str(OUTPUT_PATH),
        "cell_count": len(notebook.cells),
        "status": "ok",
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
