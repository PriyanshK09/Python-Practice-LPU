#String Practice
#Take a user input of Name, Print the first and last letter of the name.

nameOfPerson = str(input("Enter your Name :- "))

count = len(nameOfPerson)

print(nameOfPerson[0])
print(nameOfPerson[-1:])

#Take a user input of Name, Print the middle letter of the 
#for odd numbers
x = count//2
print(nameOfPerson[x])

