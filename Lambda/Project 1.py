from functools import reduce


def isEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
list1 = [1,2,3,4,5,6,7,8,9,10]
output = list(map(isEven, list1))
output1 = list(filter(isEven, list1))
output2 = list(map(lambda x: x**(1/2), list1))
output3 = reduce(lambda x,y: x+y, list1)
print(output)
print(output1)
print(output2)
print(output3)

# List map is used to apply a function to each element of a list
# List filter is used to filter out elements of a list based on a function
# The function isEven is applied to each element of the list
# The function isEven is also used to filter out the elements of the list
# The output of the map function is a list of None values
# The output of the filter function is a list of the elements that are even
# The function isEven is not returning anything, it is just printing the result
# The map function is not returning anything, it is just printing the result
# The filter function is not returning anything, it is just printing the result
