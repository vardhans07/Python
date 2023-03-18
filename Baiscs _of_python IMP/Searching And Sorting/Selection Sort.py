
def selectionSort(arr, size):
 for step in range(size):
  minimum = step
  for i in range(step + 1, size):                        # to sort in descending order, change > to < in this line
    if arr[i] < arr[minimum]:                            # select the minimum element in each loop
     minimum = i                                 #   if you give write if arr[i] > arr[minimum]: o/p=[20, 15, 12, 10, 2]

  (arr[step], arr[minimum]) = (arr[minimum], arr[step])  # Swap

input = [20, 12, 10, 15, 2]
size = len(input)
selectionSort(input, size)
print('suiiiiiii_Sorted Array in Ascending Order is: ') #nahi lihile tari chalel
print(input)

'''
Selection sort is an algorithm that selects the smallest element from an unsorted list in
each iteration and places that element at the beginning of the unsorted list. The detailed
algorithm is given below.
● Consider the given unsorted array to be:
● Set the first element as minimum.
● Compare minimum with the second element. If the second element is smaller than
minimum, assign the second element as minimum.
● Compare minimum with the third element. Again, if the third element is smaller, then
assign minimum to the third element otherwise do nothing. The process goes on until
the last element.
4
● After each iteration, minimum is placed in the front of the unsorted list.
● For each iteration, indexing starts from the first unsorted element. These steps are
repeated until all the elements are placed at their correct positions.
First Iteration
5
Second Iteration:
Third Iteration
6
Fourth Iteration
'''