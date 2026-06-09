import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=7))
f_path = r'C:\Users\sitth\.gemini\tmp\arun-creagy\chats\session-2026-06-09T07-36-0e7aab14.jsonl'

with open(f_path, encoding='utf-8') as f:
    for line in f:
        try:
            m = json.loads(line)
            if m.get('type') == 'user':
                ts = datetime.fromisoformat(m['timestamp'].replace('Z', '+00:00')).astimezone(tz)
                print(f"{ts.strftime('%Y-%m-%d %H:%M')} | {m['content'][:80]}")
        except Exception:
            pass
