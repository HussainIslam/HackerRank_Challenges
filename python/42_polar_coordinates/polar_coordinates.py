#!/usr/bin/python

from cmath import phase

if __name__ == "__main__":
    z = complex(input())
    print(abs(z))
    print(phase(z))
