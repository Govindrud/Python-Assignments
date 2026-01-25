Even = lambda No : (No % 2==0)


def main():
    No = int(input("Enter the Number :"))

    Ret = Even(No)
    if Ret == True:
        print(f"{No} is a Even Number")
    else:
        print(f"{No} is a Odd Number")

main()
