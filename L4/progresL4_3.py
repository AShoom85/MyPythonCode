# Напечатать шаблон
 
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

for i in range(5):
    n = i + 1
    print(str(n)*n)

    
for num in range(10):
    for i in range(num):
        print(num,end=" ")
    print("\n")     
