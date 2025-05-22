import pandas as pd

# Load the ipl matches.csv and deliveries.csv
df_matches = pd.read_csv('ipl_data_2008_to_2024\matches.csv')

df_deliveries = pd.read_csv('ipl_data_2008_to_2024\deliveries.csv')

# Get the columns as a list
column_names_matches = df_matches.columns.tolist()
column_names_deliveries = df_deliveries.columns.tolist()
print(column_names_matches)
print(column_names_deliveries)

# Convert date column to datetime dtype
df_matches['date'] = pd.to_datetime(df_matches['date'], errors='coerce')

# Filter df_matches rows
df_matches_2024 = df_matches[df_matches['date'].dt.year == 2024]

# Filter df_deliveries rows 
df_deliveries_2024 = df_deliveries[df_deliveries['match_id'].isin(df_matches_2024['id'])]

# Save the filtered version as separate csv
df_matches_2024.to_csv('ipl_matches_in_2024.csv', index=False)
df_deliveries_2024.to_csv('ipl_delieveries_2024.csv', index = False)




