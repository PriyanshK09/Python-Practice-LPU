# {} - Print Empty Dictionary
# keys : a,b,c,d - Enter the keys
# values : 1,2,3,4 - Enter the values
# {a: 1, b: 2, c: 3, d: 4} - Print the dictionary
# e,5 - Enter the key and value
# f,6
# g,7
# {a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7} - Print the dictionary

dict1 = {}
print(dict1)
# Entering the keys
keys = input("keys : ").split(",")
# Entering the values
values = input("values : ").split(",")

# Creating the dictionary
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)

# Adding the pair of key and value
keyandvalue = input().split(",") 
dict1[keyandvalue[0]] = keyandvalue[1]
keyandvalue = input().split(",")
dict1[keyandvalue[0]] = keyandvalue[1]
keyandvalue = input().split(",")
dict1[keyandvalue[0]] = keyandvalue[1]

print(dict1)
