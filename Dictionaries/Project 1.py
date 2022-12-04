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