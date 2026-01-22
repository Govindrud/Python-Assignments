def Digit(Value):
    sum=0
    for i in Value:
        sum = sum + int(i)
    return sum
   

def main():
    Value = (input("Enter the Number :"))
    Ret=Digit(Value)
    print("Digit Count is : ",Ret)

if __name__ =="__main__":
    main()
