"""
#different method for Triangular Star pattern
#Method -1 (Source from other User)

n=int(input())
for i in range(0, n):
    for j in range(0, i+1):
        print("*",end="")
    print()

"""
# Method - 2 (Rajvardhan Method)
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
"""
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1

