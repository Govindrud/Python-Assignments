from functools import reduce

Product = lambda A,B : A * B

def main():
    Size = int (input("Enter the Number to Entries : "))
    Data = list()

    for i in range(Size):
        No =int(input("Enter the Number : "))
        Data.append(No)
    print(Data)

    Numbers = reduce(Product,Data)
    print("Product of Numbers are : ",Numbers)

main()
    

