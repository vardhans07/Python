'''
Yet another Pattern
Send Feedback
Ninja was playing with her sister to solve a puzzle pattern. However, even after taking several hours, they could not solve the problem.
A value of N is given to them, and they are asked to solve the problem. Since they are stuck for a while, they ask you to solve the problem. Can you help solve this problem?
Example : Pattern for N = 4

****
 ***
  **
   *
'''

def ninjaPuzzle(n):
    for i in range(n, 0, -1):
        print(" "*(n-i)+"*"*i)
n=int(input())
ninjaPuzzle(n)