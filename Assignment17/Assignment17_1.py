import Arithmatic

No1 = 0
No2 = 0

def main():
    
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the Second Number :"))

    Ret =Arithmatic.Add(No1,No2)
    print ("Addition is :",Ret)
    Ret =Arithmatic.Sub(No1,No2)
    print ("Substraction is :",Ret)
    Ret =Arithmatic.Mult(No1,No2)
    print ("Multiplication is :",Ret)

    Ret =Arithmatic.Div(No1,No2)
    print ("Division is :",Ret)

if __name__ == "__main__":
    main()