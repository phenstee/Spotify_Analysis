import pandas as pd
from pathlib import Path

# Raw data folder
raw_folder = Path("data_raw")

# Find all JSON files
json_files = list(raw_folder.glob("*.json"))

print("Found files")
for file in json_files:
    print(f"- {file.name}")
