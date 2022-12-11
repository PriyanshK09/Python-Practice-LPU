class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def printOutput(self):
        print("My name is : ", self.name," and my roll number is : ", self.rollno)
        
    def idOfStudent(self):
        print(self.name, "id is : ", id(self))
        
student1 = Student("A", 1)
student2 = Student("B", 2)
student3 = Student("C", 3)

student1.printOutput()
student2.printOutput()
student3.printOutput()

student1.idOfStudent()
student2.idOfStudent()
student3.idOfStudent()
