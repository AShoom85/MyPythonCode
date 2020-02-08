

import csv


fileName = "users.csv"
users = [
    ["Name", "Age"],
    ["Tom", 28],
    ["Alis", 23],
    ["Bob", 34]
    ]
with open(fileName,"w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(fileName, "a", newline="") as file:
    user = ["Vasya",31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(fileName,"r", newline="") as file:
    reader = csv.reader(file)
    for i in reader:
        if i[0] == "Name":
            print(i[0], ":", i[1])
        else:    
            print(i[0], "- ", i[1])
print("\n","\n","\n")            
with open(fileName,"r", newline="") as file:
    reader = csv.reader(file)
    print(file.readline())

print("\n","\n","\n")            
with open(fileName,"r", newline="") as file:
    for i in range (0,5):
        print(file.readline())
    
