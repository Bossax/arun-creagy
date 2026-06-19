#!/usr/bin/env python3
"""Arun-Creagy Local Session Miner — Hardcoded for local project temp directory."""
import json, os, glob, sys, subprocess, re, time
from datetime import datetime, timedelta, timezone

# Ensure stdout handles UTF-8 for the ψ character
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DIRECT PATH TO ARUN-CREAGY CHATS
project_dirs = [r"C:\Users\sitth\.gemini\tmp\arun-creagy\chats"]
count = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# Auto-detect local timezone offset
local_offset = timedelta(seconds=-time.timezone if time.daylight == 0 else -time.altzone)
local_tz = timezone(local_offset)

def build_repo_map():
    mapping = {}
    try:
        ghq_cmd = 'ghq.exe' if os.name == 'nt' else 'ghq'
        r = subprocess.run([ghq_cmd, 'list', '-p'], capture_output=True, text=True, timeout=5, shell=(os.name == 'nt'))
        for path in r.stdout.strip().split('\n'):
            if path:
                clean_path = path.replace('\\', '/')
                mapping[clean_path.replace('/', '-')] = clean_path.split('/')[-1]
    except: pass
    return mapping

def get_repo_name(project_dir, repo_map):
    return "Arun_Creagy" # Hardcoded for local stability

repo_map = build_repo_map()

seen = {}
for d in project_dirs:
    # Scan the local chat folder for all session logs
    for f in glob.glob(os.path.join(d, 'session-*.jsonl')):
        base = os.path.basename(f)
        if base not in seen or os.path.getmtime(f) > os.path.getmtime(seen[base][0]):
            seen[base] = (f, d)
            
all_files = [(fp, d) for fp, d in seen.values()]
files = sorted(all_files, key=lambda x: os.path.getmtime(x[0]), reverse=True)[:count]

sessions = []
for fp, source_dir in files:
    sid = os.path.basename(fp).replace('session-', '').replace('.jsonl', '')
    first_ts = last_ts = None
    real_human = []
    assistant_count = 0

    try:
        with open(fp, encoding='utf-8') as fh:
            for line in fh:
                try: obj = json.loads(line)
                except: continue
                ts = obj.get('timestamp')
                if ts:
                    if not first_ts or ts < first_ts: first_ts = ts
                    if not last_ts or ts > last_ts: last_ts = ts
                
                # In Gemini-CLI .jsonl, the structure differs from Claude-Code
                # We look for user messages and assistant responses
                t = obj.get('type')
                if t == 'user':
                    text = obj.get('content', '')
                    if text and len(text) > 5:
                        real_human.append(text[:80])
                elif t == 'assistant':
                    assistant_count += 1
    except Exception as e:
        continue

    if not first_ts: continue

    def to_local(iso):
        try:
            # Handle Gemini-CLI timestamp format
            dt = datetime.fromisoformat(iso.replace('Z', '+00:00'))
            return dt.astimezone(local_tz).strftime('%Y-%m-%d %H:%M')
        except: return iso

    dur_min = 0
    if first_ts and last_ts:
        try:
            t1 = datetime.fromisoformat(first_ts.replace('Z', '+00:00'))
            t2 = datetime.fromisoformat(last_ts.replace('Z', '+00:00'))
            dur_min = int((t2 - t1).total_seconds() / 60)
        except: pass

    sessions.append({
        'sessionId': sid[:12],
        'repoName': "Arun_Creagy",
        'startLocal': to_local(first_ts),
        'endLocal': to_local(last_ts),
        'durationMin': dur_min,
        'realHumanMessages': len(real_human),
        'assistantMessages': assistant_count,
        'firstPrompt': real_human[0] if real_human else "Session Start",
        'summary': real_human[0][:80] if real_human else "N/A",
    })

sessions.sort(key=lambda s: s['startLocal'], reverse=True)
print(json.dumps(sessions, indent=2, ensure_ascii=False))
