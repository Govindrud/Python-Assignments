def NumberCount(No):
    #length = len(No)
    sum = 0 
    for i in No:
        sum = sum + int(i)
    return sum

def main():
    No = (input("Enter the No :"))
    ret = (NumberCount(No))
    print(ret)

main()