#Напишите программу простого калькулятора,
#возвращающую результат sin, cos, log и sqrt.
import math


num = float(input(" Input number = "))
action = input("Input mathematical action (sin, cos, log or sqrt) - ")
actionList = ["sin", "cos", "log" , "sqrt"]
if action in actionList:
    if action == "sin" :
        num = math.sin(num)
        print (num)
    elif action == "cos" :
        num = math.cos(num)
        print (num)        
    elif action == "log" :
        num = math.log(num)
        print (num)
    elif action == "sqrt" :
        num = math.sqrt(num)
        print (num)              
else:
    print(" oops !!")
