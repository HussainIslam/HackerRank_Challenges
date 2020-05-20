#!/bin/python3

if __name__ == "__main__":
    n, m = map(int, input().split())
    pattern = '\n'.join([('.|.' * (2*i + 1)).center(m, '-')
                         for i in range(n//2)])
    print(pattern)
    print('WELCOME'.center(m, '-'))
    print(pattern[::-1])
