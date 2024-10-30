# This repo including coding-exercises on python in Leetcode, hackerranks and questions in python.

Good reference
- Tips in python
```
https://github.com/chiphuyen/python-is-cool/blob/master/README.md
```
- Good practice
```
https://aman.ai/primers/python/
```

#### 1. What is the four basic concepts of OOP:
- encapsulation : This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
- abstraction : abstract class contain abstract method(which has declaration but no implementation), Their implementation will be declared by sub class. 
- inheritance : Inheritance is the capability of one class to derive or inherit the properties from another class. 
- polymorphism : The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.

#### 2. What is python decorators ?
It's often useful to know how long it takes a function to run, e.g. when you need to compare the performance of two algorithms that do the same thing. One naive way is to call `time.time()` at the begin and end of each function and print out the difference.

For example: compare two algorithms to calculate the n-th Fibonacci number, one uses memoization and one doesn't.

```python
def fib_helper(n):
    if n < 2:
        return n
    return fib_helper(n - 1) + fib_helper(n - 2)

def fib(n):
    """ fib is a wrapper function so that later we can change its behavior
    at the top level without affecting the behavior at every recursion step.
    """
    return fib_helper(n)

def fib_m_helper(n, computed):
    if n in computed:
        return computed[n]
    computed[n] = fib_m_helper(n - 1, computed) + fib_m_helper(n - 2, computed)
    return computed[n]

def fib_m(n):
    return fib_m_helper(n, {0: 0, 1: 1})
```

Let's make sure that `fib` and `fib_m` are functionally equivalent.

```python
for n in range(20):
    assert fib(n) == fib_m(n)
```

```python
import time

start = time.time()
fib(30)
print(f'Without memoization, it takes {time.time() - start:7f} seconds.')

==> Without memoization, it takes 0.267569 seconds.

start = time.time()
fib_m(30)
print(f'With memoization, it takes {time.time() - start:.7f} seconds.')

==> With memoization, it takes 0.0000713 seconds.
```

If you want to time multiple functions, it can be a drag having to write the same code over and over again. It'd be nice to have a way to specify how to change any function in the same way. In this case would be to call time.time() at the beginning and the end of each function, and print out the time difference.

This is exactly what decorators do. They allow programmers to change the behavior of a function or class. Here's an example to create a decorator `timeit`.

```python
def timeit(fn): 
    # *args and **kwargs are to support positional and named arguments of fn
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time 
```

Add the decorator `@timeit` to your functions.

```python
@timeit
def fib(n):
    return fib_helper(n)

@timeit
def fib_m(n):
    return fib_m_helper(n, {0: 0, 1: 1})

fib(30)
fib_m(30)

==> Time taken in fib: 0.2787242
==> Time taken in fib_m: 0.0000138
```

#### 3. Caching with @functools.lru_cache
Memoization is a form of cache: we cache the previously calculated Fibonacci numbers so that we don't have to calculate them again.

