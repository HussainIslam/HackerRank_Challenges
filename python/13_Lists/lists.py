#!/bin/python3

if __name__ == "__main__":
    number_of_operations = int(input())
    operations = []
    main_list = []
    for _ in range(number_of_operations):
        operations.append(input())
    for _ in range(number_of_operations):
        operation = operations[_].split()
        command = operation.pop(0)
        if command != "print":
            command += "(" + ", ".join(operation) + ")"
            exec(f"main_list.{command}")
        else:
            print(main_list)
