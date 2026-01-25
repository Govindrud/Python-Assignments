

Maxiumum = lambda No1,No2 : No1 > No2 


def main():
    No1 = int (input("Enter the Number 1 : "))
    No2 = int(input("Enter the Number 2: "))
    Maxiumum(No1,No2)

    Ret = Maxiumum(No1,No2)
    if Ret == True:
        print(f"{No1} is greater ")
    else:
        print(f"{No2} is greater")




if __name__ =="__main__":
    main()