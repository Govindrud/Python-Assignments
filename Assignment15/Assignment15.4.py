from functools import reduce 
#Reduce 
Add = lambda A,B : A + B

def main():
    
    size = int(input("Enter the Number of Elements : "))
    
    Data = list()
    
    for i in range(size):
        No= int(input("Enter the Number :"))
        #B= int(input("Enter the Number :"))
        
        Data.append(No)
    RData = reduce(Add,Data)
    print(RData)


main()