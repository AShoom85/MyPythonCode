'''
def eratosthenes(n):     # n - число, до которого хотим найти простые числа 
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

    
num =[i for i in eratosthenes(50) if i !=0 ] 
    
        

print(num)

n = int(input())    # число, до которого хотим найти простые числа 
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0      
print(*list(filter(lambda x: x != 0, numbers)))    # выводим простые числа
print(*[i for i in numbers if i !=0 ])
'''

n = int(input("n = "))
lis = [i for i in range(n+1)]

for i in range(2,len(lis)) :
    if lis[i-2] != 0:
        
        print("i",i)
        for k in range(2,len(lis)):
            if lis[k-2] % lis[i-2] != 0 :
                print("lis",lis[k-2] % lis[i-2])
                lis[k-2] = 0
print(lis)                
