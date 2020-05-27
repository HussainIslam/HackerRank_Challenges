#!/usr/bin/python


def symmetric_difference(set1, set2):
    [print(x)
     for x in sorted(set1.difference(set2).union(set2.difference(set1)))]


if __name__ == "__main__":
    number_of_items_list1 = int(input())
    list1 = list(map(int, input().split()))
    number_of_items_list2 = int(input())
    list2 = list(map(int, input().split()))
    symmetric_difference(set(list1), set(list2))
