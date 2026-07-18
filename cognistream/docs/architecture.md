# CogniStream Architecture

## System Overview

CogniStream is a developer productivity analytics platform that collects engineering activity from multiple sources, processes the data, stores it in a database, and visualizes insights on a dashboard.

---

## Architecture Diagram

```
                GitHub Mock API
                       │
                       ▼
                Slack Mock API
                       │
                       ▼
             IDE Activity Mock API
                       │
                       ▼
             Event Processing Layer
                       │
                       ▼
                ClickHouse Database
                       │
                       ▼
                 FastAPI Backend
                       │
                       ▼
               React Dashboard
```

---

## Component Description

### 1. GitHub Mock API
Generates sample GitHub events such as commits, pull requests, merges, and issues.

### 2. Slack Mock API
Generates mock communication events between developers.

### 3. IDE Activity Mock API
Simulates coding sessions, file edits, and build activities.

### 4. Processing Layer
- Cleans incoming events.
- Removes invalid records.
- Calculates productivity metrics.

### 5. ClickHouse
Stores processed analytics events for fast querying.

### 6. FastAPI
Provides REST APIs for the frontend.

### 7. React Dashboard
Displays productivity metrics, charts, and summaries.

---

## Data Flow

1. Generate mock events.
2. Process and clean the events.
3. Store events in ClickHouse.
4. FastAPI reads the stored data.
5. React dashboard displays the analytics.

---

Architecture Document Completed ✅