
def NuturalNumberSum(Value):
    Ans =0
    for i in range(1,(Value+1)):
        Ans = Ans + i 
        
    return Ans    
    
def main():
    Value = int(input("Enter the value : "))
    Ret= NuturalNumberSum(Value)
    print("Sum of Natural Numbers is :",Ret)
    

if __name__ == "__main__":
    main()