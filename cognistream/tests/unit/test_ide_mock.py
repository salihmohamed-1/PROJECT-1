from ingestion.mock_apis.ide_activity_mock import generate_ide_event

def test_generate_ide_event():
    event = generate_ide_event()

    assert "developer" in event
    assert "activity" in event
    assert "timestamp" in event