import polars as pl

# Read CSV
df = pl.read_csv("../data/developer_events.csv")

print(df)

print("\nTotal Rows:", df.height)
print("Columns:", df.columns)