'''
Sum of n numbers
Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.
Input Format :
Integer n
Output Format :
Sum
Constraints :
1 <= n <= 100
Sample Input :
10
Sample Output :
55
'''
num=int(input( ))
sum=0

for i in range(1, num+1 ):
        sum= sum+ i
print(sum)
