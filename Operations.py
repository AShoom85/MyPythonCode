# Operations

from errors import errors

def operations( num, fun ):
    if ("*" or "/" or "//" or "%") in fun :
            print ("*/")
    else:
        for i in range(len(fun)):
            if fun[i] == "-":
                num[0] = str(int(num[0]) - int(num[1]))
                del(num[1])
            elif fun[i] == "+":
                num[0] = str(int(num[0]) + int(num[1]))
                del(num[1])
    return (num)
