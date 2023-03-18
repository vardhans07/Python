'''
5
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
'''
n = int(input())

for i in range(1, n + 1, 1):
    for up in range(1, i, 1):
        print(n - up + 1, end='')

    for j in range(i, 2 * n - i + 1, 1):
        print(n - i + 1, end='')

    for lp in range(2 * n - i, 2 * n - 1, 1):
        print(lp - n + 2, end='')

    print()

for i in range(n - 1, 0, -1):
    for up in range(1, i, 1):
        print(n - up + 1, end='')

    for j in range(i, 2 * n - i + 1, 1):
        print(n - i + 1, end='')

    for lp in range(2 * n - i, 2 * n - 1, 1):
        print(lp - n + 2, end='')

    print()

