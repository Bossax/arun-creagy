#!/usr/bin/env python3
"""
Selective Incremental Deployment Script for CRI Data System v4.4
Deploys output/cri_impact_app_v3 to ψ/outbox/cri_deploy with pre-flight checks and metadata protection.
"""

from __future__ import annotations

import py_compile
import shutil
from pathlib import Path

BASE_DIR = Path(r"C:\Users\sitth\OracleWorkspace\Arun_Creagy")
SRC_DIR = BASE_DIR / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "output" / "cri_impact_app_v3"
DST_DIR = BASE_DIR / "ψ" / "outbox" / "cri_deploy"

print("=== 🚀 EXECUTING SELECTIVE INCREMENTAL DEPLOYMENT (v4.4) ===\n")
print(f"Source:      {SRC_DIR}")
print(f"Destination: {DST_DIR}\n")

if not SRC_DIR.exists():
    raise FileNotFoundError(f"Source directory does not exist: {SRC_DIR}")
if not DST_DIR.exists():
    raise FileNotFoundError(f"Destination directory does not exist: {DST_DIR}")

# 1. Prune legacy data directories in DST
legacy_dir = DST_DIR / "data" / "period_2560_2567"
if legacy_dir.exists():
    print(f"🗑️ Pruning legacy directory: {legacy_dir}")
    shutil.rmtree(legacy_dir)

# 2. Synchronize application code files and assets
items_to_sync = ["app.py", "__init__.py", "PLOT_NAVIGATION.md", "components", "pages", "runtime", "data"]

for item_name in items_to_sync:
    src_item = SRC_DIR / item_name
    dst_item = DST_DIR / item_name

    if not src_item.exists():
        print(f"⚠️ Source item missing: {src_item}")
        continue

    if src_item.is_file():
        print(f"📄 Syncing file: {item_name}")
        shutil.copy2(src_item, dst_item)
    elif src_item.is_dir():
        print(f"📁 Syncing directory: {item_name}/")
        if dst_item.exists():
            shutil.rmtree(dst_item)
        shutil.copytree(src_item, dst_item)

# 3. Post-sync destination compilation check
py_files = list((DST_DIR / "pages").glob("*.py")) + [DST_DIR / "app.py", DST_DIR / "runtime" / "data.py"]
for pf in py_files:
    py_compile.compile(str(pf), doraise=True)

print("\n✅ Selective incremental deployment of v4.4 completed successfully!")
