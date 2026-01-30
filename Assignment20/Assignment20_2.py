import threading
import time

def Even(Num):
    sum =0 
    for i in range(1 ,Num +1):
        if(Num % i ==0) and (i % 2 ==0):
                
                sum = sum + i
    print("Addition of Even Factors :" ,sum)

def Odd(Num):
    sum =0 
    for i in range(1 , Num +1):
          if (Num % i ==0) and (i % 2 !=0):
               
               sum = sum + i
    print("Addition of Odd Factors :",sum)
   

def main():
    Value = int(input("Enter the Value :"))
    # print(Data)
    t1 = threading.Thread(target=Even,args=(Value,))
    t2 = threading.Thread(target=Odd,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

main()



