# Mane
from Errors import Errors
from InputData import InputData
from Operations import Operations

def main():    
    print("Cut Calculator by Pyton")
    a = InputData("Firs")
    o = InputData("Operation")
    b = InputData("Second")
    Operations(a,b,o)
if __name__=="__main__" :
    main()


