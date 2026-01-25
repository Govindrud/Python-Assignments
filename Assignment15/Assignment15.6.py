from functools import reduce 
#Reduce 
Minimum_Number = lambda A ,B : A if (A < B) else B


def main():
    size = int(input("Enter the Number of Elements :"))
    Data =list()
    for i in range (size):
        No =int(input("Enter the Numbers : "))
        Data.append(No)
    print(Data)
    RData = reduce(Minimum_Number,Data)
    print("Minimum Number is :",RData)
    
main()