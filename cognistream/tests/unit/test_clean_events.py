import sys
import os

# Add the cognistream folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from processing.polars_pipeline.clean_events import clean_events


def test_clean_events():

    sample_events = [
        {
            "event_id": "101",
            "developer": "Salih",
            "event_type": "commit",
            "timestamp": "2026-07-17 10:30:00"
        },
        {
            "event_id": "102",
            "developer": "Meegadeesh"
        }
    ]

    cleaned = clean_events(sample_events)

    assert isinstance(cleaned, list)
    assert len(cleaned) == 1
    assert cleaned[0]["developer"] == "Salih"

    print("✅ Event Cleaning Test Passed!")


if __name__ == "__main__":
    test_clean_events()