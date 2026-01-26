def Factorial(Value):
    Ans =1
    for i in range(1,(Value+1)):
        Ans = Ans * i 
        
    return Ans    
    
def main():
    Value = int(input("Enter the value : "))
    Ret= Factorial(Value)
    print(f"Factorial of the {Value} is :",Ret)
    

if __name__ == "__main__":
    main()