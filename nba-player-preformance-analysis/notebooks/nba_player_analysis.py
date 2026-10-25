import csv
import os

# Find the project folder
project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Locate the CSV file
csv_path = os.path.join(
    project_folder,
    "data",
    "2024-25-player-season-totals.csv"
)

# Read the CSV data
with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Count the players/records
print("Total player records:", len(rows))

# Check for missing values in each column
print("\nMissing values by column:")

for column in reader.fieldnames:
    missing_count = 0

    for row in rows:
        if row[column] is None or row[column].strip() == "":
            missing_count += 1

    if missing_count > 0:
        print(column, ":", missing_count)
