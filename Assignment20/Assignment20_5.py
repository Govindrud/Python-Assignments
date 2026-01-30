import threading
import time
import os

count  = 0
lobj =threading.Lock() 

def Thread1(Num):
    count = 0
    Data = list()
    print("Inside Small function:",threading.get_ident()) 
    for i in range(1,51,1):
        
        with lobj:
            count = i
        Data.append(count)

    print("Thread1 count is  ",Data)
    print("Outside the Thread1")


def Thread2(Num):
    count = 0
    Data = list()
    print("Inside Capital function:",threading.get_ident()) 
     
    for i in range(50, 0 ,-1):
        
        count = i
        Data.append(count)
    
    print("Thread2 count is  ",Data)


def main():

    Num = 0
    #print(Num)

    t1 = threading.Thread(target=Thread1, args=(Num,))
    
    t2 = threading.Thread(target=Thread2, args=(Num,))
    t1.start()
    t1.join()

    t2.start()
    t2.join()
    

if __name__ == "__main__":
    main()

