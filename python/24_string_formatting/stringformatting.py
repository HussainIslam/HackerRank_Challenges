def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        converts = str(i), oct(i)[2:], hex(
            i)[2:].upper(), bin(i)[2:]
        [print(" ".join(str(x).rjust(width, " ") for x in converts))]


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
