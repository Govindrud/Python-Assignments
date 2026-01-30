def ChkPrime(Numbers):
    data = list()

    for no in Numbers:
        print(no)
        if no < 2 :
            continue
        for i in range(2,no):
            if no % i == 0 :
                break
        else:
            data.append(no)

    return data







