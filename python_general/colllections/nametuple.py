"""
namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
"""



from collections import namedtuple

N = int(input())
student = namedtuple("student", [x for x in input().split()])
# print(student.Class) 
score_student = 0
for i in range(N):
    info_i = [x for x in input().split()]
    student_i  = student(info_i[0], info_i[1], info_i[2], info_i[3])
    score_student = score_student + float(student_i.MARKS)
avg = score_student/N
print(round(avg,2))
    