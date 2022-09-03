"""
Understand iteration, iterable and iterators : 
https://www.analyticsvidhya.com/blog/2021/07/everything-you-should-know-about-iterables-and-iterators-in-python-as-a-data-scientist/
- iteration is act of repeating
- iterables are objects that can be iterated in iterations. 
- iterator is an object which implements the iterator protocol, which means it consists of the methods such as  __iter__() and __next__().

Why do we need iterators instead of foor loop ?
- Iterator and for-each loop are faster than simple for loop for collections with no random access, while in collections which allows random access there is no performance change with for-each loop/for loop/iterator.
- Iterator can set up rule and condition for how to move to the next object, see the code implement  

Implement iterators:

https://www.w3schools.com/python/python_iterators.asp#:~:text=An%20iterator%20is%20an%20object,)%20and%20__next__()%20.

"""



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