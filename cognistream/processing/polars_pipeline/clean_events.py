"""
clean_events.py

Removes invalid events before they are stored in ClickHouse.
"""


def clean_events(events):
    """
    Remove events that don't contain all required fields.
    """

    required_fields = [
        "event_id",
        "developer",
        "event_type",
        "timestamp"
    ]

    cleaned_events = []

    for event in events:
        if all(field in event for field in required_fields):
            cleaned_events.append(event)

    return cleaned_events


if __name__ == "__main__":

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

    result = clean_events(sample_events)

    print(result)
    