# Есть csv file
# filename = "users.csv"
# прочитать csv file
# Извлечь заголовки полей из первой строки
# Извлечь данные начиная со 2-й строки
# Напечатать общее число строк
# Напечатать имена полей
# Напечатать первые 5 строк


import csv
filename = "users.csv"

'''
users = [
    ["Name", "Age"],
    ["Tom", 28],
    ["Alis", 23],
    ["Bob", 34],
    ["Yana", 20]
    ]
with open(filename,"w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(filename, "a", newline="") as file:
    user = ["Vasya",31]
    writer = csv.writer(file)
    writer.writerow(user)
    
with open(filename,"r", newline="") as file:
    reader = csv.reader(file)
    print ("field names are: ",file.readline())
    print("First 5 rows are:  ")
    for i in reader:
        print(i[0], "- ", i[1],)
'''


fields = []
rows = []
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    rows =[i for i in csvreader]
    print(f"\nTotal no. of rows: {csvreader.line_num}")
print("field names are: " + ",".join(i for i in fields))
print("\nFirst 5 rows are:  ")
for i in rows[:5]:
    for col in i:
        print("%23s"%col)
    print("\n")












    
