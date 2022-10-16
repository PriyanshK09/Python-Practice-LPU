#User input for 3 sides of triangle and check if Triangle can be formed or not
triangleSide1 = int(input("Enter measure of 1st Side : "))
triangleSide2 = int(input("Enter measure of 2nd Side : "))
triangleSide3 = int(input("Enter measure of 3rd Side : "))

if triangleSide1 + triangleSide2 > triangleSide3:
    print("Triangle can be Formed")
else:
    print("Triangle can't be Formed")