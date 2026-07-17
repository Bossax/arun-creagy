import json
import os
from datetime import datetime, timezone, timedelta

def main():
    base_paths = [
        os.path.expandvars(r"%USERPROFILE%\.gemini\tmp\arun-creagy\chats"),
        os.path.expandvars(r"%USERPROFILE%\.gemini\antigravity-cli\brain")
    ]

    all_jsonls = []
    for base_path in base_paths:
        if os.path.exists(base_path):
            # Use os.walk to guarantee traversing dot-directories like .system_generated
            for root, dirs, files in os.walk(base_path):
                for f in files:
                    if f.endswith('.jsonl'):
                        all_jsonls.append(os.path.join(root, f))

    if not all_jsonls:
        print("No session directories found.")
        return

    # Find the newest file across all search directories
    latest_jsonl = max(all_jsonls, key=os.path.getmtime)

    tz = timezone(timedelta(hours=7))
    with open(latest_jsonl, encoding='utf-8') as f:
        for line in f:
            try:
                m = json.loads(line)
                # Match both antigravity-cli and older formats
                if m.get("type") in ("user", "USER_INPUT") or m.get("source") == "USER_EXPLICIT":
                    ts = m.get("timestamp") or m.get("created_at") or ""
                    content = str(m.get("content", ""))[:80].replace('\n', ' ')
                    if ts:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(tz)
                        print(f"{dt.strftime('%Y-%m-%d %H:%M')} | {content}")
            except Exception:
                pass

if __name__ == "__main__":
    main()
