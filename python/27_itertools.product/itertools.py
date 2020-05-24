#!/usr/bin/python
from itertools import product


def main():
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    print(' '.join([str(item) for item in tuple(product(list_a, list_b))]))


if __name__ == "__main__":
    main()
