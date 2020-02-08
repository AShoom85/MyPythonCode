#Напишите программу управления списком кортежей в телефонном справочнике.
#Программа должна выводить список записей, добавлять новую запись, удалять
#и редактировать существующую запись.



"""
lis = [" idn "," name "," telNumber "," birthday "]
lis1 = [" 1 "," Vasya "," 0955676556 "," 24.08.1970 "]
lis2 = [" 2 "," Olga "," 0993763490 "," 12.10.2010 "]"""


with open("listMain.txt","r") as file:
    lisMain = file.read().splitlines()    
 
idn = str(len(lisMain))
name = input(" input name ")
telNumber = input(" input tel number ")
birthday = input(" input birthday (dd.mm.yyyy)")
lisAdd = [" "+ idn +" "," "+ name +" "," "+ telNumber +" "," "+ birthday +" "]
print("    ")
lisMain.append(lisAdd)
with open("listMain.txt","w") as lism:
    for i in range(len(lisMain)):
        lism.write("%s\n" % lisMain[i])
print("    ")        
with open("listMain.txt","r") as lism:
    print(lism.read())
print("    ")

with open("listMain.txt","r") as file:
   lisMain = file.read().splitlist()
    
print(lisMain)
print(type(lisMain))
"""   
lisTrans =[[k[i] for k in lisMain] for i in range(len(lisMain[0]))]
for i in range(len(lisTrans)):
    print(lisTrans[i])
"""


