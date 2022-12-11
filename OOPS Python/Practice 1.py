class Laptop:
    def config(self):
        print("i5, 16GB, 1TB")
        
laptop1 = Laptop()
laptop2 = Laptop()

# Printing ID of laptop1 and laptop2
print(id(laptop1))
print(id(laptop2))
# Both the ID's are different because they are two different objects.
    
# Back to the code
laptop1.config()
laptop2.config()


    
# Path: OOPS Python\Practice 2.py :- Here we are using the same class as above but we are passing the parameters to the class.
# __init__ : is a constructor which is used to initialize the instance variables of the class when an object is created. 
# self : is a reference variable which is used to refer the current instance of the class.
# self.brand = brand : is an instance variable which is used to store the value of brand.
# self.model = model : is an instance variable which is used to store the value of model.
# self.price = price : is an instance variable which is used to store the value of price.
# self.laptop_name = brand + ' ' + model : is an instance variable which is used to store the value of laptop_name.
