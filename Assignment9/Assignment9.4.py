def Cube(Value1):
    return Value1 * Value1 * Value1

def main():
    Ret = int(input("Enter the Number :"))
    Ans = Cube(Ret)
    print(f"Cube of {Ret} is {Ans}")

main()
