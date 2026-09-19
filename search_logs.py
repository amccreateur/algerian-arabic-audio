import json, os

log_dir = r"C:\Users\madan\.gemini\antigravity\brain\72f26899-5a78-4076-b737-cdd1328a1ef8\.system_generated\logs"
path = os.path.join(log_dir, "transcript.jsonl")

if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            obj = json.loads(line)
            content = str(obj.get("content", ""))
            thinking = str(obj.get("thinking", ""))
            text = content + " " + thinking
            if any(k in text.lower() for k in ["fajr", "فجر", "prière", "priere", "hamdan", "waqf", "voix", "algerian"]):
                source = obj.get("source", "")
                try:
                    print(f"Step {i} ({source}): {content[:160].encode('ascii', 'replace').decode('ascii')}")
                except Exception:
                    pass
