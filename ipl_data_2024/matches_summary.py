import pandas as pd

# Load the matches 2024 dataset
matches_df = pd.read_csv("ipl_data_2024\ipl_matches_in_2024.csv")

# Drop unnecessary columns
columns_to_drop = ['player_of_match', 'toss_winner', 'toss_decision', 'target_runs', 
                   'target_overs', 'super_over', 'method', 'umpire1', 'umpire2']
matches_summary = matches_df.drop(columns=columns_to_drop, errors='ignore')

# Save the cleaned summary to a new CSV
matches_summary.to_csv("matches_summary.csv", index=False)

print("Saved as matches_summary.csv")
