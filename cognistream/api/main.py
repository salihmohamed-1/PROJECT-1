from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cognistream.ingestion.mock_apis.github_mock import get_github_events
from cognistream.ingestion.mock_apis.ide_activity_mock import generate_ide_event

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

    github_events = get_github_events()

    ide_events = [generate_ide_event() for _ in range(10)]

    return {
        "total_commits": len(github_events),
        "pull_requests": 2,
        "slack_messages": 18,
        "ide_activity": len(ide_events)
    }
@app.get("/developer/{name}")
def developer_dashboard(name: str):

    data = {
        "salih": {
            "developer": "Salih",
            "commits": 15,
            "pull_requests": 4,
            "slack_messages": 27,
            "ide_activity": 11,
            "flow_score": "High"
        },

        "meegadeesh": {
            "developer": "Meegadeesh",
            "commits": 12,
            "pull_requests": 3,
            "slack_messages": 19,
            "ide_activity": 9,
            "flow_score": "Medium"
        }
    }

    return data.get(
        name.lower(),
        {"error": "Developer not found"}
    )