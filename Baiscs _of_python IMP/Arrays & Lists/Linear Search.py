li= [int(x) for x in input().split()] #Taking list as user input
targetValue= int(input())
found = False #Boolean value to check if we found the targetValue
for i in li:
    if (i==targetValue): #If we found the targetValue
     print(li.index(i)) #Print the index

     found = True
     break

if found is False:#If we did not find the targetValue
     print('Not_Found_Suiiiiiiii')

'''
   i/p = 1 2 4 67 23 12
  2nd  i/p =   4
       output= 2
'''
