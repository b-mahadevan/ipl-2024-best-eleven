# 🏏 IPL 2024 Best XI – A Data-Driven Recommendation System

This project analyzes IPL 2024 player performance data using Python, Pandas, Web Scraping, and Power BI to recommend the **Best Playing XI**. The selected team can then be compared against actual IPL 2025 performance to refine predictions and suggest the optimal team for IPL 2026.

---

## 🚀 Project Highlights

- ✅ Web Scraping IPL 2024 Squad Data
- ✅ Data Filtering & Performance Metric Analysis
- ✅ Power BI Dashboard & Best XI Visualization

---

## 🔧 Technologies Used

- Python (Pandas)
- Power BI
- Web Scraper Chrome Extension
- VS Code
- Excel (for minor edits)

---

## 📁 Datasets

- [IPL Complete Dataset (2008–2020) – Kaggle](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- ESPNcricinfo (for IPL 2024 squad scraping)

**Processed Files**:
- `ipl_matches_in_2024.csv`
- `ipl_deliveries_2024.csv`
- `batting_summary.csv`
- `bowling_summary.csv`
- `matches_summary.csv`
- `player_details_updated.csv`

---

## 🔍 Project Workflow

### ✅ Step 1: Web Scraping – Player Info

- Scraped 2024 team squads from ESPNcricinfo using a Chrome extension.
- Extracted: Player Name, Team, Role, Batting & Bowling Style.
- Cleaned and saved the initial data as `ipl_2024_player_summary.csv`.
- Then used Pandas to standardize player names to match the historical IPL dataset (matches.csv and deliveries.csv) and saved the updated dataset as `player_details_updated.csv`.

### ✅ Step 2: Data Filtering & Performance Analysis

- Filtered 2024 matches from `matches.csv`.
- Extracted corresponding delivery records from `deliveries.csv` using match_id of 2024 matches.
- Calculated batting and bowling metrics using Pandas:
  - **Batting**: Runs, Balls, Fours, Sixes, Strike Rate, Batting Position, and more.
  - **Bowling**: Overs, Runs Conceded, Wickets, Economy Rate, Dot Balls, and more.

### ✅ Step 3: Power BI Dashboard

- Built an interactive **Power BI dashboard** showing:
  - Best Openers
  - Best Anchors
  - Best Finishers
  - Best All-Rounders
  - Best Bowlers
  - Final Best Players
  - Final Team 11

---

# 📊 Power BI Dashboard
![Dashboard - Openers](https://github.com/b-mahadevan/ipl-2024-best-eleven/blob/main/ipl_2024_dashboard_pages/ipl_2024_dashboard_page-0001.jpg)  
![Dashboard - Anchors](https://github.com/b-mahadevan/ipl-2024-best-eleven/blob/main/ipl_2024_dashboard_pages/ipl_2024_dashboard_page-0002.jpg)  
![Dashboard Team 11](https://github.com/b-mahadevan/ipl-2024-best-eleven/blob/main/ipl_2024_dashboard_pages/ipl_2024_dashboard_page-0007.jpg)

---

# 📸 Additional Screenshots
![Dashboard - Finishers (Screenshot)](https://github.com/b-mahadevan/ipl-2024-best-eleven/blob/main/ipl_2024_dashboard_pages/ipl_2024_dashboard_page-0003_screenshot.png)
![Dashboard Team 11 (Screenshot)](https://github.com/b-mahadevan/ipl-2024-best-eleven/blob/main/ipl_2024_dashboard_pages/ipl_2024_dashboard_page-0007_screenshot.png)

---

## 🏏 Final Best XI – IPL 2024

| Player Name         | Role                | Team                        |
|---------------------|-------------------- |---------------------------- |
| 1. TM Head          | Wicketkeeper        | Sunrisers Hyderabad         |
| 2. V Kohli          | Top order Batter    | Royal Challengers Bengaluru |
| 3. R Parag          | Top order Batter    | Rajasthan Royals            |
| 4. SV Samson        | Wicketkeeper Batter	| Rajasthan Royals            |
| 5. RR Pant          | Wicketkeeper Batter	| Delhi Capitals              |
| 6. AD Russell       | Allrounder          | Kolkata Knight Riders       |
| 7. Arshad Khan      | Bowler              | Lucknow Super Giants        |
| 8. HH Pandya        | Allrounder          | Mumbai Indians              |
| 9. Swapnil Singh    | Bowler              | Royal Challengers Bengaluru |
| 10. CV Varun        | Bowler              | Kolkata Knight Riders       |
| 11. JJ Bumrah       | Bowler              | Mumbai Indians              |

---

## 📈 Future Scope

- After the conclusion of IPL 2025, perform the same data analysis on 2025 match and delivery data.
- Compare the 2024-based Best XI with the actual top performers of 2025.
- Analyze:
  ✅ Who delivered as expected?
  ❌ Who underperformed?
  🔁 Who should be replaced or retained?
- Based on this comparison, finalize a refined Best XI for IPL 2026 using updated performance insights.

---

## 🙏 Acknowledgments

- [Kaggle – IPL Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- [ESPNcricinfo](https://www.espncricinfo.com/)
- Power BI and Pandas documentation
- For educational and non-commercial use only.

---
