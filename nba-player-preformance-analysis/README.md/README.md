# NBA Player Performance Analysis

## Overview

This project analyzes NBA player statistics from the 2024–25 season to investigate the relationship between scoring volume and scoring efficiency.

Using SQL and Python, I explored points per game (PPG), true shooting percentage (TS%), three-point shooting, and the effect of sample size on player rankings. I also developed a combined ranking to identify players who performed well in both scoring volume and efficiency.

## Research Question

Which NBA players combined high scoring volume with high scoring efficiency during the 2024–25 season?

## Tools and Technologies

- **SQL:** Data querying, filtering, sorting, and ranking
- **Python:** Data analysis and data validation
- **pandas:** Data loading, filtering, sorting, and summary statistics
- **SQLite:** Database storage and querying
- **Matplotlib:** Data visualization

## Dataset

The project uses a CSV dataset containing NBA player statistics for the 2024–25 season. The data was imported into a SQLite database for SQL analysis and loaded into pandas for further exploration.

The dataset contains 569 player records and 32 columns, including games played, points, rebounds, assists, field-goal attempts, three-point shooting, free throws, points per game, and true shooting percentage.

## Analysis Performed

- Ranked players by points per game.
- Identified players with high true shooting percentages.
- Compared scoring volume with scoring efficiency.
- Investigated how small sample sizes affect efficiency rankings.
- Applied minimum-games and field-goal-attempt thresholds.
- Compared recorded true shooting percentages with recalculated values.
- Created a combined ranking using percentile ranks for points per game and true shooting percentage.
- Used pandas to inspect the dataset, summarize numerical columns, filter records, and rank players.

## Visualizations

The project includes the following visualizations:

- `top_10_scorers.png` — compares the leading scorers by points per game.
- `ppg_vs_true_shooting.png` — explores the relationship between scoring volume and true shooting percentage.
- `three_point_vs_true_shooting.png` — explores the relationship between three-point shooting percentage and true shooting percentage.

## Key Findings

### Scoring Volume and Efficiency

Shai Gilgeous-Alexander led the dataset in scoring, averaging approximately 32.68 points per game. However, Nikola Jokić combined high scoring volume with a true shooting percentage of 66.3%, placing him first in the project's combined scoring-and-efficiency ranking.

### True Shooting Percentage

Jarrett Allen led the players who appeared in at least 50 games, recording a true shooting percentage of 72.4%. This analysis showed that highly efficient players are not necessarily the highest-volume scorers.

### Sample Size

Players with very few games or shooting attempts can produce unusually high efficiency percentages. Applying minimum-games and minimum-attempt thresholds helped make the rankings more meaningful.

### Combined Ranking

I created a combined score by averaging each qualifying player's percentile rank in points per game and true shooting percentage. Nikola Jokić ranked first with a combined score of approximately 0.976.

### Statistical Relationships

In the filtered sample used for one analysis, three-point percentage and true shooting percentage had a correlation of approximately 0.708. This indicates a positive linear association in that sample, but it does not establish that one statistic causes the other.

***Three-point shooting and scoring efficiency:** In the filtered sample of 234 players, three-point percentage and true shooting percentage had a Pearson correlation of **0.708**, indicating a strong positive linear association. This does not establish that higher three-point percentage causes higher true shooting percentage.

## Data Validation

I recalculated true shooting percentage using points, field-goal attempts, and free-throw attempts, then compared the results with the existing `ts_pct` column. The largest differences were approximately 0.05 percentage points, consistent with rounding in the original data.

## Limitations

- Minimum-games and minimum-attempt thresholds are analytical choices and can change the rankings.
- The dataset contains some missing values in columns such as player position, effective field-goal percentage, and turnover percentage.
- The combined ranking gives equal weight to scoring volume and efficiency; other weighting methods could produce different results.
- Correlation describes association, not causation.
- The analysis focuses on selected scoring statistics rather than every aspect of a player's contribution to team success.

## Project Structure

```text
nba-player-preformance-analysis/
├── data/
│   └── 2024-25-player-season-totals.csv
├── misc/
│   └── test_pandas_cvs.py
├── notebooks/
│   └── 02_nba_player_analysis.py
├── sql/
│   └── SQL analysis files
├── visualizations/
│   ├── top_10_scorers.png
│   ├── ppg_vs_true_shooting.png
│   └── three_point_vs_true_shooting.png
├── nba_stats.db
└── README.md
```
d
## Reproducing the Analysis

### Requirements

- Python 3
- pandas
- Matplotlib
- SQLite

### Steps

1. Clone or download this repository to your computer.
2. Install the Python libraries if needed:

   ```bash
   python3 -m pip install pandas matplotlib
   ```

3. Open the SQLite database, `nba_stats.db`, using a SQLite-compatible tool such as DB Browser for SQLite.
4. Open and run the SQL query files in the `sql/` directory.
5. Run the Python analysis script from the `notebooks/` directory. Make sure the script's relative paths point to the correct dataset and visualization folders.

The Python analysis script reads the dataset, analyzes player statistics, and generates visualizations in the `visualizations/` directory.
## Future Improvements

- Investigate additional relationships among player statistics.
- Explore regression models to examine statistical associations.
- Improve data validation and document the data source.
- Expand the analysis to include additional measures of player performance.
