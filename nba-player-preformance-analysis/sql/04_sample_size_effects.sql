-- Query 4: Examine efficiency rankings without a games threshold
SELECT
    player_name,
    team,
    games_played,
    field_goal_attempts,
    free_throw_attempts,
    points_pg,
    ts_pct
FROM player_stats
ORDER BY ts_pct DESC
LIMIT 10;