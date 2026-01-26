def NumberCount(No):
    sum = 0
    for i in range(len(No)):
        sum += int(No[i])
    return sum

def main():
    No =int(input("Enter the No :"))
    print(NumberCount(No))

main()