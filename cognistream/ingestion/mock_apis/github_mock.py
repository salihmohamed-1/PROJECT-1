import random
import uuid
import json
from datetime import datetime

developers = ["Salih", "Meegadeesh", "Anusha", "Member4"]

repositories = [
    "CogniStream",
    "Analytics",
    "Frontend"
]

event_types = [
    "commit",
    "pull_request",
    "issue",
    "merge"
]

commit_messages = [
    "Fixed login bug",
    "Added dashboard page",
    "Updated README",
    "Improved API performance",
    "Created new feature"
]


def generate_github_event():
    return {
        "event_id": str(uuid.uuid4()),
        "developer": random.choice(developers),
        "repository": random.choice(repositories),
        "event_type": random.choice(event_types),
        "commit_message": random.choice(commit_messages),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


if __name__ == "__main__":
    events = []

    for _ in range(10):
        events.append(generate_github_event())

    print(json.dumps(events, indent=4))