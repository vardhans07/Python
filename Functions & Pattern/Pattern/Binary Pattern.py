'''
Binary Pattern:
Print the following pattern for the given number of rows.

Pattern for N = 4

1111

000

11

0
'''
n = int(input())

for i in range(1, n + 1, 1):

    for j in range(1, n - i + 2, 1):
        if (i % 2 != 0):
            print('1', end='')

        else:
            print('0', end='')

    print()
