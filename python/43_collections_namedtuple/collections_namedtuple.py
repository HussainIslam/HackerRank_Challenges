#!/usr/bin/python
from collections import namedtuple

if __name__ == "__main__":
    number = int(input())
    headings = input()
    Student = namedtuple("Student", headings)
    marks = [int(Student._make(input().split()).MARKS) for _ in range(number)]
    print(sum(marks) / len(marks))
