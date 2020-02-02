# Exercise 3
# Задан словарь
# dic1 = {  "name":'Mary Ann',   "age":'22',   "phone":'1234567' }
# Напишите функцию записи словаря в файл
# Функция должна принимать в качестве параметра словарь
# Напишите функцию чтения словаря из файла
# Функция должна возвращать словарь из файла
# {'name': 'Mary Ann', 'age': '22', 'phone': '1234567'}
# <class 'dict'>

def addDict (dic):
    file = open("addDict.txt","w")
    file.write(str(dic))
    file.close

def outDict ():
    with open("addDict.txt","r")as file:
        res = file.readline()
    return eval(res)
    
dic1 = {  "name":'Mary Ann',   "age":'22',   "phone":'1234569' }
addDict(dic1)
print(outDict())
print(type(outDict()))
