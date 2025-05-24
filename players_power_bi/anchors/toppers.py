import pandas as pd

df = pd.read_csv('players_power_bi/anchors/data.csv')


# Normalize relevant metrics for anchors (all higher is better)
df['bat_avg_norm'] = (df['Batting Avg'] - df['Batting Avg'].min()) / (df['Batting Avg'].max() - df['Batting Avg'].min())
df['strike_rate_norm'] = (df['Strike rate'] - df['Strike rate'].min()) / (df['Strike rate'].max() - df['Strike rate'].min())
df['balls_faced_norm'] = (df['Avg. balls Faced'] - df['Avg. balls Faced'].min()) / (df['Avg. balls Faced'].max() - df['Avg. balls Faced'].min())
df['boundary_pct_norm'] = (df['Boundary %'] - df['Boundary %'].min()) / (df['Boundary %'].max() - df['Boundary %'].min())

# Final anchor score
df['anchor_score'] = df[['bat_avg_norm', 'strike_rate_norm', 'balls_faced_norm', 'boundary_pct_norm']].mean(axis=1)

# Top 2 anchors
top_anchors = df.sort_values(by='anchor_score', ascending=False).head(3)

# Display results
print(top_anchors[['player_name', 'team', 'Total Runs', 'Strike rate', 'Batting Avg', 'Avg. balls Faced', 'Boundary %', 'anchor_score']])
