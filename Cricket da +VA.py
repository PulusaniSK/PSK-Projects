SELECT 
    match_id,
    date,
    opponent,
    toss_winner,
    winner,
    margin,
    venue
FROM cricket_matches
WHERE team_1 = 'India' OR team_2 = 'India';

-- Extract player performance data
SELECT 
    match_id,
    player_id,
    batting_runs,
    batting_balls,
    batting_fours,
    batting_sixes,
    bowling_overs,
    bowling_runs,
    bowling_wickets
FROM player_performances
WHERE player_id IN (SELECT player_id FROM players WHERE team = 'India');
```

**Python Code for Data Analysis and Visualization**:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed data
matches = pd.read_csv('cricket_matches.csv')
player_stats = pd.read_csv('player_performances.csv')

# Analyze team performance
win_rate = matches[matches['winner'] == 'India'].shape[0] / matches.shape[0]
print(f'India's win rate: {win_rate:.2%}')

# Analyze player performance
player_stats['batting_strike_rate'] = (player_stats['batting_runs'] / player_stats['batting_balls']) * 100
top_batters = player_stats.groupby('player_id')['batting_runs', 'batting_strike_rate'].mean().sort_values('batting_runs', ascending=False)
top_bowlers = player_stats.groupby('player_id')['bowling_wickets', 'bowling_economy'].mean().sort_values('bowling_wickets', ascending=False)

# Visualize the results
plt.figure(figsize=(12, 6))
top_batters['batting_runs'].head(10).plot(kind='bar')
plt.title('Top Indian Batters')
plt.xlabel('Player')
plt.ylabel('Batting Runs')
plt.show()

plt.figure(figsize=(12, 6))
top_bowlers['bowling_wickets'].head(10).plot(kind='bar')
plt.title('Top Indian Bowlers')
plt.xlabel('Player')
plt.ylabel('Bowling Wickets')
plt.show()
