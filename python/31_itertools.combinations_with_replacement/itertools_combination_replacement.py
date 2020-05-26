#!/usr/bin/python

from itertools import combinations_with_replacement


def combination_replacement(word, size):
    for item in list(combinations_with_replacement(sorted(word.upper()), size)):
        print("".join(item))


if __name__ == "__main__":
    word, size = map(str, input().split())
    combination_replacement(word, int(size))
