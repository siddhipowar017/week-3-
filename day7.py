# Day 7 - Mini Project
print("\n" + "*" * 50)
print("          DAY 7 - MINI PROJECT")
print("     EXPLORATORY DATA ANALYSIS")
print("*" * 50)
# Exploratory Data Analysis (EDA)

import pandas as pd
import numpy as np

# 1. Create Dataset
data = {
    "Name": ["Babu", "Sita", "Siya", "Riya", "Amit", "Neha", "Babu"],
    "Course": ["Python", "Python", "SQL", "SQL", "Python", "SQL", "Python"],
    "Age": [20, 21, 22, 19, 20, None, 20],
    "Marks": [80, 75, 65, 85, 90, 70, 80]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("Student_EDA.csv", index=False)

# Load CSV
df = pd.read_csv("Student_EDA.csv")

print("\n❖ DATASET ❖")
print(df)

# 2. Dataset Information
print("\n❖ SHAPE ❖")
print(df.shape)

print("\n❖ COLUMNS ❖")
print(df.columns)

print("\n❖ DATA TYPES ❖")
print(df.dtypes)

# 3. Missing Values
print("\n❖ MISSING VALUES ❖")
print(df.isnull().sum())

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean()).round().astype(int)

print("\n❖ AFTER FILLING MISSING AGE ❖")
print(df)

# 4. Remove Duplicate Rows
print("\n❖ DUPLICATES ❖")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\n❖ AFTER REMOVING DUPLICATES ❖")
print(df)

# 5. Filtering
print("\n❖ STUDENTS WITH MARKS > 75 ❖")
print(df[df["Marks"] > 75])

# 6. GroupBy
print("\n❖ AVERAGE MARKS BY COURSE ❖")
print(df.groupby("Course")["Marks"].mean())

# 7. Highest Marks
print("\n❖ STUDENT WITH HIGHEST MARKS ❖")
print(df.loc[df["Marks"].idxmax()])

# 8. Sorted
print("\n❖ STUDENTS SORTED BY MARKS ❖")
print(df.sort_values("Marks", ascending=False))

# 9. Summary Statistics
print("\n❖ SUMMARY STATISTICS ❖\n")

print("Mean:")
print(df["Marks"].mean())

print()
print("Median:")
print(df["Marks"].median())

print()
print("Minimum:")
print(df["Marks"].min())

print()
print("Maximum:")
print(df["Marks"].max())


# 10. NumPy Operation
print("\n❖ NUMPY OPERATION ❖\n")

print("Total Marks:")
print(np.sum(df["Marks"]))

print()
print("Average Marks:")
print(np.mean(df["Marks"]))

print()
print("Maximum Marks:")
print(np.max(df["Marks"]))

print()
print("Minimum Marks:")
print(np.min(df["Marks"]))

print()
print("Standard Deviation:")
print(np.std(df["Marks"]))

# 11. Final Findings
print("\n❖ FINDINGS ❖")

print("Python Average Marks:")
print(df[df["Course"] == "Python"]["Marks"].mean())

print("\nSQL Average Marks:")
print(df[df["Course"] == "SQL"]["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

#Key Insights
print("\n❖ KEY INSIGHTS ❖")

print("1. Python course has the highest average marks.")
print("2. Python students performed better than SQL students.")
print("3. The highest marks scored are 90.")
print("4. The lowest marks scored are 65.")
