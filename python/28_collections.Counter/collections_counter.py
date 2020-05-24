# /usr/bin/python
from collections import Counter


def main():
    number_of_shoes = int(input())
    available_shoe_sizes = Counter(map(int, input().split()))
    number_of_customers = int(input())
    total_price = 0
    for req in range(number_of_customers):
        size, price = map(int, input().split())
        if available_shoe_sizes[size] > 0:
            total_price += price
            available_shoe_sizes[size] -= 1
    print(total_price)


if __name__ == "__main__":
    main()
