name = input("Enter name:")
age = int(input("Enter age:"))
country = input("Enter country:")
percentage = float(input("Enter percentage:"))

myDictionary = {"Name": name, "Age": age, "Country of Birth": country, "Percentage": percentage}
print(myDictionary)

# Length of dictionary
print(len(myDictionary))

#Printing the keys of the Dictionary
print(myDictionary.keys())
#Printing the values of the Dictionary
print(myDictionary.values())
#Printing the items of the Dictionary
print(myDictionary.items())
#Changing the value of a key
myDictionary["Name"]="John"
print(myDictionary)


#Printing the Keys and Values of the Dictionary seperately
print("Keys of the given Dictionary: ", myDictionary.keys())
print("Values of the given Dictionary: ", myDictionary.values())

#Changing the value of a key using update
myDictionary.update({"Name":"John"})
print(myDictionary)
#Poping a key from the dictionary
a=myDictionary.pop("Name")
print(a)
