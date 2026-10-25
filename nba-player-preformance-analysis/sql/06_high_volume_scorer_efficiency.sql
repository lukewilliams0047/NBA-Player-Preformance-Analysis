-- Query 6: Efficiency among high-volume scorers
SELECT
    player_name,
    team,
    games_played,
    points_pg,
    ts_pct
FROM player_stats
WHERE games_played >= 50
  AND points_pg >= 25
ORDER BY ts_pct DESC;