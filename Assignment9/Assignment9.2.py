def ChkGreater(Value1,Value2):
    Value1=int(input("Enter First Number: "))
    Value2=int(input("Enter Second Number: "))
    if Value1>Value2:
        print(f"{Value1} is Greater")
    else:
        print(f"{Value2} is Greater")

def main():
    ChkGreater(Value1=0,Value2=0)

if __name__=="__main__":
    main()

