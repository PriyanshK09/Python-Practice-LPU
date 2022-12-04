# list1 = [10, 20, 30, 40, 50]
# triple all the elements in the list

list1 = [10, 20, 30, 40, 50]

# Using for loop
for i in range(len(list1)):
    list1[i] = list1[i] * 3
print(list1)

# Using map
list2 = list(map(lambda x: x * 3, list1))
print(list2)