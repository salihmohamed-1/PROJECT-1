def clean_events(events):
    """
    Remove invalid events before storing them.
    """

    required_fields = [
        "event_id",
        "developer",
        "event_type",
        "timestamp"
    ]

    cleaned_events = []

    for event in events:

        # Check all required fields exist
        if not all(field in event for field in required_fields):
            continue

        # Check values are not empty
        if not event["developer"].strip():
            continue

        if not event["event_type"].strip():
            continue

        if not event["timestamp"].strip():
            continue

        cleaned_events.append(event)

    return cleaned_events