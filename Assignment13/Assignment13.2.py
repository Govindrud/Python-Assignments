def Maths(Radius):
    Area=(3.14 *Radius * Radius)
    return Area

        
def main():
    Radius = int(input("Enter the Radius :"))
    
    Ret=Maths(Radius)
    print("Area of the Circle is   : ",Ret)

if __name__ =="__main__":
    main()