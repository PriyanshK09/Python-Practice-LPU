# Input : [1, 1, 2, 2, 3, 4, 4, 5]
# Output : [3, 5]
list1 = [1, 1, 2, 2, 3, 4, 4, 5]
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)
