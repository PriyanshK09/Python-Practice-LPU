number1 = int(input("Enter 1st Number :- "))
number2 = int(input("Enter 2nd Number :- "))

print("Write 'A' for Addition, 'S' for Subtraction, 'M' for Multiplication, 'D' for Divide")
operation = str(input("Enter the Operation to be done :- "))

print(operation)

if operation == "A":
    summ = number1 + number2
    print(summ)
    
elif operation == "S":
    sub = number1 - number2
    print(sub)
    
elif operation == "M":
    multi = number1 * number2
    print(multi)
    
elif operation == "D":
    div = number1/number2
    print(div)
    
else : 
    print("Wrong Choice!")