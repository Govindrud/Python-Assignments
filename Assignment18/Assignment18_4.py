

def Freq(Numbers , Freq_Search):
    count = 0
    for n in Numbers:
        if n == Freq_Search: 
            count = count + 1
    return count

def main():
    Size = int(input("Enter the Number of Elements :"))
    Numbers = list()
    
    for i in range(Size):
        value = int(input("Enter the Numbers :"))
        Numbers.append(value)
    print(Numbers)
    Freq_Search = int(input("Enter the Element to search:"))
    ret  = Freq(Numbers , Freq_Search)
    print(f"Frequenecy of the {Freq_Search} from list is :",ret)

main()

    
