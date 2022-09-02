
"""
The main goal of this exercise is to understand decorators in python

Question :
https://www.hackerrank.com/domains/python/closures-and-decorators/difficulty/all/page/1

Tutorial :

https://www.datacamp.com/tutorial/decorators-python


Note :
To see the difference between *args and **kwargs:
https://www.programiz.com/python-programming/args-and-kwargs

To understand closure and decorator and understand why decorator is useful (read section 8 and 9)

http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


"""

"""
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. 
Make a decorator that standardizes the mobile numbers and apply it to the function.
"""


#A decorator is just a callable that takes a function as an argument and returns a replacement function. 
def wrapper(f): # f is sort_phone function
    def fun(l):
        # complete the function
        # l = "".join(l)
        new_l = []
        for e in l:
            if len(e) > 10:
                if e.startswith('+91'):
                    e = e[3:]
                elif e.startswith('91'):
                    e = e[2:]
                elif e.startswith('0'):
                    e = e[1:]
            e1 = e[:5]
            e2 = e[5:]
            e = "+91 "+e1 + " " + e2
            new_l.append(e) 
        ret = f(new_l) 
        return ret
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
