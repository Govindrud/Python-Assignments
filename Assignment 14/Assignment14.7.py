DivisibleBy5 = lambda No : (No % 5 ==0)

def main():
    No = int(input("Enter the Number :"))

    Ret = DivisibleBy5(No)

    if Ret == True:
        print(f"{No} is divisible by 5")
    else:
        print(f"{No} is Not Divisible by 5")

main()