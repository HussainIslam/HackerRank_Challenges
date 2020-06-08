#!/usr/bin/python

from collections import Counter

if __name__ == "__main__":
    group_size = int(input())
    room_set = Counter(input().split()).items()
    [print(key) for key, value in room_set if value != group_size]
