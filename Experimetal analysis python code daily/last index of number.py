def lastindex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    smalleroutput = arr[1:]
    print(smalleroutput)
    smallerlistoutput = lastindex(smalleroutput, x)
    if smallerlistoutput != -1:
        print(smallerlistoutput , end='_A_')              #test - 1
        print(smallerlistoutput + 1, end='ha')             #test - 2
        return smallerlistoutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input('Input Range:'))
arr = list(int(i) for i in input('Array List:').strip().split(' '))
x = int(input('To Find last index Number:'))
print(lastindex(arr, x))

'''
Input Range:5
Array List:2 3 5 2 3
To Find last index Number:3
[3, 5, 2, 3]
[5, 2, 3]
[2, 3]
[3]
[]

Answer  = 0_A_1ha1_A_2ha2_A_3ha3_A_4ha ----> 4

'''