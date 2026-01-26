def ChkNum(Number):
    if (Number % 2 ==0):
        print("Even Number ")
    else:
        print(" Odd Number  ")

def main():
    Number = int(input("Enter the Number :"))
    ChkNum(Number)

if __name__ == "__main__":
    main()