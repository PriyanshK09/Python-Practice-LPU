# Tuples - They store multiple items in a Single Variable
# They are immutable - cannot be changed
# They are ordered - they have a defined order
# They allow duplicate members
# They are indexed - they have indexes
# They are written with round brackets
# They are faster than lists
# They are used to write-protect data
# They are used to return multiple values from a function
# They are used to assign multiple variables in one line
# They are used to swap values
# They are used to store fixed data
# They are used to store data that should not be changed

myTuple = ("Max", 28, "Boston") # Tuple with 3 items - 1 string, 1 integer, 1 string - they are immutable
print(myTuple)

myTuple2 = ("Max", 28, "Bostor", 28) # Tuple with 4 items - 1 string, 1 integer, 1 string, 1 integer - they allow duplicate members
print(myTuple2)

print(len(myTuple2)) # Length of the tuple

print(myTuple[0]) # Indexing - first item in the tuple