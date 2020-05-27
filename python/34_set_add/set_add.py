#!/usr/bin/python


if __name__ == "__main__":
    number_of_countris = int(input())
    set_of_countries = set()
    for _ in range(number_of_countris):
        set_of_countries.add(input())
    print(len(set_of_countries))
