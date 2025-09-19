import pandas as pd
import matplotlib.pyplot as plt

# Load Fitness/Gym Progress Tracker Excel file
df = pd.read_excel("Fitness_Gym_Progress_Tracker.xlsx")

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_excel("Cleaned_Fitness_Gym_Progress_Tracker.xlsx", index=False)
print("\n✅ Cleaned dataset saved as 'Cleaned_Fitness_Gym_Progress_Tracker.xlsx'")

# Key insights
print("\nAverage Workout Duration (minutes):", df['duration_minutes'].mean())
print("Maximum Calories Burned in a Session:", df['calories_burned'].max())
print("\nAverage Weight per Member:\n", df.groupby('name')['weight_kg'].mean())
print("\nWorkout Counts per Exercise:\n", df['exercise'].value_counts())
print("\nSessions Longer than 90 Minutes:\n", df[df['duration_minutes'] > 90])

# Charts
# 1. Bar chart - Number of Workouts per Exercise
df['exercise'].value_counts().plot(kind='bar', color="skyblue", edgecolor="black", figsize=(8,5))
plt.title("Number of Workouts per Exercise")
plt.xlabel("Exercise")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart_exercises.png")
plt.close()

# 2. Pie chart - Goal distribution
df['goal'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap="tab20", figsize=(6,6))
plt.title("Fitness Goal Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart_goals.png")
plt.close()

# 3. Histogram - Calories burned distribution
df['calories_burned'].plot(kind='hist', bins=10, color="lightgreen", edgecolor="black", figsize=(8,5))
plt.title("Calories Burned Distribution")
plt.xlabel("Calories Burned")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_calories.png")
plt.close()

print("\n✅ Charts saved as: bar_chart_exercises.png, pie_chart_goals.png, histogram_calories.png")
