import sys
import re
from pathlib import Path

def check_density(source_path, draft_path, min_ratio=0.8):
    with open(source_path, 'r', encoding='utf-8') as f:
        source_text = f.read()
    with open(draft_path, 'r', encoding='utf-8') as f:
        draft_text = f.read()
        
    # Remove whitespaces for pure character density calculation
    src_len = len(re.sub(r'\s+', '', source_text))
    draft_len = len(re.sub(r'\s+', '', draft_text))
    
    if src_len == 0:
        print("✅ Source is empty, no density check required.")
        sys.exit(0)
        
    ratio = draft_len / src_len
    
    print(f"📊 Density Check: Source = {src_len} chars | Draft = {draft_len} chars | Ratio = {ratio:.2f}")
    
    if ratio < min_ratio:
        print(f"\n❌ DENSITY FAILED! Draft is only {ratio*100:.1f}% the size of the source (Minimum required: {min_ratio*100:.1f}%).")
        print("Reason: Destructive Compression / Task Executor Bias detected.")
        print("Action: You must expand the draft to preserve technical details, schemas, and examples.")
        sys.exit(1)
    else:
        print("✅ DENSITY PASSED! Structural weight is preserved.")
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python check_density.py <source_path> <draft_path> [min_ratio]")
        sys.exit(1)
    
    ratio = float(sys.argv[3]) if len(sys.argv) > 3 else 0.8
    check_density(sys.argv[1], sys.argv[2], ratio)
