
import csv
import os
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

# Find the project folder and CSV file
project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

csv_path = os.path.join(
    project_folder,
    "data",
    "2024-25-player-season-totals.csv"
)

# Create a folder for our charts if it doesn't exist
visualizations_folder = os.path.join(
    project_folder,
    "visualizations"
)
os.makedirs(visualizations_folder, exist_ok=True)

# Read the NBA player data
players = []

with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        games = int(float(row["games_played"]))
        points_per_game = float(row["points_pg"])

        # Keep players who played at least 50 games
        if games >= 50:
            players.append({
                "name": row["player_name"],
                "points_pg": points_per_game
            })

# Sort players from highest to lowest points per game
players.sort(
    key=lambda player: player["points_pg"],
    reverse=True
)

# Select the top 10 scorers
top_10 = players[:10]

names = [player["name"] for player in top_10]
points = [player["points_pg"] for player in top_10]

# Create the bar chart
plt.figure(figsize=(12, 7))
plt.bar(names, points)

plt.title("Top 10 NBA Scorers — 2024–25 Season")
plt.xlabel("Player")
plt.ylabel("Points Per Game")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart automatically
chart_path = os.path.join(
    visualizations_folder,
    "top_10_scorers.png"
)
plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print("Bar chart saved successfully!")
print("Saved to:", chart_path)

# Display the chart
plt.show()
 


# Connect to our NBA database
database_path = os.path.join(project_folder, "nba_stats.db")
connection = sqlite3.connect(database_path)

try:
    # Check that the expected table exists
    tables = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()
    print("Database tables:", tables)

    # Get three-point percentage and true shooting percentage
    query = """
    SELECT three_point_pct, ts_pct
    FROM player_stats
    WHERE games_played >= 50
        AND three_point_attempts >= 100
        AND three_point_pct IS NOT NULL
        AND ts_pct IS NOT NULL;
    """

    data = connection.execute(query).fetchall()

    # Separate the two statistics
    three_point_pct = [row[0] for row in data]
    true_shooting_pct = [row[1] for row in data]

    # Calculate Pearson correlation
    correlation = np.corrcoef(
        three_point_pct,
        true_shooting_pct
    )[0, 1]

    print("Number of players:", len(data))
    print("Correlation:", round(correlation, 3))
    
    # Create a scatter plot of three-point percentage vs. true shooting
    plt.figure(figsize=(10, 6))
    plt.scatter(three_point_pct, true_shooting_pct, alpha=0.7)

    plt.title("Three-Point Percentage vs. True Shooting Percentage")
    plt.xlabel("Three-Point Percentage")
    plt.ylabel("True Shooting Percentage")

    plt.tight_layout()

    chart_path = os.path.join(
        visualizations_folder,
        "three_point_vs_true_shooting.png"
    )
    plt.savefig(chart_path, dpi=300, bbox_inches="tight")
    plt.close()
    print("Three-point vs. true shooting scatter plot saved!")
    print("Saved to:", chart_path)

    print("Reached the end of the analysis!")

finally:
    connection.close()
