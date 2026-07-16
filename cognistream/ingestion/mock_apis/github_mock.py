import random
import uuid
from datetime import datetime, timedelta
import json

# Sample developers
developers = [
    "salih",
    "meegadeesh",
    "anusha",
    "member4"
]

# Sample repositories
repositories = [
    "cognistream",
    "analytics-engine",
    "frontend-dashboard"
]

# Sample branches
branches = [
    "main",
    "develop",
    "feature/login",
    "feature/dashboard",
    "bugfix/api"
]

# GitHub event types
event_types = [
    "commit",
    "pull_request",
    "merge",
    "branch_created",
    "issue_opened",
    "issue_closed"
]


def generate_event():
    """Generate one mock GitHub event."""

    event = {
        "event_id": str(uuid.uuid4()),
        "developer": random.choice(developers),
        "repository": random.choice(repositories),
        "branch": random.choice(branches),
        "event_type": random.choice(event_types),
        "commit_message": random.choice([
            "Fixed login bug",
            "Updated dashboard",
            "Added API endpoint",
            "Improved UI",
            "Refactored authentication",
            "Optimized database query",
            "Implemented feature"
        ]),
        "timestamp": (
            datetime.now() -
            timedelta(minutes=random.randint(1, 5000))
        ).strftime("%Y-%m-%d %H:%M:%S")
    }

    return event


def generate_events(count=10):
    """Generate multiple GitHub events."""

    events = []

    for _ in range(count):
        events.append(generate_event())

    return events


if __name__ == "__main__":

    github_events = generate_events(20)

    print(json.dumps(github_events, indent=4))