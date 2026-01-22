def EvenNumber(Value):
    a =list()
    for i in range(2,(Value+1),2):
        a.append(i)
        print(i)
    return a     
     

def main():
    Value = int(input("Enter the Number :"))
   
    Ret= EvenNumber(Value)
    print("The Even Numbers are :", Ret)

if __name__ == "__main__":
    main()
