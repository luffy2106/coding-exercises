"""
Reference :
- https://www.geeksforgeeks.org/generators-in-python/
- https://www.geeksforgeeks.org/python-yield-keyword/
- https://www.geeksforgeeks.org/python-list-comprehensions-vs-generator-expressions
- https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/


"""


"""
Generator:
- Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 
- Generator-Object : Generator functions return a generator object that is iterable, i.e., can be used as an Iterators. Generator objects are used either by calling the next method on the generator object 
or using the generator object in a “for in” loop (as shown in the above program). 
"""

# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))


"""
yield in Python
Difference between return and yield Python
The yield keyword in Python is similar to a return statement used for returning values in Python. It's returns a generator object to the one who calls the function which contains yield, 
instead of simply returning a value. The main difference between them is, the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function. 

Advantages of yield:
- Using yield keyword is highly memory efficient, since the execution happens only when the caller iterates over the object.
- As the variables states are saved, we can pause and resume from the same point, thus saving time.
Disadvantages of yield: 
- Sometimes it becomes hard to understand the flow of code due to multiple times of value return from the function generator.
- Calling of generator functions must be handled properly, else might cause errors in program.
"""

def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"
 
 
obj = fun_generator()
 
print(type(obj))
 
print(next(obj))
print(next(obj))


"""
Compare list comprehension and Generator expression on space and time complexity:

The generator yields one item at a time and generates item only when in demand. Whereas, in a list comprehension, Python reserves memory for the whole list. 
Thus we can say that the generator expressions are memory efficient than the lists.
"""

"""In term of space"""
# import getsizeof from sys module
from sys import getsizeof
  
comp = [i for i in range(10000)]
gen = (i for i in range(10000))
  
#gives size for list comprehension
print("size of list comprehension")
x = getsizeof(comp) 
print("x = ", x)
  
#gives size for generator expression
print("size of generator expression")
y = getsizeof(gen) 
print("y = ", y)

"""In term of time efficient"""

#List Comprehension: 
import timeit
  
print("Time to create list")
print(timeit.timeit('''list_com = [i for i in range(100) if i % 2 == 0]''', number=1000000))
print("Time to create generator objects")
print(timeit.timeit('''gen_exp = (i for i in range(100) if i % 2 == 0)''', number=1000000))

