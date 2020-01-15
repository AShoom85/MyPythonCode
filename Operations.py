# Operations

from Errors import Errors  


def Operations(a,b,o):
    if o == "+" :
        print ("!!!Result!!!     "+ str(a)+" + "+str(b)+" = "+str(a+b))
    elif o == "-":
        print ("!!!Result!!!     "+ str(a)+" - "+str(b)+" = "+str(a-b))
    elif o == "*":
        print ("!!!Result!!!     "+ str(a)+" * "+str(b)+" = "+str(a*b))
    elif o == "/" and b == 0 or o == "//" and b == 0 or o == "%" and b == 0:
        Errors(1)       
    elif o == "/" and b != 0:
        print ("!!!Result!!!     "+ str(a)+" / "+str(b)+" = "+str(a/b))
    elif o == "//" and b != 0:
        print ("!!!Result!!!     "+ str(a)+" // "+str(b)+" = "+str(a//b))
    elif o == "%" and b != 0:
        print ("!!!Result!!!     "+ str(a)+" % "+str(b)+" = "+str(a%b))
