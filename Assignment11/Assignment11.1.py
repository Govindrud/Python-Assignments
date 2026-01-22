def PrimeNumber(Value):
    if Value > 1:
        for i in range(2,Value):


         if Value % i==0:
            print("The value is Not prime Number")
            break
        else:
            print("The Value is Prime Number")

def main():
    Value = int(input("Enter the Value :"))
    PrimeNumber(Value)

if __name__ =="__main__":
    main()
