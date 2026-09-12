# Day 4
# 1-Pandas series
print("PANDAS SERIES:\n")

import pandas as pd
Marks = pd.Series ([70,75,65,60,55,80,77],
                   index=["Ram","Sita","Shree","Sai","Siya","Babu","Raj"])

print("Marks  Series :")
print(Marks)

#2-Dataframe
print("\nDATAFRAME :\n")
import pandas as pd
Data ={
    "Name":["Babu","Sita","Riya","Siya"],
    "Age" :[18,20,25,21],
    "Marks":[80,75,85,90]
    }

df = pd.DataFrame(Data)
print(df)

#3-Read csv file
import pandas as pd

print("\nREAD CSV FILE:\n")

Data = {
    "Name": ["Babu", "Sita", "Riya", "Siya"],
    "Age": [18, 20, 25, 21],
    "Marks": [80, 75, 85, 90]
}

df = pd.DataFrame(Data)

df.to_csv("D:/students.csv", index=False)

print("CSV file created successfully!")

data_from_csv = pd.read_csv("D:/students.csv")

print("CSV DATA:")
print(data_from_csv)

#4-Shape, Columns & Data Types
print("\nSHAPE, COLUMNS & DATA TYPES:\n")
import pandas as pd
df = pd.read_csv("Student.csv")
print("shape :", df.shape)
print("Columns :", df.columns)
print("Data Types :")
print(df.dtypes)
