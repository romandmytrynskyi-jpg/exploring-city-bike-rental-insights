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
print(avg_holiday)