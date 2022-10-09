#Take input of age from 3 people
#Determine the oldest

Age1 = int(input("Enter the 1st Person's Age :- "))
Age2 = int(input("Enter the 2nd Person's Age :- "))
Age3 = int(input("Enter the 3rd Person's Age :- "))

#Defining the matrix to calculate the smallest and largest age digit 

if Age1 > Age2 and Age1 > Age3 :
    print("1st Person is the Oldest")

elif Age2 > Age1 and Age2 > Age3 :
    print("2nd Person is the Oldest")
    
elif Age3 > Age1 and Age3 > Age2 :
    print("3rd Person is the Oldest")
    
elif Age1 == Age2 and Age2 == Age3 :
    print("All 3 people have the same Age")
    
else :
    print("Wrong Value!")
