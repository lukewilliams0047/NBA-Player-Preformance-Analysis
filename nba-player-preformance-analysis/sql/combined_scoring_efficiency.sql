
WITH eligible_players AS (
    SELECT
        player_name,
        team,
        games_played,
        points_pg,
        ts_pct,
        PERCENT_RANK() OVER (
            ORDER BY points_pg
        ) AS scoring_rank,
        PERCENT_RANK() OVER (
            ORDER BY ts_pct
        ) AS efficiency_rank
    FROM player_stats
    WHERE games_played >= 50
      AND points_pg IS NOT NULL
      AND ts_pct IS NOT NULL
)
SELECT
    player_name,
    team,
    games_played,
    ROUND(points_pg, 2) AS points_per_game,
    ROUND(ts_pct * 100, 1) AS true_shooting_pct,
    ROUND(
        (scoring_rank + efficiency_rank) / 2.0,
        3
    ) AS combined_score
FROM eligible_players
ORDER BY combined_score DESC
LIMIT 10;
