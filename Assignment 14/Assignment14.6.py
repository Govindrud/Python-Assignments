Odd = lambda No : (No % 2 == 0)

def main():
    No = int(input("Enter the Number :"))

    Ret= Odd(No)

    if Ret== False:
        print(f"{No} is odd Number")
    else:
        print(f"{No} is Even Number")

main()