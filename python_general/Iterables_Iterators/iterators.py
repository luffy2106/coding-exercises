"""
Understand iteration, iterable and iterators : 
https://www.analyticsvidhya.com/blog/2021/07/everything-you-should-know-about-iterables-and-iterators-in-python-as-a-data-scientist/
- iteration is act of repeating
- iterables are objects that can be iterated in iterations(example : lists, tuples, sets, dictionaries ...)
- iterator is an object which implements the iterator protocol, which means it consists of the methods such as :
  * __iter__() :  returns an iterator
  * __next__() :  to manually iterate through all the items of an iterator

Why do we need iterators instead of foor loop ?
- Iterator and for-each loop are faster than simple for loop for collections with no random access, while in collections which allows random access there is no performance change with for-each loop/for loop/iterator.
- Iterator can set up rule and condition for how to move to the next object, see the code implement  

Implement iterators:

https://www.w3schools.com/python/python_iterators.asp#:~:text=An%20iterator%20is%20an%20object,)%20and%20__next__()%20.

"""


# If we define iterators by ourself
print("If we define iterators by ourself")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("if we use default iterators of python such as lists, tuples, sets, dictionaries, they already have function __next__()")
# if we use default iterators of python such as lists, tuples, sets, dictionaries, they already have function __next__()
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))