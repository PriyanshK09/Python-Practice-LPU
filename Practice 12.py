#A company decided to give bonus of 1000rs
#to employee if his/her service is more than 5 years
#Ask user their salary and year of service and print
#the net bonus amount

print("Input your Salary and Year of Service below in order to find your Bonus Amount : ")
Salary = int(input("Enter your Salary : "))
YearOfService = int(input("Enter the number of years of your Service : "))

if YearOfService > 5 :
    NetSalary = Salary + 1000
    print("Congratulations! You fulfill the Bonus Criteria.")
    print("Your Net amount of Salary will be : " , NetSalary)
    
else :
    print("Bonus Criteria not fulfilled!")
    print("Your Net amount of Salary will be : " , Salary)
    
    