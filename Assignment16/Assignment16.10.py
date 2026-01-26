def DisplayMain(Name):
    sum = 0
    for i in range((len(Name)+1)):
        sum = i
    return sum

def main():
    Name =input("Enter the Name :")
    print(DisplayMain(Name))

main()