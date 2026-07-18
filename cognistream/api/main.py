from fastapi import FastAPI
from cognistream.ingestion.mock_apis.github_mock import get_github_events

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