from cognistream.api.analytics import get_developer_metrics
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cognistream.ingestion.mock_apis.github_mock import get_github_events
from cognistream.ingestion.mock_apis.ide_activity_mock import generate_ide_event
from cognistream.api.analytics import (
    get_developer_metrics,
    get_dashboard_metrics,
)
app = FastAPI(
    title="CogniStream API",
    description="Developer Productivity Analytics Platform",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    return get_dashboard_metrics()
@app.get("/developer/{name}")
def developer_dashboard(name: str):
    return get_developer_metrics(name)

    return data.get(
        name.lower(),
        {"error": "Developer not found"}
    )