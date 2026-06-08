import json
import sys
from datetime import datetime, timezone, timedelta

def main():
    f_path = r'C:\Users\sitth\.gemini\tmp\arun-creagy\chats\session-2026-06-08T19-04-d635439f.jsonl'
    tz = timezone(timedelta(hours=7))
    try:
        with open(f_path, encoding='utf-8') as f:
            for line in f:
                try:
                    m = json.loads(line)
                    if m.get('type') == 'user':
                        ts_str = m['timestamp'].replace('Z', '+00:00')
                        dt = datetime.fromisoformat(ts_str).astimezone(tz)
                        print(f"{dt.strftime('%Y-%m-%d %H:%M')} | {m['content'][:80]}")
                except (json.JSONDecodeError, KeyError) as e:
                    continue
    except FileNotFoundError:
        print(f"File not found: {f_path}")

if __name__ == "__main__":
    main()
