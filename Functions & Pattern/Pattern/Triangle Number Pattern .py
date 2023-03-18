#Triangle Number Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
22
333
4444
"""
n = int(input())
i = 1
p = 0
while i <= n:
    j = 1
    p = p + 1
    while j <= i:
        print(p, end="")
        j = j + 1
    print()
    i = i + 1
