# IPL 2024 Best XI Selection

This project identifies the best performing players of IPL 2024 using detailed match and delivery data. The goal is to suggest an optimal playing XI for IPL 2025 based on batting and bowling performances using data analytics and visualization.

## 📊 Tools Used
- Python (Pandas)
- Power BI
- VS Code (for preprocessing and analysis)

## 📁 Dataset

This project uses the [IPL Complete Dataset (2008–2020) by Patrick B](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) on Kaggle. The original dataset includes:

- `matches.csv`: Contains match-level information (match ID, teams, venue, date, result, etc.).
- `deliveries.csv`: Ball-by-ball details for each match (batsman, bowler, runs, extras, dismissals, etc.).

For this project, IPL data has been extended to include seasons up to 2024.

We filter matches and deliveries for the 2024 season to analyze player performance and recommend the best XI for IPL 2025.


## 🔍 Project Workflow

1. **Data Filtering**  
   - Extract matches from the year 2024 using `datetime` column from `matches.csv`.
   - Get corresponding `match_id`s and filter `deliveries.csv` for those matches.

2. **Performance Analysis**
   - Create batting and bowling summaries using `groupby()` and aggregation in Pandas.
   - Calculate key performance metrics (e.g., runs, strike rate, economy, wickets).

3. **Best XI Selection**
   - Analyze top performers based on roles.
   - Visualize insights using Power BI dashboards.
   - Select the most balanced team for IPL 2025.

## 📸 Power BI Visuals
> Add screenshots here 

## 🏏 Final Team - Best XI for IPL 2025
> (List the selected 11 players here once finalized)

