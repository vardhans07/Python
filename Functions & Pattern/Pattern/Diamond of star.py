'''
Diamond of Stars
Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
'''
n=int(input())
firstHalf = (n+1)//2
secondHalf=n//2
currentRow=1
while currentRow<=firstHalf:
    spaces=1
    while spaces<=(firstHalf-currentRow):
        print(" ",end="")
        spaces=spaces+1
    currentCol=1
    while currentCol<=(2*currentRow)-1:
        print("*",end="")
        currentCol=currentCol+1
    print()
    currentRow+=1
sp=1
st=n-2
t=n//2
while(t>0):
    i=0
    while(i<sp):
        print(end=" ")
        i += 1
    i=0
    while(i<st):
        print('*',end="")
        i += 1
    print()
    t-=1
    sp+= 1
    st -=2
