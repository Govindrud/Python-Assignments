def Digit(Value):
    Ans =0
    for digit in Value:
        Ans =len(Value)
           
    return Ans

def main():
    Value = (input("Enter the Number :"))
    Ret=Digit(Value)
    print("Digit Count is : ",Ret)

if __name__ =="__main__":
    main()
