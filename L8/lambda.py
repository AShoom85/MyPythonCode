# Exercise 3
# список представляет собой базу данных.
# каждый элемент содержит сведения:
# имя
# возраст
# рост
# вес
# Пользователь может заказать сортировку по любому полю:
# a = [['tom',2,13,3], ['basil',11,15,5],['kity',9,14,4],['soly',4,12,2]]
# n = input('Сортировать по имени (1), возрасту (2), росту (3), весу (4): ')
# пользователь вводит номер поля. Число приводится к типу integer, и из него
# вычитается единица, т. к. индексация списка начинается с нуля.
# n = int(n)-1
# Далее определяется функция sort_cats(). Ей передается аргумент i, а она
# возвращает n-ый элемент этого аргумента. если этой функции передать
# вложенный список, то она вернет его n-й элемент.
# def sort_cats(i):
#     return i[n]
# a.sort(key=sort_cats)
# for i in a:
#    print("%7s %3d %4d %3d" % (i[0],i[1],i[2],i[3]))
# В функции sort() указывается пользовательская функция. Когда sort() извлекает
# очередной элемент списка, в данном случае - вложенный список, то передает
# этой функции.
# Элемент списка подменяется на то, что возвращает пользовательская функция.
# Если пользователь заказывает сортировку по второму столбцу, вывод будет таким:
# Сортировать по имени (1), возрасту (2), росту (3), весу (4): 2
#     tom   2   13   3
#    soly   4   12   2
#    kity   9   14   4
#   basil  11   15   5
# Переписать программу с использованием lambda-функции


a = [['tom',2,13,3], ['basil',11,15,5],['kity',9,14,4],['soly',4,12,2]]
n = int(input('Сортировать по имени (1), возрасту (2), росту (3), весу (4): '))-1
a.sort(key=lambda i: i[n])
for i in a:
    print("%7s %3d %4d %3d" % (i[0],i[1],i[2],i[3]))















    
