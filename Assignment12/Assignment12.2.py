def Factor(Number):
    for i in range(1 , Number + 1):
        if (Number % i == 0):
            print(i)
        

    
   

def main():
    Number = int(input("Enter the Number :"))
    Ret=Factor(Number)
    #print("Digit Count is : ",Ret)

if __name__ =="__main__":
    main()