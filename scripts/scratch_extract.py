import json, os
from datetime import datetime, timezone, timedelta

def main():
    tz = timezone(timedelta(hours=7))
    
    # Try current session transcript.jsonl
    session_transcript = r"C:\Users\sitth\.gemini\antigravity-cli\brain\96fe5d5c-f01f-4f3d-9e0b-dc38e9de9cc1\.system_generated\logs\transcript.jsonl"
    if os.path.exists(session_transcript):
        latest_jsonl = session_transcript
    else:
        # Fallback to the chat folder
        chats_dir = os.path.expandvars(r"$USERPROFILE\.gemini\tmp\arun-creagy\chats")
        if not os.path.exists(chats_dir):
            print("No chat folder found.")
            return
        items = [os.path.join(chats_dir, x) for x in os.listdir(chats_dir)]
        if not items: 
            print("No items in chat folder.")
            return
        items.sort(key=os.path.getmtime, reverse=True)
        project_base = items[0]
        if os.path.isdir(project_base):
            jsonl_files = [os.path.join(project_base, x) for x in os.listdir(project_base) if x.endswith('.jsonl')]
        elif project_base.endswith('.jsonl'):
            jsonl_files = [project_base]
        else:
            jsonl_files = []
        if not jsonl_files: 
            print("No jsonl files found.")
            return
        jsonl_files.sort(key=os.path.getmtime, reverse=True)
        latest_jsonl = jsonl_files[0]
        
    print(f"Reading from: {latest_jsonl}")
    with open(latest_jsonl, encoding='utf-8') as f:
        for l in f:
            try:
                m = json.loads(l)
                if m.get('type') in ('USER_INPUT', 'user'):
                    ts = m.get('timestamp') or m.get('created_at')
                    if not ts: continue
                    ts = ts.replace('Z', '+00:00')
                    dt = datetime.fromisoformat(ts).astimezone(tz)
                    content = str(m.get('content', ''))
                    if '<USER_REQUEST>' in content:
                        content = content.split('<USER_REQUEST>')[1].split('</USER_REQUEST>')[0].strip()
                    content = content[:80].replace('\n', ' ')
                    print(f"{dt.strftime('%Y-%m-%d %H:%M')} | {content}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
