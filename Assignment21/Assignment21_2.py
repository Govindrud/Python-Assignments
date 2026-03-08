import threading
import time

def Max(Numbers):
    max = Numbers[0]
    for i in range(len(Numbers)):
        if max < Numbers[i]:
            max = Numbers[i]
            
    print("Maximum Number is :", max) 


def Min(Numbers):
        min = Numbers[0]
        for i in Numbers:
             if min > i:
                 min = i
        print("Minimum Number is : ", min) 

def main():
    Value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    t1 = threading.Thread(target=Max , args=(Value,))
    t2 = threading.Thread(target=Min , args=(Value,))
    
    start_time = time.time()
    t1.start()
    t1.join()
    end_time = time.time()

    start_time2 = time.time()

    t2.start()
    t2.join()
    end_time2 = time.time()


    print("Start time:",end_time - start_time)
    print("End time: ",end_time2 - start_time2)

if __name__ =="__main__":
    main()

