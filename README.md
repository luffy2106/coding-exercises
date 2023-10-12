# This repo including coding-exercises on python in Leetcode, hackerranks and questions in python.

Good reference
```
https://github.com/chiphuyen/python-is-cool/blob/master/README.md
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
