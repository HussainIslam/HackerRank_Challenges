def print_rangoli(size):
    alphabets = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alphabets[size-1:i:-1] +
                       alphabets[i:size]).center((4 * size - 3), '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
