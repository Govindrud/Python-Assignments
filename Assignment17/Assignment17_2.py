def AstrikPattern(No):
    for i in range(No):
        print(" * " * No)
       
        # for j in range(No):
        #     print("*")


def main():
    No =int(input("Enter the Number : "))
    AstrikPattern(No)

if __name__ == "__main__":
    main()