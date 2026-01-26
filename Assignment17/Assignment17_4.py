def Factors(Number):
    sum =0
    for i in range(1 , Number):
        if (Number % i == 0) :
            sum = sum + i
    return sum
        
def main():
    Number = int(input("Enter the  Number :"))
    
    Ret=Factors(Number)

    print("Addition of factors   : ",Ret)
 

if __name__ =="__main__":
    main()