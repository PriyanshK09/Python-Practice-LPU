officialName = input("Enter your Name :- ")
print("Hey there! " + officialName + " Please enter the further asked details correctly.")

timeSpent = int(input("Tenure you are working in the company (in years) :- "))
salary = int(input("What's your Current Salary :- "))

if timeSpent > 10 :
    netSalary = salary + (salary/100)*10
    print("Your net salary from next month will be " + str(netSalary) + " Congratulations")

elif timeSpent > 6 and timeSpent <= 10 :
    netSalary = salary + (salary/100)*8
    print("Your net salary from next month will be " + str(netSalary) + " Congratulations")
    
elif timeSpent < 6 :
    netSalary = salary + (salary/100)*5
    print("Your net salary from next month will be " + str(netSalary) + " Congratulations")
    
else :
    print("Sorry, You aren't eligible")
