
def DivisibleBy(Value1):
    if (Value1 % 3 ==0) and (Value1 % 5==0):
        print("The number is divisible by 3 & 5")
    else:
        print("Not divisible by 3 & 5")

    
     


def main():
    Value1=int(input("Enter a number "))
    DivisibleBy(Value1)


    


if __name__ == "__main__":
    main()