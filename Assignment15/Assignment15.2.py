Even = lambda No : (No % 2==0)

def main():
    
    size = int(input("Enter the Number of Elements : "))
    

    Data = list()
    

    for i in range(size):
        No  = int(input("Enter the Number :"))
        
        Data.append(No)
    MData = list(filter(Even,Data))
    print(MData)


main()