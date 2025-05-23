import pandas as pd

df = pd.read_csv("ipl_data_2024\ipl_deliveries_2024.csv")

dismissal_types = ['caught', 'run out', 'stumped']

# Group by fielder and dismissal_kind
summary = df.groupby(['fielder', 'dismissal_kind']).size().unstack(fill_value=0)

# Ensure all dismissal types are included as columns
for dtype in dismissal_types:
    if dtype not in summary.columns:
        summary[dtype] = 0

# Reorder columns
summary = summary[dismissal_types]

# Reset index to get 'fielder' as a column
summary = summary.reset_index()

# Optionally save to a CSV
summary.to_csv('dismissal_summary_by_fielder.csv', index=False)