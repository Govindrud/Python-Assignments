def OddNumbers(Value):
    a =list()
    for i in range(1,(Value+1),2):
        a.append(i)
        print(i)

    return a 
     

def main():
    Value = int(input("Enter the Number :"))
    Ret= OddNumbers(Value)
    print("The Odd Number are :",Ret)
    

if __name__ == "__main__":
    main()
