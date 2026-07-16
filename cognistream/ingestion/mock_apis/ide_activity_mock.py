import random
import uuid
import json
from datetime import datetime

developers = ["Salih", "Meegadeesh", "Anusha", "Member4"]

files = [
    "main.py",
    "dashboard.jsx",
    "event_tables.sql",
    "github_mock.py",
    "api.py"
]

activities = [
    "file_opened",
    "file_saved",
    "debug_started",
    "build_completed",
    "code_written"
]

def generate_ide_event():
    return {
        "event_id": str(uuid.uuid4()),
        "developer": random.choice(developers),
        "file_name": random.choice(files),
        "activity": random.choice(activities),
        "duration_minutes": random.randint(5, 120),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    events = [generate_ide_event() for _ in range(10)]
    print(json.dumps(events, indent=4))
    