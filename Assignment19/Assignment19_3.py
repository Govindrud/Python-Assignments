from functools import reduce

GreaterNumber = lambda A :  (A >= 70) and (A <= 90)
Addition = lambda A : (A +10)

Product = lambda A,B : A * B

def main():
    #S = [4,34,36,76,68,24,89,23,86,90,45,70]
    Data = list()
    Numbers = int(input("Enter the Elements : "))
    for i in range(Numbers):
        Values = int(input("Enter the Numbers : "))
        Data.append(Values) 
    #print(Data)
   
    NewList = list(filter(GreaterNumber,Data))
    print(NewList)

    NewList1 = list(map(Addition,NewList))
    print(NewList1)

    NewList2 = reduce(Product ,NewList1 )
    print(NewList2)


main()