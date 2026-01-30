

def Max(Numbers):
    Max_No =Numbers[0]
    for n in Numbers:
        if n > Max_No: 
            Max_No = n
    return Max_No

def main():
    Size = int(input("Enter the Number of Elements :"))
    Numbers = list()
    
    for i in range(Size):
        value = int(input("Enter the Numbers :"))
        Numbers.append(value)
    print(Numbers)
    Maxiumum  = Max(Numbers)
    print("Maximum of the elements from list is :",Maxiumum)

main()

    
