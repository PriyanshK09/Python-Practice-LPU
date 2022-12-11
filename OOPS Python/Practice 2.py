class Laptop:
    
    def __init__(self, name, processor):
        self.name = name
        self.processor = processor
    
    def printoutput(self):
        print("My Laptop name is : ", self.name," and processor is : ", self.processor)
        
laptop1 = Laptop("Dell", "i7")
laptop2 = Laptop("HP", "i5")
laptop3 = Laptop("Lenovo", "i3")

laptop1.printoutput()
laptop2.printoutput()
laptop3.printoutput()