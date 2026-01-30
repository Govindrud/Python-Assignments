

def Addition(Numbers):
    sum =0
    for i in Numbers:
        sum = sum + i
    return sum

def main():
    Size = int(input("Enter the Number of Elements :"))
    Numbers = list()
    
    for i in range(Size):
        value = int(input("Enter the Numbers :"))
        Numbers.append(value)
    print(Numbers)
    Add = Addition(Numbers)
    print("Addition of the elements from list is :",Add)

main()

    
