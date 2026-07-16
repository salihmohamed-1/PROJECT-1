# ClickHouse Database Schema

## Database Name
cognistream

## Tables

### developer_events
Stores all developer events from different sources.

Columns:
- event_id (UUID)
- developer_id (String)
- event_source (String)
- event_type (String)
- event_time (DateTime)

---

### github_events

Stores GitHub activities.

Columns:
- event_id
- developer_id
- repository
- branch
- commit_message
- event_time

---

### slack_events

Stores Slack communication events.

Columns:
- event_id
- developer_id
- channel
- message
- event_time

---

### ide_events

Stores IDE coding activities.

Columns:
- event_id
- developer_id
- file_name
- activity_type
- duration
- event_time

---

## Storage Engine

MergeTree

## Sorting Key

(developer_id, event_time)