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
- Then used Pandas to standardize player names to match the historical IPL dataset (matches.csv and deliveries.csv) and saved the updated dataset.

### ✅ Step 2: Data Filtering & Performance Analysis

- Filtered 2024 matches from `matches.csv`.
- Extracted corresponding delivery records from `deliveries.csv` using match_id of 2024 matches.
- Calculated batting and bowling metrics using Pandas:
  - **Batting**: Runs, Balls, Fours, Sixes, Strike Rate, Batting Position.
  - **Bowling**: Overs, Runs Conceded, Wickets, Economy Rate, Dot Balls.

### ✅ Step 3: Power BI Dashboard

- Built an interactive **Power BI dashboard** showing:
  - Best Openers
  - Best Anchors
  - Best Finishers
  - Best All-Rounders
  - Best Bowlers
  - Final Best Players
  - Final Team 11

📸 **Screenshots**:  
![Dashboard - Openers](https://github.com/yourusername/ipl-best-xi/blob/main/dashboard_images/ipl_2024_dashboard_page-0001.jpg)  
![Dashboard - Anchors](https://github.com/yourusername/ipl-best-xi/blob/main/dashboard_images/ipl_2024_dashboard_page-0002.jpg)  
![Dashboard - Finishers (Screenshot)](https://github.com/yourusername/ipl-best-xi/blob/main/dashboard_images/ipl_2024_dashboard_page-0007.jpg)
![Dashboard Team 11 (Screenshot)](https://github.com/yourusername/ipl-best-xi/blob/main/dashboard_images/ipl_2024_dashboard_page-0007.jpg)
![Dashboard Team 11](https://github.com/yourusername/ipl-best-xi/blob/main/dashboard_images/ipl_2024_dashboard_page-0007.jpg)

---

## 🏏 Final Best XI – IPL 2024

| Player Name         | Role           | Team            |
|---------------------|----------------|------------------|
| 1. Player A         | Batsman        | Team X           |
| 2. Player B         | Batsman        | Team Y           |
| 3. Player C         | All-Rounder    | Team Z           |
| 4. Player D         | Batsman        | Team A           |
| 5. Player E         | Wicket-Keeper  | Team B           |
| 6. Player F         | All-Rounder    | Team C           |
| 7. Player G         | Bowler         | Team D           |
| 8. Player H         | Bowler         | Team E           |
| 9. Player I         | Bowler         | Team F           |
| 10. Player J        | Bowler         | Team G           |
| 11. Player K        | Bowler         | Team H           |

> ⚠️ Replace placeholder names with your actual selections.

---

## 📈 Future Scope

- After IPL 2025, compare this Best XI with actual performance.
- Analyze:
  - Who delivered?
  - Who underperformed?
  - Suggestions for IPL 2026 Best XI.

---

## 🙏 Acknowledgments

- [Kaggle – IPL Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- [ESPNcricinfo](https://www.espncricinfo.com/)
- Power BI and Pandas documentation
- For educational and non-commercial use only.