Caching is such an important technique that Python provides a built-in decorator to give your function the caching capacity. If you want `fib_helper` to reuse the previously calculated Fibonacci numbers, you can just add the decorator `lru_cache` from `functools`. `lru` stands for "least recently used". For more information on cache, see [here](https://docs.python.org/3/library/functools.html).

```python
import functools

@functools.lru_cache()
def fib_helper(n):
    if n < 2:
        return n
    return fib_helper(n - 1) + fib_helper(n - 2)

@timeit
def fib(n):
    """ fib is a wrapper function so that later we can change its behavior
    at the top level without affecting the behavior at every recursion step.
    """
    return fib_helper(n)

fib(50)
fib_m(50)

==> Time taken in fib: 0.0000412
==> Time taken in fib_m: 0.0000281
```
#### 4. Some built-in function?
In Python, magic methods are prefixed and suffixed with the double underscore `__`, also known as dunder. The most wellknown magic method is probably `__init__`.

```python
class Node:
    """ A struct to denote the node of a binary tree.
    It contains a value and pointers to left and right children.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

When we try to print out a Node object, however, it's not very interpretable.

```python
root = Node(5)
print(root) # <__main__.Node object at 0x1069c4518>
```

Ideally, when user prints out a node, we want to print out the node's value and the values of its children if it has children. To do so, we use the magic method `__repr__`, which must return a printable object, like string.

```python
class Node:
    """ A struct to denote the node of a binary tree.
    It contains a value and pointers to left and right children.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        strings = [f'value: {self.value}']
        strings.append(f'left: {self.left.value}' if self.left else 'left: None')
        strings.append(f'right: {self.right.value}' if self.right else 'right: None')
        return ', '.join(strings)

left = Node(4)
root = Node(5, left)
print(root) # value: 5, left: 4, right: None
```

We'd also like to compare two nodes by comparing their values. To do so, we overload the operator `==` with `__eq__`, `<` with `__lt__`, and `>=` with `__ge__`.

```python
class Node:
    """ A struct to denote the node of a binary tree.
    It contains a value and pointers to left and right children.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value


left = Node(4)
root = Node(5, left)
print(left == root) # False
print(left < root) # True
print(left >= root) # False
```

For a comprehensive list of supported magic methods [here](https://www.tutorialsteacher.com/python/magic-methods-in-python) or see the official Python documentation [here](https://docs.python.org/3/reference/datamodel.html#special-method-names) (slightly harder to read).

Some of the methods that I highly recommend:

- `__len__`: to overload the `len()` function.
- `__str__`: to overload the `str()` function.
- `__iter__`: if you want to your objects to be iterators. This also allows you to call `next()` on your object.

For classes like Node where we know for sure all the attributes they can support (in the case of Node, they are `value`, `left`, and `right`), we might want to use `__slots__` to denote those values for both performance boost and memory saving. For a comprehensive understanding of pros and cons of `__slots__`, see this [absolutely amazing answer by Aaron Hall on StackOverflow](https://stackoverflow.com/a/28059785/5029595).

```python
class Node:
    """ A struct to denote the node of a binary tree.
    It contains a value and pointers to left and right children.
    """
    __slots__ = ('value', 'left', 'right')
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

#### 5. What is generator, when do you use it. What is the difference between iterator and generator ?

A generator is a special type of iterator in Python. It is implemented using a function that uses the yield keyword instead of return. When a generator function is called, it returns an object (generator) that can be iterated over to retrieve values one at a time.

Generators are used when we want to generate a sequence of values dynamically, on-the-fly, without storing them all in memory at once. They are memory-efficient and provide a way to work with large or infinite sequences of data.

The primary difference between an iterator and a generator is that an iterator is an object that implements the iterator protocol, whereas a generator is a specific type of iterator that is created using a generator function.

Here are some key differences:

Iterator:
- An iterator is an object that implements the __iter__() and __next__() methods.
- Iterators are used to iterate over a collection or sequence of items, providing access to each item one at a time.
- The __iter__() method returns the iterator object itself.
- Iterators can be created for any custom class by implementing the iterator protocol.
Generator:
- A generator is a special type of iterator that is created using a generator function.
- Generator functions use the yield keyword to yield values one at a time, suspending the execution of the function until the next value is requested.
- Each time a value is yielded, the state of the generator function is saved, allowing it to resume from where it left off.
- Generators automatically implement the iterator protocol, so they can be used in loops and other constructs that expect an iterable.

Iterator differs from generators, which do not store the entire sequence in memory. Instead, generators yield values dynamically as they are requested. Each time the yield keyword is encountered, the generator suspends its execution and waits for the next iteration. This allows generators to be more memory-efficient, especially when dealing with large or infinite sequences.

Ask chatGPT for example.


#### 6. The order of code block in python 
The order of code alway from top to bottom in python file, even in the main function. In the example below, the code order will be : blockA->blockB->blockC


# code block A - start
print("Hello, 1")
# code block A - end
def main():
    # code block B - start
    print("Hello, 2")
    # code block B - start

if __name__ == "__main__":
    main()

# code block C - start
print("Hello, 3")
# code block C - start


#### 7. Is private attributes exist in python ?

In Python, there is no strict concept of private attributes like in some other programming languages such as Java or C++. However, there is a convention that developers use to indicate that an attribute or method should be treated as private.

By convention, if you want to indicate that an attribute or method is intended for internal use and should not be accessed directly from outside the class, you can prefix its name with an underscore (_). This serves as a signal to other developers that the attribute or method is intended to be private.
```
class MyClass:
    def __init__(self):
        self._private_attribute = 10

    def _private_method(self):
        print("This is a private method")

my_object = MyClass()
print(my_object._private_attribute)  # Accessing a "private" attribute (not recommended)
my_object._private_method()  # Calling a "private" method (not recommended)
```

#### 8. gabarge collector in python exist ?

Yes, Python does have a garbage collector. The garbage collector in Python is responsible for automatically reclaiming memory that is no longer in use, freeing it up for other purposes. The garbage collector in Python operates transparently in the background, and in most cases, you don't need to explicitly manage memory deallocation as it dones automatically by Python.


#### 9. What is the difference between List and Tuple ?

1. Mutability:
- List: Mutable (you can change, add, or remove elements after creating a list).
- Tuple: Immutable (once a tuple is created, you cannot change, add, or remove elements).

2. Performance:
- List: Slightly slower for certain operations due to mutability.
- Tuple: Faster, especially for access and iteration, due to its fixed size and immutability.

3. Use cases
- List: When you need a collection that can change over time (like appending, removing, or updating items).
- Tuple: When you need a fixed collection of items, often for fixed data structures or as dictionary keys (since they are hashable, unlike lists).

4. Key in dictionary
- List : you cannot use a list as a key in a dictionary in Python. This is because lists are mutable
- Tuple : you can use a tuple as a dictionary key since tuples are immutable and hashable, as long as the tuple itself only contains immutable elements
Ex :
my_dict = { (1, 2): "value" }
my_dict = { [1, 2]: "value" }  # Raises a TypeError


Note : Both lists and tuples allow duplicate values in Python. You can have multiple occurrences of the same element in both
