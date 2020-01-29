

lis = [" idn "," name "," telNumber "," birthday "]
lis1 = [" 1 "," Vasya "," 0955676556 "," 24.08.1970 "]
lis2 = [" 2 "," Olga "," 0993763490 "," 12.10.2010 "]
lisMain = [lis,lis1,lis2]
idn = str(len(lisMain)+1)

name = input(" input name ")
telNumber = input(" input tel number ")
birthday = input(" input birthday ")
lisAdd = [" "+ idn +" "," "+ name +" "," "+ telNumber +" "," "+ birthday +" "]

lisMain.append(lisAdd)
for i in range(len(lisMain)):
    print(lisMain[i])

print("    ")
lisTrans =[[k[i] for k in lisMain] for i in range(len(lisMain[0]))]
for i in range(len(lisTrans)):
    print(lisTrans[i])
