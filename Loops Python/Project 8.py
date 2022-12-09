# Print unique numbers from a List of numbers using a for loop and a while loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("Unique numbers from the list using for loop: ", list2)