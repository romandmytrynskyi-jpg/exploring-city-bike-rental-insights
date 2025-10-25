This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
day.csv
fs_report.md
main.py
````

# Files

## File: day.csv
````
instant,dteday,season,yr,mnth,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered,cnt
1,2011-01-01,1,0,1,0,6,0,2,0.344167,0.363625,0.805833,0.160446,331,654,985
2,2011-01-02,1,0,1,0,0,0,2,0.363478,0.353739,0.696087,0.248539,131,670,801
````

## File: main.py
````
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("day.csv")

# Your code starts here

# Map season numbers to names for readability
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
df['season_name'] = df['season'].map(season_mapping)

# 1. Average number of rentals per season
season_avg = df.groupby('season_name')['cnt'].mean().reset_index()
print("Average total rentals per season:")
print(season_avg)

# Bar chart of average rentals by season
plt.figure(figsize=(8,5))
sns.barplot(data=season_avg, x='season_name', y='cnt', palette='viridis')
plt.title("Average Total Bike Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Average Rentals")
plt.tight_layout()
plt.show()

# Identify seasons with highest and lowest average rentals
max_season = season_avg.loc[season_avg['cnt'].idxmax()]
min_season = season_avg.loc[season_avg['cnt'].idxmin()]
print(f"Highest average rentals: {max_season['season_name']} ({max_season['cnt']:.1f})")
print(f"Lowest average rentals: {min_season['season_name']} ({min_season['cnt']:.1f})")

# 2. Average casual and registered users per season
user_avg = df.groupby('season_name')[['casual', 'registered']].mean().reset_index()
print("\nAverage casual and registered users per season:")
print(user_avg)

# 3. Ratio of casual to registered per season
user_avg['casual_to_registered'] = user_avg['casual'] / user_avg['registered']
print("\nCasual to registered ratio per season:")
print(user_avg[['season_name', 'casual_to_registered']])

highest_ratio = user_avg.loc[user_avg['casual_to_registered'].idxmax()]
print(f"Season with highest casual-to-registered ratio: {highest_ratio['season_name']} ({highest_ratio['casual_to_registered']:.2f})")

# 4. Average rentals on holidays only, by season
holiday_avg = df[df['holiday'] == 1].groupby('season_name')['cnt'].mean().reset_index()
print("\nAverage rentals on holidays by season:")
print(holiday_avg)````
