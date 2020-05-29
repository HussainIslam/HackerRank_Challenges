#!/usr/bin/python


def set_input():
    return set(map(int, input().split()))


if __name__ == "__main__":
    number_of_items_main = int(input())
    main_set = set_input()
    number_of_operations = int(input())
    for _ in range(number_of_operations):
        command, size = input().split()
        temp_set = set_input()
        command_string = "main_set." + command + "(temp_set)"
        exec(command_string)
    print(sum(main_set))
