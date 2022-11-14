#### In python list, we can not sort a list which contain element of different types
Because when we do sort function, we do compare element in a list, and we can not compare 2 elements with different types 

Ex: [2,5J,6].sort() => generate errors

#### Print question
t = '%(a)s %(b)s %(c)s'
print(t % dict(a='Welcome', b='to', c='Turing'))

=> output is "Welcome to Turing"

#### Global and local variable
Few keynote to remember:
- Variables that are created outside of a function (as in all of the examples above) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.
- If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was(NO MATTER YOU CHANGE THE LOCAL VARIABLE WITH THE SAME NAME INSIDE THE FUNCTION), global and with the original value.
- To create a global variable inside a function, you can use the global keyword. Also, use the global keyword if you want to change a global variable inside a function.

To see the demo : https://www.w3schools.com/python/python_variables_global.asp

Example 1:
i = "Welcome"
def welcome(i):
    i = i + ', Welcome to Turing'
    return i

welcome("Developer")
print(i)

=> the output is "Welcome"

Example 2:
def add(c,k):
    c.test = c.test + 1
    k  = k + 1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0
    for i in range(0,25):
        add(p,index)
    print("p.test =", p.test)
    print("index =", index)
    
main()

=> the output is:
p.test = 25
index = 0

#### Mode for python I/O

Mode	Description
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)


#### Set in python

set is mutable data type(we can remove or add elements to it)

set() only take one argument, for example:
- argument as a tuple : thisset = set(("apple", "banana", "cherry")) => {'cherry', 'banana', 'apple'}
- argument as a list : thisset = set(["apple", "banana", "cherry"]) => {'cherry', 'banana', 'apple'}
- argument as a string : thisset = set("abc") => {'b', 'c', 'a'}

update set:
- set("abc").update(set(["p","q"])) => {'b', 'c', 'a','p','q'}


#### copy a list

The difference between deep copy and shallow copy : https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

Important Points: The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists in list or class instances in list). Therefore, when you work with matrix list of list, it's recommend to use deep copy.

data = [1,2,3]
ways of copy :
- newList = data.copy()
- newList = list(data)
- by copy library:
import copy
newList = copy.copy(data) #swallow copy
newList = copy.deepcopy(data) #swallow copy

#### find all in regex
The findall(pattern, string, ) function scans the string from left to right and finds all the matches of the pattern in the string.

import re 
result = re.findall("welcome to turing", "welcome", 1)
print(result)

#### Python tell() function

Get the current position of file object : https://www.geeksforgeeks.org/python-tell-function

#### capitalize()

The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
Refrence : https://www.w3schools.com/python/ref_string_capitalize.asp


#### Example of mutable and immutable data in python

In mutable data types, we can modify the already existing values of the data types (such as lists, dictionaries, etc.). Or, we may add new values or remove the existing values from our data types. Basically, we may perform any operation with our data without having to create a new copy of our data type. Hence, the value assigned to any variable can be changed. In immutable data, on the contrary, we can not do that.

Example of mutable data:
- List
- Dictionary
- Set

Example of immutable data:
- Numbers
- Strings
- Tuples

Compare :
- Immutable objects are faster to access when compared to mutable objects
- Immutable objects are best suitable when we are sure that we don't need to change them at any point in time.
- Changing immutable objects is an expensive operation since it involves creating a new copy for any changes made.

Why tuple is faster than list ?
- Tuple is stored in a single block of memory while list is stored in two blocks of memory (One is fixed sized and the other is variable sized for storing data).
- List is stored in two blocks of memory (One is fixed sized and the other is variable sized for storing data)

Reference:
https://www.educative.io/answers/tuples-vs-list-in-python

# What is the difference between generator and iterator ?(need to check in detailed)

An iterator in Python serves as a holder for objects so that they can be iterated over; a generator facilitates the creation of a custom iterator.

- Genrator is alway an Iterator but Iterator is not always as a Generator.
- Generator implemented using a function. Iterator implemented using a class.
- Generator using the yield keyword. Iterator does not us the yield keyword.

Reference: 
https://www.educative.io/answers/generator-vs-iterator-in-python

# What is list comprehension ?

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.Without list comprehension you will have to write a for statement with a conditional test inside. To be more specific, to create another list from an existing list, instead of having a loop with a condition in many lines, you can simply do it like this :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

Reference:
https://www.w3schools.com/python/python_lists_comprehension.asps

# What is the difference between data frame and time series ?(Need to revise in detailed)

Series is a type of list in pandas which can take integer values, string values, double values and more. But in Pandas Series we return an object in the form of list, having index starting from 0 to n, Where n is the length of values in series. Later in this article, we will discuss dataframes in pandas, but we first need to understand the main difference between Series and Dataframe. Series can only contain single list with index, whereas dataframe can be made of more than one series or we can say that a dataframe is a collection of series that can be used to analyse the data. 

Reference:
https://www.geeksforgeeks.org/creating-a-dataframe-from-pandas-series










