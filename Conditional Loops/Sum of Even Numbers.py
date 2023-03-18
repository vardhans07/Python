'''
Sum of Even Numbers
Given a number N, print sum of all even numbers from 1 to N.
Input Format :
Integer N
Output Format :
Required Sum
Sample Input 1 :
 6
Sample Output 1 :
12

'''
number = int(input("Give Input Range:"))
i= 2
Sum = 0
while i <= number:
      Sum += i
      i += 2
print(Sum)