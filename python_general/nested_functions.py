"""
Tutorial :
https://www.geeksforgeeks.org/python-inner-functions/


In Python, functions are treated as first class objects(which mean it's an entity which  can be constructed at run-time, 
passed as a parameter, returned from a function, or assigned into a variable), to be more specific
- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …
"""

"""
1. Inner function:

A function which is defined inside another function is known as inner function or nested function. Nested functions are able to access variables of the enclosing scope. 
Inner functions are used so that they can be protected from everything happening outside the function. This process is also known as Encapsulation

In the below example, innerFunction() has been defined inside outerFunction(), making it an inner function. 
To call innerFunction(), we must first call outerFunction(). The outerFunction() will then go ahead and call innerFunction() as it has been defined inside it
"""
# Python program to illustrate 
# nested functions 
def outerFunction(text): 
    text = text 
    
    def innerFunction(): 
        print(text) 
    
    innerFunction() 
    
if __name__ == '__main__': 
    outerFunction('Hey !') 

#output : Hey!


"""
Scope of variable in nested function
Remember:
- If the variable is non-iterable or string, you can access the variable of outer function from inner function but can not modify it
- If the variable is iterable except string(varialbe where you can loop on it : lists, tuples, sets, dictionaries ...), you can access the variable of outer function from inner function and you can modify it
"""
# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
	s = 'I love GeeksforGeeks'
	
	def f2():
		print(s)
		
	f2()

# Driver's code
print("check if we can access the variable from inner function")
f1()


# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
	s = 'I love GeeksforGeeks'
	
	def f2():
		s = 'Me too'
		print(s)
		
	f2()
	print(s)

# Driver's code
print("check if we can modify the variable from inner function")
f1()

"""
We can see that we can access the variable but you can not change it from inner function
"""

"""
How to change variable from inner function
- Use an iterable variable
- use nonelocal keyword(if you declare a variable in inner function as non local, it become variable of outer function)
"""

# Use an iterable variable
def f1():
	s = ['I love GeeksforGeeks']
	
	def f2():
		s[0] = 'Me too'
		print(s)
		
	f2()
	print(s)

# Driver's code
f1()

# Using nonlocal keyword
def f1():
	s = 'I love GeeksforGeeks'
	
	def f2():
		nonlocal s
		s = 'Me too'
		print(s)
	f2()
	print(s)

# Driver's code
f1()




