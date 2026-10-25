
import pandas as pd

file_path = "../data/2024-25-player-season-totals.csv"
df = pd.read_csv(file_path)

# Keep players who appeared in at least 50 games
qualified_players = df[df["games_played"] >= 50].copy()

# Rank each statistic from lowest to highest
qualified_players["ppg_rank"] = qualified_players["points_pg"].rank(pct=True)
qualified_players["ts_rank"] = qualified_players["ts_pct"].rank(pct=True)

# Give scoring volume and efficiency equal weight
qualified_players["combined_score"] = (
    qualified_players["ppg_rank"] + qualified_players["ts_rank"]
) / 2

# Display players with the highest combined scores
top_combined = qualified_players.sort_values(
    by="combined_score",
    ascending=False
)

print("Top 10 players combining scoring volume and efficiency:")
print(
    top_combined[
        ["player_name", "team", "games_played",
         "points_pg", "ts_pct", "combined_score"]
    ].head(10).round(3)
)
