import PyInstaller.__main__
import os
import shutil
from pathlib import Path

# --- CONFIGURATION ---
APP_NAME = "CRI_Impact_Dashboard"
ENTRY_POINT = "launcher.py"
DATA_FOLDERS = ["data", "assets"]
ADDITIONAL_FILES = ["app.py"]

def build():
    print(f"🚀 Starting Hardened Standalone Build (Non-Interactive): {APP_NAME}")
    
    # 1. Prepare PyInstaller Arguments
    params = [
        ENTRY_POINT,
        "--name", APP_NAME,
        "--onedir",
        "--noconsole",
        "--clean",
        "--noconfirm", # FIX: Bypasses the "Delete output directory" prompt
        "--distpath", "./dist",
        "--workpath", "./build",
        # FIX: Explicitly collect all metadata, binaries, and data for critical packages
        "--collect-all", "streamlit",
        "--collect-all", "plotly",
        "--copy-metadata", "streamlit",
        "--copy-metadata", "plotly",
    ]

    # 2. Add Main Script and Folders
    for folder in DATA_FOLDERS:
        if os.path.exists(folder):
            params.extend(["--add-data", f"{folder}{os.pathsep}{folder}"])
    
    for file in ADDITIONAL_FILES:
        if os.path.exists(file):
            params.extend(["--add-data", f"{file}{os.pathsep}."])

    # 3. Execute Build
    print(f"🛠 Running PyInstaller with: {params}")
    PyInstaller.__main__.run(params)

    print(f"✅ Hardened Build Complete! Your portable app is in: ./dist/{APP_NAME}/")
    print(f"👉 Instructions: Zip the '{APP_NAME}' folder and share it.")

if __name__ == "__main__":
    # Change to app directory
    os.chdir(Path(__file__).parent)
    build()
