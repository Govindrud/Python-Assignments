def Loop(Number):
    for i in range(Number ,0,-1):
        
        print(i)
        

    
   

def main():
    Number = int(input("Enter the Number :"))
    Ret=Loop(Number)
    #print("Digit Count is : ",Ret)

if __name__ =="__main__":
    main()