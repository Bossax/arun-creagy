import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=7))
f_path = r'C:\Users\sitth\.gemini\tmp\arun-creagy\chats\session-2026-06-18T15-51-b5bedec0.jsonl'

with open(f_path, encoding='utf-8') as f:
    for line in f:
        try:
            m = json.loads(line)
            if m.get('type') == 'user':
                ts_str = m['timestamp'].replace('Z', '+00:00')
                ts = datetime.fromisoformat(ts_str).astimezone(tz)
                content = str(m.get('content', ''))[:80].replace('\n', ' ')
                print(f"{ts.strftime('%Y-%m-%d %H:%M')} | {content}")
        except Exception as e:
            pass
