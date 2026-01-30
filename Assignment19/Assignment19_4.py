from functools import reduce

Even = lambda A :  (A % 2 ==0) 
Square = lambda A : (A *A)

Addition = lambda A,B : A + B

def main():
    #S = [4,34,36,76,68,24,89,23,86,90,45,70]
    Data = list()
    Numbers = int(input("Enter the Elements : "))
    for i in range(Numbers):
        Values = int(input("Enter the Numbers : "))
        Data.append(Values) 
    #print(Data)
   
    NewList = list(filter(Even,Data))
    print(NewList)

    NewList1 = list(map(Square,NewList))
    print(NewList1)

    NewList2 = reduce(Addition ,NewList1 )
    print(NewList2)


main()