import threading
import time
import os


def Small(Name):
    count = 0
    print("Inside Small function:",threading.get_ident()) 
    for i in Name:
        if i.islower():
            count = count + 1
    print("1.Small coint is  ",count)


def Capital(Name):
    count = 0
    print("Inside Capital function:",threading.get_ident()) 
     
    for i in (Name):
        if i.isupper():
            count = count + 1
    
    print("2.Capital count is  ",count)


def Digit(Name):
    count = 0
    print("Inside Digit function:",threading.get_ident()) 
    for i in (Name):
        if i.isdigit():
            count = count + 1
    print("3.Digits count is  ",count)


def main():

    String = input("Enter the String :")
    print(String)

    t1 = threading.Thread(target=Small, args=(String,))
    
    t2 = threading.Thread(target=Capital, args=(String,))

    t3 = threading.Thread(target=Digit , args=(String,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()

