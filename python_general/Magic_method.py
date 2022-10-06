"""
Magic or duner methods are the special methods that start and end with the double underscores.
It was used to invoke internal method or sum built in method. We can override this method for our purpose.
For example:
- when you add two numbers using the + operator, internally, the __add__() method will be called.
- when you call str(12), it calls the __str__() method in the int class

some important magic methods:
https://www.tutorialsteacher.com/python/magic-methods-in-python
"""

class Employee:
    """
    This class try to overrive __str__() method, which is called when you print an object
    """
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

e1 = Employee()
print(e1)


class distance:
    """
    This class try to override :
    - __init__ method, which was called when you create an class object
    - __add__ method, which was called when you call + operator
    - __str__ method, which was called when you call print function
    """
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self,x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)

d1=distance(3,10)
d2=distance(4,4)
print("d1= {} d2={}".format(d1, d2))
d3=d1+d2
print(d3)

class distance:
    """
    This class try to override :
    - __init__ method, which was called when you create an class object
    - __ge__ method, which was called when you call > operator
    
    """
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False

d1=distance(2,1)
d2=distance(4,10)
print(d1>=d2)


