import math
#take input from the user
num = int(input("Enter a number to find Square Root : "))
#check if the input number is negative
if num<0:
    print("Negative numbers can't have Square Roots!")
else:
    print("Square Root of the Given Number is = ",math.sqrt(num))