-- Query 2: Most efficient players who played at least 50 games
SELECT
    player_name,
    team,
    games_played,
    points_pg,
    ts_pct
FROM player_stats
WHERE games_played >= 50
ORDER BY ts_pct DESC
LIMIT 10;