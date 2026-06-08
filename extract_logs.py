import json
from datetime import datetime, timezone, timedelta
tz = timezone(timedelta(hours=7))
f_path = r'C:\Users\sitth\.gemini\tmp\arun-creagy\chats\session-2026-06-05T07-11-4f0eb0c9.jsonl'
with open(f_path, encoding='utf-8') as f:
    for line in f:
        try:
            m = json.loads(line)
            if m.get('type') == 'user':
                ts = datetime.fromisoformat(m['timestamp'].replace('Z', '+00:00')).astimezone(tz).strftime('%Y-%m-%d %H:%M')
                content_raw = m.get('content', '')
                if isinstance(content_raw, list):
                    content = "".join([p.get('text', '') for p in content_raw if isinstance(p, dict)])
                else:
                    content = content_raw
                content = content[:80].replace('\n', ' ')
                print(f'{ts} | {content}')
        except Exception as e:
            continue