import sys
import shutil
import subprocess
from pathlib import Path

def merge(draft_path, dest_path, lexicon_path=None):
    draft = Path(draft_path)
    dest = Path(dest_path)
    
    if not draft.exists():
        print(f"❌ MERGE FAILED! Draft not found at {draft_path}")
        sys.exit(1)
        
    # Optional: We could run the linter automatically here before merge, 
    # but separating them allows manual linting before the merge step.
    
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(draft, dest)
    
    print(f"✅ MERGE SUCCESSFUL!")
    print(f"Source: {draft_path}")
    print(f"Target: {dest_path}")
    print(f"\nYou may now safely delete or archive the scratch directory: {draft.parent}")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python merge_draft.py <draft_path> <dest_path>")
        sys.exit(1)
    merge(sys.argv[1], sys.argv[2])
