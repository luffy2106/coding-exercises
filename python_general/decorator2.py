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
explain :
* point to a list
- when name_format call, it go to person_lister
- the person_lister go to inner function
- in the inner function, we sort then store to the new list

"""

 #A decorator is just a callable that takes a function as an argument and returns a replacement function. 
def person_lister(f): # f is name_format function
    def inner(people):
        for i in range(len(people)):
            people[i].append(i)
        people.sort(key=lambda people : int(people[2]))
        ret = [f(person) for person in people]
        return ret
        # complete the function
    return inner



@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')