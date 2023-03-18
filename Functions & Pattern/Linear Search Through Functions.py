def linearSearch(li,targetValue):
    for i in li:
        if (i == targetValue):                          # If we found the targetValue
            return li.index(i)                          # Return the index
            return -1                                   # If not found, return -1
li = [int(x) for x in input().split()]                 # Taking list as user input
targetValue = int(input())                              # User input for targetValue
print(linearSearch(li, targetValue))