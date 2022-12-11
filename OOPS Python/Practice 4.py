# Types of Variables in Class : Instance Variable, Class Variable, Static Variable

# Class Variable : Class variable is a variable whose value is assigned inside a class but outside
# any constructor or method. Class variable is shared by all objects. It is declared inside the class

# Static Variable : Static variable is a variable whose value is assigned inside a class but outside
# any constructor or method. Static variable is shared by all objects. It is declared inside the class

# Instance Variable : Instance variable is a variable whose value is assigned inside a constructor or method with self.
# Instance variable is not shared by all objects. It is declared inside the constructor or method with self.
# Instance variable can be accessed inside the class directly but we can't access it from outside the class.


# ---------------------------------------------------------------------------------------------
# Question : Create a class Name with two instance variables name and age. Create a method which will update the age of the person.

class Name:
    def __init__(self):
        self.name = "Sachin"
        self.age = 25
        
    def update(self):
        self.age = 30
        
    def printOutput(self):
        print("Updated Age of",self.name,"is : ",self.age)
        
name1 = Name()
name1.update()
name1.printOutput()
