#Day 5
# 1-Missing Values
print("MISSING VALUES:")

import pandas as pd
data = {
    "Name":["Sita","Babu","Siya"],
    "Age" :[20, None, 21],
    "Marks":[80,75,None]
    }
df = pd.DataFrame(data)

print("Data:")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())

# 2-Duplicates
print("\nDUPLICATE:")

import pandas as pd
data = {
    "Name": ["Babu","Sita","Babu","Siya"],
    "Age" : [20,21,20,22],
    "Marks" :[80,75,80,85]
    }
df = pd.DataFrame(data)

print("Data:")
print(df)
print("\nDuplicate Rows:")
print(df.duplicated())


# 3-Data Types Conversion
print("\nDATA TYPES CONVERSION:\n")

import pandas as pd
data = {
    "Name":["Babu","Sita","Siya","Riya"],
    "Age":["20","21","22","19"],
    "Marks":[80,70,75,85]
    }
df = pd.DataFrame(data)

print("Before Conversion:")
print(df.dtypes)

df["Age"]= df["Age"].astype(int)
print("\nAfter Conversion:")
print(df.dtypes)

# 4-Rename Columns
print("\nRENAME COLUMNS:\n")
import pandas as pd
data = {
    "Name":["Babu","Sita","Siya","Riya"],
    "Age" :[20,21,22,19],
    "Marks":[80,75,70,65]
    }
df = pd.DataFrame(data)
print("Before Renaming:")
print(df.columns)

df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Student_Marks"
    }, inplace = True)
print("\nAfter Ranaming:")
print(df.columns)
