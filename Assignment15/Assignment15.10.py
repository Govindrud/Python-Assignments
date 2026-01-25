from functools import reduce

EvenNo = lambda A : (A % 2 ==0)

def main():
    Size = int (input("Enter the Number to Entries : "))
    Data = list()

    for i in range(Size):
        No =int(input("Enter the Number : "))
        Data.append(No)
    print(Data)

    Numbers = list(filter((EvenNo),Data))
    print("Product of Numbers are : ",Numbers)

main()
    

