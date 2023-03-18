'''
A
BB
CCC
DDDD
'''
'''
n = int(input())
i = 1
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
p=0
while i <= n:
    j = 0
    p = p + 1
    while j <= i:
        print(l[p], end="")
        j = j + 1
    print()
    i = i + 1
'''
n = int(input())
i = 1
while i<=n:
    char = ord("A")+i-1
    j = 1
    while j<=i:
        print(chr(char),end="")
        j+=1
    print()
    i+=1