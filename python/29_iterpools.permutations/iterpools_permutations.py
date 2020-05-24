#!/usr/bin/python
from itertools import permutations


def main():
    word, size = map(str, input().split())
    for item in sorted(list(permutations(word.upper(), int(size)))):
        print("".join(item))


if __name__ == "__main__":
    main()
