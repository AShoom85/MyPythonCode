# InputData

def InputData(v):
    if v == "O" or v == "o" or v == "Operation":
        x = input("Input operation = ")
    else:
        x = int(input("Input "+v+" data = "))
    return x
