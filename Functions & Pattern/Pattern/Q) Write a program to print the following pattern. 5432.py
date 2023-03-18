'''
Q) Write a program to print the following pattern.
5432*

543*1

54*21

5*321
'''
lines=int(input())
i=1
while(i<=lines):# this loop is used to print lines
    j=lines
    while (j>=1):# this loop is used to print numbers in a line
        if j!=i:
            print(j, end='', flush=True)
        else:
            print('*', end='', flush=True)
        j=j-1
    print("")
    i=i+1;
    '''
    Algorithm
STEP 1: START
STEP 2: SET lines=5
SET i=1
Step 3: REPEAT STEP 4 TO 8 UNTIL i is less than or equals to lines
STEP 4: SET j=lines
STEP 5: REPEAT STEP 6 and 7 UNTIL j is greater than 0
STEP 6: IF j!=i
PRINT j
ELSE
PRINT *
STEP 7: j=j-1
STEP 8: i=i+1
Step 9: EXIT
    '''