def Vowels(Value):
    String = ['a','e','i','o','u']
    for i in String:

        if Value == i:
            print("This is a vowel")
        else:
            print("This is not a vowel")
    
    
    
def main():
    Value = (input("Enter the character :"))
    Ret=Vowels(Value)
    print(Ret)
    # if Value == Ret:
    #     print("this is a vowel")
    # else:
    #     print("Not a vowel")

if __name__ =="__main__":
    main()