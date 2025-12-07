import json
import os
from datetime import datetime

DB_PATH = os.path.join("database", "opportunities.json")

def load_opportunities():
    if not os.path.exists(DB_PATH):
        return []

    with open(DB_PATH, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_opportunity(post, score, ai_reply):
    data = load_opportunities()

    entry = {
        "username": post["username"],
        "platform": post["platform"],
        "text": post["text"],
        "timestamp": post["timestamp"],
        "score": score,
        "ai_reply": ai_reply,
        "status": "pending",
        "saved_at": datetime.utcnow().isoformat()
    }

    data.append(entry)

    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def save_opportunities(all_data):
    with open(DB_PATH, "w") as f:
        json.dump(all_data, f, indent=4)
