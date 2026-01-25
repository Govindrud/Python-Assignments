from functools import reduce 
#Reduce 
Maximum_Element = lambda A,B :A if  (A > B) else B

def main():
    
    size = int(input("Enter the Number of Elements : "))
    
    Data = list()
    
    for i in range(size):
        No= int(input("Enter the Number :"))
        #B= int(input("Enter the Number :"))
        
        Data.append(No)
    RData = reduce(Maximum_Element,Data)
    print(Data)
    print("Maximum Number is : ",RData)


main()