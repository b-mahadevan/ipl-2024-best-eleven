import pandas as pd

# Load the files
players = pd.read_csv("web_scraped_data/players_summary_without_squad.csv")
batting = pd.read_csv("summarized_data/batting_summary.csv")
bowling = pd.read_csv("summarized_data/bowling_summary.csv")

# Function to extract last name
def get_last_name(name):
    if pd.isna(name):
        return ""
    return name.strip().split()[-1]

# Build a mapping: (last_name, team) -> full_name from batting
batting_map = {}
for _, row in batting.dropna(subset=['batter', 'inning']).iterrows():
    last = get_last_name(row['batter'])
    key = (last, row['inning'])
    if key not in batting_map:
        batting_map[key] = row['batter']

# Add mapping from bowling too
for _, row in bowling.dropna(subset=['bowler', 'bowling_team']).iterrows():
    last = get_last_name(row['bowler'])
    key = (last, row['bowling_team'])
    if key not in batting_map:
        batting_map[key] = row['bowler']

# Function to map player names in 'players' DataFrame
def find_changed_name(row):
    last_name = get_last_name(row['player_full_name'])
    team = row['team']
    return batting_map.get((last_name, team), None)

# Apply mapping
players['ChangedName'] = players.apply(find_changed_name, axis=1)

# Save result
players.to_csv("players_updated.csv", index=False)
print("Updated players file saved as 'players_updated.csv'")
