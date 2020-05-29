#!/usr/bin/python


def get_set(size):
    return set(map(int, input().split()))


if __name__ == "__main__":
    num_test_cases = int(input())
    results = list()
    for _ in range(num_test_cases):
        set_A_size = int(input())
        set_A = get_set(set_A_size)
        set_B_size = int(input())
        set_B = get_set(set_A_size)
        results.append(str(set_A.issubset(set_B)))

    print("\n".join(results))
