import pandas as pd
from pathlib import Path

# Raw data folder
raw_folder = Path("data_raw")

# Find all JSON files
json_files = list(raw_folder.glob("*.json"))

print("Found files")
for file in json_files:
    print(f"- {file.name}")


# Load and combine them into one df
dfs = []
for file in json_files:
    df = pd.read_json(file)
    dfs.append(df)

plays_raw = pd.concat(dfs, ignore_index=True)

print("\nrows:", len(plays_raw))
print("Columns:", list(plays_raw.columns))
print("\nFirst 5 rows: ")
print(plays_raw.head())
