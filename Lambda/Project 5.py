# list2 = [34, 88, 30, 22, 10, 15,18]
# Print out all the multiples of 5 using filter function and lambda expression in the list2 

list2 = [34, 88, 30, 22, 10, 15,18]
print(list(filter(lambda x: x%5==0, list2)))

# Lambda is used to create a function without a name.