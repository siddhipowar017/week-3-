#Day 2 - Task

# 1-List
print("LIST")
Products = ["Laptop","Mouse", "Keyboard", "Monitor","USB Cable"]

print ("Products : ",Products)
print ("First product : ",Products[0])
print ("Third product : ",Products[2])

# 2-Dictionary
print("\nDICTIONARY ")
Student = {
    "Name" : "Sai",
    "Age" : 22,
    "City" : "Kagal",
    "Course" : "Data Analytics"
    }
print(Student)
print("Name   : ", Student["Name"])
print("Course : ", Student["Course"])

# 3-Tuple
print("\nTUPLE")
Numbers = (10,20,30,40,50,60,70)

print("Numbers : ", Numbers)
print("First Number : ", Numbers[0])
print("Last Number  : ", Numbers[4])


# 4 - All Loop Examples in One Program

print("\nFOR LOOP")
for i in range(1, 6):
    print(i)

print("\nWHILE LOOP")
i = 1
while i <= 5:
    print(i)
    i = i + 1

print("\nNESTED LOOP")
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

print("\nBREAK")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\nCONTINUE")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nPASS")
for i in range(1, 4):
    pass
print("Program Completed")
