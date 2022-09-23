"""
Inheritance is the capability of one class to derive or inherit the properties from another class. 

Benefits of inheritance are: 
It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
"""

# Creating a Parent Class
# A Python program to demonstrate inheritance
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()


# Creating a Child Class
# Here Emp is another class which is going to inherit the properties of the Person class(base class).
class Emp(Person):
    def Print(self):
        print("child class called")
        

Emp_details = Emp("Mayank", 103)
# calling parent class function
Emp_details.Display()
# Calling child class function
Emp_details.Print()

