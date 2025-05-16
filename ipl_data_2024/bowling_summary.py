import pandas as pd

# Load the dataset
df = pd.read_csv("ipl_data_2024\ipl_deliveries_2024.csv")

# Clean 'extras_type' column
df['extras_type'] = df['extras_type'].fillna('').str.strip().str.lower()

# Add 'is_legal' column
df['is_legal'] = ~df['extras_type'].isin(['wides', 'no_balls'])

# Sort for safety
df = df.sort_values(by=['match_id', 'bowling_team', 'over', 'ball'])

# Runs Conceded by Bowler (Exclude byes and legbyes)
# Runs not caused by 'byes' or 'legbyes' are considered bowler's runs
bowler_runs_df = df[~df['extras_type'].isin(['byes', 'legbyes'])]
bowler_runs = bowler_runs_df.groupby(['match_id', 'bowling_team', 'bowler'])['total_runs'].sum().reset_index(name='runs')

# Legal Deliveries & Overs
legal_df = df[df['is_legal']]
legal_counts = legal_df.groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='legal_deliveries')
legal_counts['overs'] = legal_counts['legal_deliveries'] // 6 + (legal_counts['legal_deliveries'] % 6) / 10

# Wickets (Exclude run outs)
valid_wickets = df[
    df['dismissal_kind'].notna() & (df['dismissal_kind'].str.lower() != 'run out')
]
wickets = valid_wickets.groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='wickets')

# Dot balls (0s) from legal deliveries only
dot_balls = legal_df[legal_df['total_runs'] == 0].groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='0s')

# Fours and Sixes
fours = df[df['batsman_runs'] == 4].groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='4s')
sixes = df[df['batsman_runs'] == 6].groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='6s')

# Wide and No Balls
wides = df[df['extras_type'] == 'wides'].groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='no_of_wides')
no_balls = df[df['extras_type'] == 'no_balls'].groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='no_of_no_balls')

# Maiden Overs: Legal overs with 0 total_runs
over_runs = legal_df.groupby(['match_id', 'bowling_team', 'bowler', 'over'])['total_runs'].sum().reset_index()
maiden_overs = over_runs[over_runs['total_runs'] == 0]
maidens = maiden_overs.groupby(['match_id', 'bowling_team', 'bowler']).size().reset_index(name='maidens')

# Merge all metrics
summary = legal_counts.merge(bowler_runs, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(wickets, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(dot_balls, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(fours, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(sixes, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(wides, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(no_balls, on=['match_id', 'bowling_team', 'bowler'], how='left') \
                      .merge(maidens, on=['match_id', 'bowling_team', 'bowler'], how='left')

# Fill NaNs
for col in ['runs', 'wickets', '0s', '4s', '6s', 'extra_runs', 'no_of_wides', 'no_of_no_balls', 'maidens']:
    summary[col] = summary[col].fillna(0).astype(int)

# Economy Rate = (Runs / Overs) * 6
summary['economy'] = round((summary['runs'] / summary['legal_deliveries']) * 6, 2)

# Add 'match' column
match_lookup = df.groupby('match_id')['batting_team'].first().reset_index(name='opponent_team')
summary = summary.merge(match_lookup, on='match_id', how='left')
summary['match'] = summary['bowling_team'] + " vs " + summary['opponent_team']
summary.drop(columns=['opponent_team'], inplace=True)

# Reorder Columns
summary = summary[['match_id', 'bowling_team', 'bowler', 'overs', 'maidens',
                   'runs', 'wickets', 'economy', '0s', '4s', '6s',
                   'no_of_wides', 'no_of_no_balls', 'match']]

# Save to CSV
summary.to_csv("bowling_summary.csv", index=False)
print("Saved as bowling_summary.csv")
