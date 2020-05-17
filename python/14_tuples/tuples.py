#!/bin/python3

if __name__ == "__main__":
    number_of_elements = int(input())
    my_tuple = tuple(map(int, input().split()))
    print(hash(my_tuple))
