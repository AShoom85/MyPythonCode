#Отсортировать список идентификаторов, представленных в виде строк.
#Каждый идентификатор представляет собой объединение идентификатора
#строки и числа.
#ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
#При сортировке этого списка с помощью встроенной функции sorted()
#по умолчанию используется лексикографический порядок, поскольку
#элементы в списке являются строками.
#print(sorted(ids)) #Lexicographic sort ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
#Выполнить сортировку так, чтобы сортировка использовала число, связанное
#с идентификатором:
#print(sorted_ids) # ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']


def listsep(lis):
    a = ['','']
    for i in range(len(lis)):
        for k in lis[i] :
            if k.isalpha():
                a[0] += k
            elif k.isdigit():
                a[1] += k
        lis[i] = a
        a = ['','']
    return lis    


#ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id1670','id454','5id','i4d']
ids = listsep([list(i) for i in ids])    
ids = [[i[0],int(i[1])] for i in ids]
ids.sort(key=lambda x: x[1])
ids = [i[0] + str(i[1]) for i in ids]
print(ids)

