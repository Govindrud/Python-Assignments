def Maths(Number1,Number2):
    print("Addition is: ",Number1 + Number2)
    print("Sunstraction:", Number1 - Number2)
    print("Multiplication is: ",Number1 * Number2)
    print("Division is :",Number1 / Number2)
    

        
def main():
    Number1 = int(input("Enter the Number1 :"))
    Number2 = int(input("Enter the Number2 :"))
    Ret=Maths(Number1,Number2)
    print("Calculations of the Numbers are  : ",Ret)

if __name__ =="__main__":
    main()