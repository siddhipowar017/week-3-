#Day 6
# 1-Filtering
print("FILTERING:")

import pandas as pd
data = {
    "Name":["Babu","Sita","Siya","Riya"],
    "Age" :[20,21,22,19],
    "Marks":[80,75,65,85]
    }
df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nStudents with Marks > 70:")
print(df[df["Marks"]>70])

# 2-Sorting
print("\nSORTING:")

print("Data Sorted by Marks:")
print(df.sort_values("Marks",ascending=False))

# 3-GroupBy
print("\nGROUPBY:")

data = {
    "Name":["Babu","Sita","Siya","Riya"],
    "Course":["Python","Python","SQL","SQL"],
    "Marks":[80,75,65,85]
    }
df = pd.DataFrame(data)
print("Data:")
print(df)
print("\nAverage Marks by Course :\n")
print(df.groupby("Course")["Marks"].mean())

# 4-Summary Statistics
print("\nSUMMARY STATISTIC:\n")

print("Mean:",df["Marks"].mean())
print("Median:",df["Marks"].median())
print("Minimum:",df["Marks"].min())
print("Maximum:",df["Marks"].max())
    
            
