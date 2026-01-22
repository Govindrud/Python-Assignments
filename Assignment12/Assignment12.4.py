def Loop(Number):
    for i in range(1 , Number + 1):
        
        print(i)
    return
        

    
   

def main():
    Number = int(input("Enter the Number :"))
    Ret=Loop(Number)
    #print("Digit Count is : ",Ret)

if __name__ =="__main__":
    main()