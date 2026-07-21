from fastapi import FastAPI
from cognistream.ingestion.mock_apis.github_mock import get_github_events
from cognistream.ingestion.mock_apis.ide_activity_mock import generate_ide_event

app = FastAPI(
    title="CogniStream API",
    description="Developer Productivity Analytics Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CogniStream API",
        "status": "Running"
    }


@app.get("/github-events")
def github_events():
    return get_github_events()


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
@app.get("/dashboard")
def dashboard():

    github_events = get_github_events()

    ide_events = [generate_ide_event() for _ in range(10)]

    return {
        "total_commits": len(github_events),
        "pull_requests": 2,
        "slack_messages": 18,
        "ide_activity": len(ide_events)
    }