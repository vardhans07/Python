li= [int(x) for x in input().split()]
targetValue= int(input())
found = False
for i in li:
   if (i==targetValue):
      print(li.index(i))
      found = True
      break
if found is False:
    print("Not Found!")
