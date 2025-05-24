import pandas as pd

df = pd.read_csv('players_power_bi/all_rounders/data.csv')

df['bat_sr_norm'] = (df['Strike rate'] - df['Strike rate'].min()) / (df['Strike rate'].max() - df['Strike rate'].min())
df['bat_avg_norm'] = (df['Batting Avg'] - df['Batting Avg'].min()) / (df['Batting Avg'].max() - df['Batting Avg'].min())

# Normalize bowling metrics
# Wickets (higher better), Economy & Bowling Strike Rate (lower better)
df['wickets_norm'] = (df['wickets'] - df['wickets'].min()) / (df['wickets'].max() - df['wickets'].min())
df['eco_norm'] = 1 - (df['Economy'] - df['Economy'].min()) / (df['Economy'].max() - df['Economy'].min())
df['bowl_sr_norm'] = 1 - (df['Bowling Strike Rate'] - df['Bowling Strike Rate'].min()) / (df['Bowling Strike Rate'].max() - df['Bowling Strike Rate'].min())

# Final score: average of all metrics
df['allrounder_score'] = df[['bat_sr_norm', 'bat_avg_norm', 'wickets_norm', 'eco_norm', 'bowl_sr_norm']].mean(axis=1)

# Top 2 all-rounders
top_allrounders = df.sort_values(by='allrounder_score', ascending=False).head(2)

# Display results
print(top_allrounders[['player_name', 'team', 'Total Runs', 'wickets', 'Strike rate', 'Batting Avg', 'Economy', 'Bowling Strike Rate', 'allrounder_score']])