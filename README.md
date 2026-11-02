# NBA Player Analysis

A Python and Streamlit project for exploring NBA player statistics. It allows users to filter player records by season, team and position, inspect numerical statistics and visualise their distributions.

I built this project to practise working with sports data using Pandas and to explore how statistical information can be presented through an interactive dashboard.

## What it does

- Loads NBA player statistics from a CSV dataset.
- Filters records by season or year, when the corresponding column is available.
- Allows selection of one or more teams.
- Filters players by playing position.
- Displays the filtered dataset in an interactive table.
- Lets users choose a numerical statistic to analyse.
- Generates histograms and box plots.
- Displays the average, median and maximum for the selected statistic.
- Allows filtered player data to be downloaded as a CSV file.

## Built with

- Python
- Streamlit
- Pandas
- Matplotlib

## Running the project

Clone the repository:

```bash
git clone <YOUR_NBA_REPOSITORY_URL>
cd <YOUR_NBA_REPOSITORY_FOLDER>
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Place `player_index.csv` in the same folder as `NBA.py`.

Run the application:

```bash
streamlit run NBA.py
```

## Dataset

The application reads its player statistics from:

```text
player_index.csv
```

The CSV file should contain player-level information, including numerical statistics and, for the corresponding filters, team, position and season/year information.

The application looks for recognised column names such as:

| Information | Recognised column names |
|---|---|
| Season | `SEASON`, `SEASON_YEAR`, `SEASON_ID`, `YEAR`, `SEASON_START_YEAR` |
| Team | `TEAM_ABBREVIATION`, `TEAM`, `TEAM_NAME` |
| Position | `POSITION`, `POS` |

Column matching is case-insensitive, and the application displays a message when an optional filter column is unavailable.

## Visualisations

Two chart types are currently available:

**Histogram**

Shows the frequency distribution of a selected numerical statistic.

**Box Plot**

Provides a quick view of the distribution, median and spread of the selected statistic.

The dashboard also calculates the average, median and maximum of the selected column.

## Project structure

```text
NBA-Player-Analysis/
│
├── NBA.py
├── player_index.csv
├── requirements.txt
└── README.md
```

## A note on the current version

The dashboard focuses on exploring and filtering player statistics. It does not currently calculate advanced basketball metrics, player efficiency ratings or predictive models.

There is plenty of room to extend it with player comparisons, team-level analysis, season-over-season trends and more detailed basketball statistics.

---

**Author:** [Neel Maniar](https://github.com/NeelManiar)

---
P.S. This is for educational purposes only. It was made after getting inspiration from a Streamlit tutorial offered by freeCodeCamp.
