Number = input("Enter the Digits :")
DigitCounts = list(Number)

Str =""

for i in range ((len(DigitCounts)-1),-1,-1):
    Str = Str + DigitCounts[i]
print("Reversed digits are : ",Str)

