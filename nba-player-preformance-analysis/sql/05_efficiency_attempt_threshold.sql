-- Query 5: Efficiency leaders with at least 200 field-goal attempts
SELECT
    player_name,
    team,
    games_played,
    field_goal_attempts,
    free_throw_attempts,
    points_pg,
    ts_pct
FROM player_stats
WHERE field_goal_attempts >= 200
ORDER BY ts_pct DESC
LIMIT 10;