import json
import sys
import os

def extract_timestamps(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'user':
                    timestamp = data.get('timestamp', '')
                    # Format timestamp: YYYY-MM-DD HH:MM
                    if timestamp:
                        formatted_ts = timestamp.replace('T', ' ')[:16]
                    else:
                        formatted_ts = "Unknown"
                    
                    content_list = data.get('content', [])
                    text = ""
                    for item in content_list:
                        if 'text' in item:
                            text = item['text'].strip()
                            break
                    
                    snippet = text[:80].replace('\n', ' ')
                    print(f"{formatted_ts} | {snippet}")
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_timestamps(sys.argv[1])
    else:
        print("Usage: python extract_logs.py <path_to_jsonl>")
