import threading
import time


def Even(Data):
    even =list()
    sum =0
    for i in Data:
        if (i > 1) and (i % 2 ==0):
            even.append(i)
    print(even)
    for i in even:
        sum = sum + i

    print(sum)


def Odd(Data):
    odd = list()
    sum =0
    for i in Data:
        if (i >= 1) and (i % 2 != 0):
            odd.append(i)
        
    print(odd)
    for i in odd:
        sum = sum + i

    print(sum)

def main():
    Data = list()
    Number = 0
    for i in range(1,21):
        Data.append(i)
    # print(Data)
    t1 = threading.Thread(target=Even,args=(Data,))
    t2 = threading.Thread(target=Odd,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

main()



