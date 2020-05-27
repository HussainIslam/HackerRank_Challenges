#!/usr/bin/python
if __name__ == "__main__":
    number_of_students_english = int(input())
    set_of_students_english = set(list(map(int, input().split())))
    number_of_students_french = int(input())
    set_of_students_french = set(list(map(int, input().split())))
    print(len(set_of_students_english.union(set_of_students_french)))
