# Program to check if the given number is Prime Number or Not
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break
       
elif n == 1:
    print(n,"is not a prime number")
 
else:
    print(n,"Enter a Valid Number greater than 1")
    
        