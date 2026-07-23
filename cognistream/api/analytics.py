from pathlib import Path
import polars as pl

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "developer_events.csv"

def get_dashboard_metrics():
    df = pl.read_csv(CSV_PATH, try_parse_dates=True)

    df = df.filter(pl.col("developer").is_not_null())

    return {
        "developers": df["developer"].n_unique(),
        "commits": df.filter(pl.col("event") == "commit").height,
        "pull_requests": df.filter(pl.col("event") == "pull_request").height,
        "slack_messages": df.filter(pl.col("source") == "Slack").height,
        "ide_sessions": df.filter(pl.col("source") == "IDE").height,
        "total_events": df.height,
    }
def get_developer_metrics(developer_name):
    df = pl.read_csv(CSV_PATH, try_parse_dates=True)

    df = df.filter(pl.col("developer").is_not_null())

    summary = (
        df.group_by("developer")
        .agg([
            pl.len().alias("events"),
            (pl.col("event") == "commit").sum().alias("commits"),
            (pl.col("event") == "pull_request").sum().alias("pull_requests"),
            (pl.col("source") == "Slack").sum().alias("slack_messages"),
            (pl.col("source") == "IDE").sum().alias("ide_activity"),
            pl.col("duration_minutes").sum().alias("total_minutes"),
        ])
    )

    row = summary.filter(
    pl.col("developer").str.to_lowercase() == developer_name.lower()
)

    if row.height == 0:
        return {"error": "Developer not found"}

    result = row.to_dicts()[0]

    result["flow_score"] = round(
        result["total_minutes"] / (result["slack_messages"] + 1),
        2,
    )

    return result