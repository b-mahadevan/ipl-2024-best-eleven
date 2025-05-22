import pandas as pd

# Load dataset
df = pd.read_csv("ipl_data_2024\ipl_deliveries_2024.csv")

# Clean 'extras_type' column
df['extras_type'] = df['extras_type'].fillna('').str.strip().str.lower()

# Filter out wides and no-balls
legal_df = df[~df['extras_type'].isin(['wides', 'noballs'])]

# Sort to reflect actual batting order
legal_df = legal_df.sort_values(by=['match_id', 'batting_team', 'over', 'ball'])

# Get Batting Position
first_balls = (
    legal_df.groupby(['match_id', 'batting_team', 'batter'])
    .first()
    .reset_index()
    .sort_values(by=['match_id', 'batting_team', 'over', 'ball'])
)

# Assign position: who faced first, second, etc.
first_balls['batting_position'] = first_balls.groupby(['match_id', 'batting_team']).cumcount() + 1

# Summarize stats
summary = legal_df.groupby(['match_id', 'inning', 'batter', 'batting_team', 'bowling_team']).agg(
    runs=('batsman_runs', 'sum'),
    balls=('batsman_runs', 'count'),
    fours=('batsman_runs', lambda x: (x == 4).sum()),
    sixes=('batsman_runs', lambda x: (x == 6).sum())
).reset_index()

# Merge Batting Position
summary = summary.merge(
    first_balls[['match_id', 'batting_team', 'batter', 'batting_position']],
    on=['match_id', 'batting_team', 'batter'],
    how='left'
)

# Add "out/not out" column
dismissals = legal_df[['match_id', 'inning', 'player_dismissed']].dropna()
dismissals = dismissals.rename(columns={'player_dismissed': 'batter'})
dismissals['out/not out'] = 'out'

summary = summary.merge(
    dismissals[['match_id', 'inning', 'batter', 'out/not out']],
    on=['match_id', 'inning', 'batter'],
    how='left'
)
summary['out/not out'] = summary['out/not out'].fillna('not out')

# Add Strike Rate
summary['SR'] = round((summary['runs'] / summary['balls']) * 100, 2)

# Add "match" column
summary['match'] = summary['batting_team'] + " vs " + summary['bowling_team']

# Replace inning number with team name
summary['inning'] = summary.apply(
    lambda row: row['batting_team'] if row['inning'] in [1, 2] else row['inning'],
    axis=1
)

# Drop unused columns
summary = summary.drop(columns=['batting_team', 'bowling_team'])

# Save to CSV
summary.to_csv("batting_summary.csv", index=False)
print("Saved as batting_summary.csv")
