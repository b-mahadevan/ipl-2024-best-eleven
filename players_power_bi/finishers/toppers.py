import pandas as pd

# Load the data
df = pd.read_csv('players_power_bi/finishers/data.csv')

# Normalize relevant metrics (higher is better for all these)
df['bat_avg_norm'] = (df['Batting Avg'] - df['Batting Avg'].min()) / (df['Batting Avg'].max() - df['Batting Avg'].min())
df['strike_rate_norm'] = (df['Strike rate'] - df['Strike rate'].min()) / (df['Strike rate'].max() - df['Strike rate'].min())
df['balls_faced_norm'] = (df['Avg. balls Faced'] - df['Avg. balls Faced'].min()) / (df['Avg. balls Faced'].max() - df['Avg. balls Faced'].min())
df['boundary_pct_norm'] = (df['Boundary %'] - df['Boundary %'].min()) / (df['Boundary %'].max() - df['Boundary %'].min())

# Final finisher score
df['finisher_score'] = df[['bat_avg_norm', 'strike_rate_norm', 'balls_faced_norm', 'boundary_pct_norm']].mean(axis=1)

# Top 2 finishers
top_finishers = df.sort_values(by='finisher_score', ascending=False).head(2)

# Display the results
print(top_finishers[['player_name', 'team', 'Total Runs', 'Batting Avg', 'Strike rate', 'Avg. balls Faced', 'Boundary %', 'finisher_score']])
