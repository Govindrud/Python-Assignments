#Largest1 = lambda No1,No2 : No1 if  (No1>No2) else No2
#Largest = lambda Largest1,No3 :Largest1 if (Largest1 > No3) else No3
Large = lambda No1,No2,No3 : No1 if (No1 > No2)  else  (No2 if No2 > No3 else No3) 


def main():
    No1 = int(input("Enter the Number 1 :"))
    No2 = int(input("Enter the Number 2:"))
    No3 = int(input("Enter the Number 3:"))
    
    #Ret = Largest1(No1,No2)
    
    #Ret1= Largest(Ret,No3)
    Return = Large(No1,No2,No3)
    print(f"From {No1},{No2},{No3} largest number is ",Return)
    

main()