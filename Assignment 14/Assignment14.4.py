Minimum = lambda No1 , No2 : No1 < No2

def main():
    No1=int(input("Enter the Number 1 :"))
    No2=int (input("Enter the Number 2:"))

    Ret = Minimum(No1,No2)

    if Ret == True:
        print(f"{No1} is Minimum Number")
    else:
        print(f"{No2} is Minimum Number")

main()