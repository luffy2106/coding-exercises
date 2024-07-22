"""
This exercices is for understanding abstract class in python

Question :
https://www.hackerrank.com/challenges/abstract-classes/problem


Note:
One real world example of this concept is a snack machine, where you give the machine money, make a selection, and the machine dispenses the snack. The only thing that matters is what the machine does (i.e.: dispenses the selected snack); 
you can easily buy a snack from any number of snack machines without knowing how the machine's internals are designed (i.e.: the implementation details).

1. The main difference between abstraction and inheritance is that abstraction allows hiding the internal details and displaying only the functionality to the users, 
while inheritance allows using properties and methods of an already existing class. See in detailed below:

https://www.w3schools.com/python/python_inheritance.asp

https://www.hackerrank.com/challenges/30-abstract-classes/tutorial

2. 
- A class which contains one or more abstract methods is called an abstract class.
- An abstract method is a method that has a declaration but does not have an implementation. Their implementation will be declared by sub class. 
"""

# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC
from abc import ABC, abstractmethod
#Write MyBook class
class Book(ABC): 
    def __init__(self, title, author, price):
        self.title =  title
        self.author = author
        self.price = price

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
        # super()
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))



title="math"
author="Kien"
price=10
new_novel=MyBook(title,author,price)
new_novel.display()







