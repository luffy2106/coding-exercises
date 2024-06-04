
"""
This is just a simple exercise to test code review skill. no complicated.

Question :

Write a function to reverse the number. Ex: 12345 -> 54321
"""

def reverse_number(number):
    str_num = str(number)
    str_reverse_number = str_num[::-1]
    return int(str_reverse_number)