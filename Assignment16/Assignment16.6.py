def Number(No):
    if (No == 0):
        print("Zero")
    elif(No < 0):
        print("Negative Number")
    else :
        print("Positive NUmber")

def main():
    No = int(input("Enter the Number : "))
    Number(No)

main()