import json
import os
import glob
from datetime import datetime, timezone, timedelta

def main():
    base_paths = [
        os.path.expandvars(r"%USERPROFILE%\.gemini\tmp\arun-creagy\chats"),
        os.path.expandvars(r"%USERPROFILE%\.gemini\antigravity-cli\brain")
    ]

    latest_jsonl = None
    for base_path in base_paths:
        if os.path.exists(base_path):
            # Sort all jsonl files recursively by modified time
            jsonls = sorted(glob.glob(os.path.join(base_path, "**", "*.jsonl"), recursive=True), key=os.path.getmtime, reverse=True)
            if jsonls:
                latest_jsonl = jsonls[0]
                break

    if not latest_jsonl:
        print("No session directories found.")
        return

    tz = timezone(timedelta(hours=7))
    with open(latest_jsonl, encoding='utf-8') as f:
        for line in f:
            try:
                m = json.loads(line)
                # Match both antigravity-cli and older formats
                if m.get("type") in ("user", "USER_INPUT") or m.get("source") == "USER_EXPLICIT":
                    ts = m.get("timestamp", "")
                    content = str(m.get("content", ""))[:80].replace('\n', ' ')
                    if ts:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(tz)
                        print(f"{dt.strftime('%Y-%m-%d %H:%M')} | {content}")
            except Exception:
                pass

if __name__ == "__main__":
    main()
