import sys
import json
import re
from pathlib import Path

def lint(draft_path, lexicon_path):
    with open(draft_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(lexicon_path, 'r', encoding='utf-8') as f:
        lexicon_data = json.load(f)
    
    errors = []
    
    # 1. Lexicon checks
    for entry in lexicon_data.get('lexicon', []):
        banned = entry['banned']
        # Handle cases with ellipses like "สถาปัตยกรรม..."
        pattern = banned.replace("...", ".*?")
        
        if re.search(pattern, content):
            errors.append(f"[LEXICON] Banned word found: '{banned}'. Use '{entry['preferred']}' instead. (Reason: {entry['reason']})")
            
    # 2. Hardcoded Translation Artifacts & Passive Voice
    if re.search(r'ไม่ได้.*?แต่', content):
        errors.append("[STRUCTURE] Translation artifact found: 'ไม่ได้...แต่...'. Rewrite to state the affirmative action directly.")
        
    if re.search(r'ถูก(ดำเนินการ|จัดทำ|สร้าง|พัฒนา|มองว่า|ถือว่า)', content):
        errors.append("[STRUCTURE] Passive voice found: 'ถูก...'. Rewrite to use the active institutional subject (e.g., 'กรมฯ ดำเนินการ...').")
        
    # 3. Conceptual English in parentheses (e.g. (Data Availability))
    # Match Title Cased English concepts in parentheses
    if re.search(r'\([A-Z][a-z]+ [A-Z][a-z]+\)', content):
        errors.append("[JARGON] English conceptual term in parentheses found. Translate to standard institutional Thai.")
        
    if errors:
        print("\n❌ LINT FAILED! The draft violates Harness Constraints:")
        for e in errors:
            print(f"  - {e}")
        print("\nFix these issues in the draft before attempting to merge.")
        sys.exit(1)
    else:
        print("✅ LINT PASSED! No jargon or banned structures detected.")
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python lint_thai_writing.py <draft_path> <lexicon_json_path>")
        sys.exit(1)
    lint(sys.argv[1], sys.argv[2])
