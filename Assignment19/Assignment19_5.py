from functools import reduce

prime = lambda A  : A > 1 and all (A % i !=0 for i in range (2,A))
Square = lambda A : (A *2)

Maximum = lambda A,B : A if A > B else B

def main():
    #S = [4,34,36,76,68,24,89,23,86,90,45,70]
    Data = list()
    Numbers = int(input("Enter the Elements : "))
    for i in range(Numbers):
        Values = int(input("Enter the Numbers : "))
        Data.append(Values) 
    #print(Data)
   
    NewList = list(filter(prime,Data))
    print(NewList)

    NewList1 = list(map(Square,NewList))
    print(NewList1)

    NewList2 = reduce(Maximum ,NewList1 )
    print(NewList2)


main()