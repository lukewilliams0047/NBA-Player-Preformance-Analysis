-- Query 3: Compare scoring volume and efficiency
SELECT
    player_name,
    team,
    games_played,
    points_pg,
    ts_pct
FROM player_stats
WHERE games_played >= 50
ORDER BY points_pg DESC
LIMIT 10;