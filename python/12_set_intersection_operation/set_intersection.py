#!/bin/python3

if __name__ == "__main__":
    num_english = int(input())
    english_newspaper = set(input().split())
    num_french = int(input())
    french_newspaper = set(input().split())
    print(len(english_newspaper.intersection(french_newspaper)))
