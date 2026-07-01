import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=7))
f_path = r'C:\Users\sitth\.gemini\antigravity-cli\brain\785cdc97-20a5-4ba3-9816-9d96f81b0f7a\.system_generated\logs\transcript.jsonl'

with open(f_path, encoding='utf-8') as f:
    for line in f:
        try:
            m = json.loads(line)
            if m.get('type') == 'USER_INPUT':
                ts_str = m['created_at'].replace('Z', '+00:00')
                ts = datetime.fromisoformat(ts_str).astimezone(tz)
                content = str(m.get('content', ''))[:80].replace('\n', ' ')
                print(f"{ts.strftime('%Y-%m-%d %H:%M')} | {content}")
        except Exception as e:
            pass
