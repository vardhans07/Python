# fakt yachyat change kela ahe arrays list pn in this program little bug as foolows
'''
Mother Father Daughter 10, 23
10
Not_Found_Suiiiiiiii
'''
# above we can see if we give integer number give us wrong output

li= [x for x in input().split()]                #Taking list as user input
targetValue= input()
found = False                                   #Boolean value to check if we found the targetValue
for i in li:
    if (i==targetValue):                        #If we found the targetValue
     print(li.index(i))                          #Print the index

     found = True
     break

if found is False:                              #If we did not find the targetValue
     print('Not_Found_Suiiiiiiii')

'''
   i/p = Mother Father Daughter 10, 23
  2nd  i/p =  Daughter
       output= 2
'''
