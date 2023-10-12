# This repo including coding-exercises on python in Leetcode, hackerranks and questions in python.

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

reference:
```
https://github.com/chiphuyen/python-is-cool/blob/master/README.md
```


