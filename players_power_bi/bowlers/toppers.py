import pandas as pd

# Load the data
df = pd.read_csv('players_power_bi/bowlers/data.csv')


# Normalize key bowling metrics (lower is better for avg, eco, sr; higher is better for dot ball % and wickets)
df['wickets_norm'] = (df['wickets'] - df['wickets'].min()) / (df['wickets'].max() - df['wickets'].min())
df['eco_norm'] = 1 - (df['Economy'] - df['Economy'].min()) / (df['Economy'].max() - df['Economy'].min())
df['bowl_sr_norm'] = 1 - (df['Bowling Strike Rate'] - df['Bowling Strike Rate'].min()) / (df['Bowling Strike Rate'].max() - df['Bowling Strike Rate'].min())
df['avg_norm'] = 1 - (df['Bowling Average'] - df['Bowling Average'].min()) / (df['Bowling Average'].max() - df['Bowling Average'].min())
df['dot_pct_norm'] = (df['Dot ball %'] - df['Dot ball %'].min()) / (df['Dot ball %'].max() - df['Dot ball %'].min())

# Compute overall bowling score
df['bowler_score'] = df[['wickets_norm', 'eco_norm', 'bowl_sr_norm', 'avg_norm', 'dot_pct_norm']].mean(axis=1)

# Select top 2
top_bowlers = df.sort_values(by='bowler_score', ascending=False).head(2)

# Display results
print(top_bowlers[['player_name', 'team', 'wickets', 'Economy', 'Bowling Average', 'Bowling Strike Rate', 'Dot ball %', 'bowler_score']])
