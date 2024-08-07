"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc. 
The finance section handles all the financial transactions and keeps records of all the data related to finance. 
Similarly, the sales section handles all the sales-related activities and keeps records of all the sales. 
Now there may arise a situation when for some reason an official from the finance section needs all the data about sales in a particular month. 
In this case, he is not allowed to directly access the data of the sales section. He will first have to contact some other officer in the sales section and 
then request him to give the particular data. 
This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”. 
Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""


"""
There are 3 types of members
- public 
- protected
- private
"""

"""
public member:
public members of a class are available to everyone. So they can be accessed from outside the class and also by other classes too. 
All members of a class are by default public in Python. These members can be accessed outside of the class, and their values can be modified too.
"""

"""
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
"""

# Creating a base class
class Base:
    def __init__(self):
 
        # Protected member
        self._a = 2
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)
 
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)
 
 
obj1 = Derived()
 
obj2 = Base()
 
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)
 
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)



"""
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any inherited class. 
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”.
"""

# Python program to
# demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

try:
    print(obj1.__c)
except:
    print("Can not access member __c from base class because this variable is private")

try:
    obj2 = Derived()
except:
    print("Can not access member __c from child class(inherit from base) because this variable is private")

