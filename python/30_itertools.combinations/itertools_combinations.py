#!usr/bin/python
from itertools import combinations


def main():
    word, size = map(str, input().split())
    for i in range(1, int(size)+1):
        for item in list(combinations(sorted(word.upper()), i)):
            print("".join(item))


if __name__ == "__main__":
    main()
