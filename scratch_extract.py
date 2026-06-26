import json, os
from datetime import datetime, timezone, timedelta
tz = timezone(timedelta(hours=7))
f_path = r'C:\Users\sitth\.gemini\tmp\arun-creagy\chats\598c4f60-a6a5-4b57-8369-08069878b4be\fa71319f-f38f-420a-b8fa-f0b006918d3d.jsonl'
with open(f_path, encoding='utf-8') as f:
    for l in f:
        m = json.loads(l)
        if m.get('type') == 'USER_INPUT':
            ts = m['timestamp'].replace('Z', '+00:00')
            dt = datetime.fromisoformat(ts).astimezone(tz)
            print(f"{dt.strftime('%Y-%m-%d %H:%M')} | {m['content'][:80].replace(chr(10), ' ')}")
