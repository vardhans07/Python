'''
Pyramid Number Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
'''
n=int(input())
i=1

while i<=n:
    #spaces
    spaces=1  
    while spaces<=n-i:
        print(" ",end="")
        spaces=spaces+1
    j=1
    p=i
    while j<=i:
        print(p,end="")
        j=j+1
        p=p-1
    j=1
    p=2
    while j<=i-1:
        print(p,end="")
        p=p+1
        j=j+1
    print()
    i=i+1