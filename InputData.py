# InputData
from operations import operations

def inputData():
    s = list(input("Input  "))    
    functions = tuple("+-*/%")
    num = list()
    fun = list()
    text = list()
    
    for i in range(len(s)):
        if s[i].isdigit(): 
            if fun :
                if len(num)== len(fun):
                    num.append(s[i])
                else:
                    num[len(fun)] = num[len(fun)]+s[i]
            else:
                if num :
                    num[0] = num[0]+s[i]
                else:
                    num.append(s[i])               
        elif s[i] in functions:
            fun.append(s[i])
        else:
            text.append(s[i])               
        i += 1
        
    res = operations( num, fun )
    print("resalt =", res)
    
