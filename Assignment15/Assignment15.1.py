Square = lambda No : (No * No)

def main():
    
    size = int(input("Enter the Number of Elements : "))
    

    Data = list()
    

    for i in range(size):
        No  = int(input("Enter the Number :"))
        
        Data.append(No)
    MData = list(map(Square,Data))
    print(MData)


main()