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


def generate_events(count=10):
    events = []

    for _ in range(count):
        events.append(generate_github_event())

    return events


def get_github_events(count=10):
    """
    This function will be used by FastAPI later.
    """
    return generate_events(count)


if __name__ == "__main__":
    print(json.dumps(get_github_events(), indent=4))