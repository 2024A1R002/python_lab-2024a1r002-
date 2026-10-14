#create a class and object : Student detailsc
#create a student class to store a students name and roll number create an object and display the details using an instance method
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll}")
student1 = Student("Aman", 123)        
student1.display_details()



    
