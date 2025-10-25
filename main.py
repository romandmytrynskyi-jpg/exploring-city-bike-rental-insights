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
print(holiday_avg)