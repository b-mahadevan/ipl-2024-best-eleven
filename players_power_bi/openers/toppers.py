import pandas as pd

df = pd.read_csv('players_power_bi\openers\data.csv')

for col in ['Runs', 'Batting SR', 'Batting AVG']:
    df[f'{col}_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Calculate composite performance score
df['Performance Score'] = df[['Runs_norm', 'Batting SR_norm', 'Batting AVG_norm']].mean(axis=1)

# Get top 2 performers
top_two = df.sort_values(by='Performance Score', ascending=False).head(2)

print(top_two[['Name', 'Team', 'Batting Position', 'Runs', 'Batting SR', 'Batting AVG', 'Performance Score']])