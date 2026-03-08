import threading

def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True

def PrimeNumber(Numbers):
    data = []
    for i in Numbers:
        if is_prime(i):
            data.append(i)
    print("PrimeNumbers are:",data)


def Non_PrimeNumber(Numbers):
        data = []
        for i in Numbers:
            if not is_prime(i):
                data.append(i)
        print("Non_PrimeNumbers are:",data)


def main():
    Value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    t1 = threading.Thread(target=PrimeNumber , args=(Value,))
    t2 = threading.Thread(target=Non_PrimeNumber , args=(Value,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ =="__main__":
    main()

