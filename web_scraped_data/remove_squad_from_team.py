import pandas as pd

# Load the player summary file
players = pd.read_csv("web_scraped_data\ipl_2024_player_summary.csv")

# Remove ' Squad' from team names
players['team'] = players['team'].str.replace(" Squad", "", regex=False)

# Save to a new file
players.to_csv("players_summary_without_squad.csv", index=False)

print("Saved cleaned file as 'players_summary_without_squad.csv'")