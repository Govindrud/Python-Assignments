def Number(No):
    return(No % 5 == 0)
       
def main():
    No = int(input("Enter the Number : "))
    print (Number(No))

main()