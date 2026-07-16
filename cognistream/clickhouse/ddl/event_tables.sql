-- Create database
CREATE DATABASE IF NOT EXISTS cognistream;

USE cognistream;

-- Main developer events table
CREATE TABLE developer_events (
    event_id UUID,
    developer_id String,
    event_source String,
    event_type String,
    event_time DateTime
)
ENGINE = MergeTree()
ORDER BY (developer_id, event_time);

-- GitHub events table
CREATE TABLE github_events (
    event_id UUID,
    developer_id String,
    repository String,
    branch String,
    commit_message String,
    event_time DateTime
)
ENGINE = MergeTree()
ORDER BY (developer_id, event_time);

-- Slack events table
CREATE TABLE slack_events (
    event_id UUID,
    developer_id String,
    channel String,
    message String,
    event_time DateTime
)
ENGINE = MergeTree()
ORDER BY (developer_id, event_time);

-- IDE activity table
CREATE TABLE ide_events (
    event_id UUID,
    developer_id String,
    file_name String,
    activity_type String,
    duration UInt32,
    event_time DateTime
)
ENGINE = MergeTree()
ORDER BY (developer_id, event_time);