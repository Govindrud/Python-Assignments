

def Min(Numbers):
    Min_No =Numbers[0]
    for n in Numbers:
        if n < Min_No: 
            Min_No = n
    return Min_No

def main():
    Size = int(input("Enter the Number of Elements :"))
    Numbers = list()
    
    for i in range(Size):
        value = int(input("Enter the Numbers :"))
        Numbers.append(value)
    print(Numbers)
    Minimum  = Min(Numbers)
    print("Minimum of the elements from list is :",Minimum)

main()

    
