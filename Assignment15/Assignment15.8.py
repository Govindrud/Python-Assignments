from functools import reduce

DivisibleNumbers = lambda A : (A % 3==0 ) and (A % 5 ==0)

def main():
    Size = int (input("Enter the Number to check : "))
    Data = list()

    for i in range(Size):
        No =int(input("Enter the Number : "))
        Data.append(No)
    print(Data)

    Numbers = list(filter(DivisibleNumbers,Data))
    print("Divisible Number are : ",Numbers)

main()
    

