#!/bin/python3


def split_and_join(line):
    return "-".join(line.split(sep=" "))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
