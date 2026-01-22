def Perfect(Number):
    sum =0
    for i in range(1 , Number):
        if (Number % i == 0) :
            sum = sum + i
    return sum
        
def main():
    Number = int(input("Enter the  Number :"))
    
    Ret=Perfect(Number)
    if Ret == Number:
        print(" Number is perfect Number   : ",Ret)
    else:
        print(f"{Number} is Not a perfect number")

if __name__ =="__main__":
    main()