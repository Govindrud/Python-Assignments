def Palindrome(Value):
    DigitCounts = list(Value)

    Str =""

    for i in range ((len(DigitCounts)-1),-1,-1):
        Str = Str + DigitCounts[i]
    print("Reversed digits are : ",Str)
    return Str

    
def main():
    Value = (input("Enter the Number :"))
    Ret=Palindrome(Value)
    if Value == Ret:
        print("this is a palindrome")
    else:
        print("Not a Palindrome")

if __name__ =="__main__":
    main()