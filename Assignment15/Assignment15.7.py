from functools import reduce

GreaterString = lambda A : len(A) > 5 

def main():
    Size = int (input("Enter the Number of Words to check : "))
    Data = list()

    for i in range(Size):
        Strings =input("Enter the word : ")
        Data.append(Strings)
    print(Data)

    Stringarray = list(filter(GreaterString,Data))
    print("Greatest String is : ",Stringarray)

main()
    

