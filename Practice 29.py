#Take a user Input, If length of that input is greater than 3 characters then prind "ing" prefix otherwise print as it is.

name = input("Enter name of Person : ")
x = len(name)

if x>3:
    print("ing" + name)
    
if x<3:
    print(name)
    print("Name too Short!")
    
if x==3:
    print(name)
    print("Name doesn't fulfil Requirement!")
