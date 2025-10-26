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

# Map season numbers to names
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
df["season_name"] = df["season"].map(season_mapping)

# 1. Average total rentals per season
avg_cnt = df.groupby("season_name")["cnt"].mean().reset_index()

# Print data values for plot
print("Average rentals per season (cnt):")
print(avg_cnt.to_dict(orient="list"))

# Bar chart of average rentals
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_cnt, x="season_name", y="cnt", order=["spring", "summer", "fall", "winter"])
plt.title("Average Bike Rentals per Season")
plt.xlabel("Season")
plt.ylabel("Average Count of Rentals")
plt.show()

# Identify seasons with highest and lowest average rentals
highest_season = avg_cnt.loc[avg_cnt["cnt"].idxmax(), "season_name"]
lowest_season = avg_cnt.loc[avg_cnt["cnt"].idxmin(), "season_name"]
print(f"Highest average rentals: {highest_season}")
print(f"Lowest average rentals: {lowest_season}")

# 2. Average casual and registered users per season
avg_users = df.groupby("season_name")[["casual", "registered"]].mean().reset_index()
print("Average casual and registered per season:")
print(avg_users)

# 3. Ratio of casual to registered users per season
avg_users["casual_registered_ratio"] = avg_users["casual"] / avg_users["registered"]
print("Casual to Registered ratio per season:")
print(avg_users[["season_name", "casual_registered_ratio"]])

# Season with highest ratio
highest_ratio_season = avg_users.loc[avg_users["casual_registered_ratio"].idxmax(), "season_name"]
print(f"Season with highest casual/registered ratio: {highest_ratio_season}")

# 4. Average rentals on holidays only, per season
avg_holiday = (
    df[df["holiday"] == 1]
    .groupby("season_name")["cnt"]
    .mean()
    .reset_index(name="avg_holiday_cnt")
)
print("Average holiday rentals per season:")
print(avg_holiday)````
