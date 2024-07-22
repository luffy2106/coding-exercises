"""
Inheritance is the capability of one class to derive or inherit the properties from another class. 

Benefits of inheritance are: 
It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
"""

# Creating a Parent Class
# A Python program to demonstrate inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Unknown sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

def make_animal_speak(animal):
    print(animal.speak())

# Create an instance of the base class
animal = Animal("Generic animal")
make_animal_speak(animal)  # Output: Unknown sound

# Create an instance of the derived class
dog = Dog("Buddy")
make_animal_speak(dog)  # Output: Woof!


