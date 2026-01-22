def Maths(Length,Breadth):
    Area=(Length * Breadth)
    return Area

        
def main():
    Length = int(input("Enter the Length :"))
    Breadth = int(input("Enter the Breadth :"))
    Ret=Maths(Length,Breadth)
    print("Area of the Rectangle is   : ",Ret)

if __name__ =="__main__":
    main()