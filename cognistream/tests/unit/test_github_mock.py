import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from ingestion.mock_apis.github_mock import get_github_events


def test_github_mock():
    events = get_github_events()

    assert isinstance(events, list)
    assert len(events) == 10

    for event in events:
        assert "developer" in event
        assert "repository" in event
        assert "event_type" in event
        assert "timestamp" in event

    print("✅ GitHub Mock API Test Passed!")


if __name__ == "__main__":
    test_github_mock()