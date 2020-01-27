#Есть список из 5 чисел: [3, 6, 9, 12, 15],отобразить каждый
#элемент, удвоив его с помощью функции for loop in range():
#Element Index[ 0 ] Previous Value  3 Now  6
#Element Index[ 1 ] Previous Value  6 Now  12
#Element Index[ 2 ] Previous Value  9 Now  18
#Element Index[ 3 ] Previous Value  12 Now  24
#Element Index[ 4 ] Previous Value  15 Now  30

lis = [3,6,9,12,15]
for i in range(len(lis)):
    lis[i] = int(lis[i])*2
    print("Element Index[ "+str(i)+" ] Previous Value "+str(lis[i])+"  Now "+str(int(lis[i])*2))
  
