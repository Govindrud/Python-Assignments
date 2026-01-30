import MarvellousNum

def ListPrime(Number):

    S = MarvellousNum.ChkPrime(Number)
    print(S)
    Addition =0
    for num in S:
        Addition += num

    return Addition 
    
def main():
    Size = int(input("Enter the Number of Elements :"))
    Number = list()
    
    for i in range(Size):
        value = int(input("Enter the Numbers :"))

        Number.append(value)
    print(Number)
    #Freq_Search = int(input("Enter the Element to search:"))
    ret  = ListPrime(Number)
    print(f"Addition of prime no list is :",ret)

main()