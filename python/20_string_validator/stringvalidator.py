#!/bin/python3

if __name__ == '__main__':
    s = input()
    print(any(s[i:i+1].isalnum() for i in range(0, len(s))))
    print(any(s[i:i+1].isalpha() for i in range(0, len(s))))
    print(any(s[i:i+1].isdigit() for i in range(0, len(s))))
    print(any(s[i:i+1].islower() for i in range(0, len(s))))
    print(any(s[i:i+1].isupper() for i in range(0, len(s))))
