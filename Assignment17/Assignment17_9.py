def NumberCount(No):
    sum = 0
    for i in range(int(len(No))):
        sum = i
    return sum

def main():
    No =int(input("Enter the No :"))
    print(NumberCount(No))

main()