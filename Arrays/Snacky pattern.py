s_tmp = input("Enter s =")
n_tmp = input("num in row=")
s = s_tmp
n = int(n_tmp)
snake = []
number = 0
k = 0
for i in range(n):
    snake.append([])

for i in range(len(s)):
    number += k
    if number == 0:
        k = 1
    elif number == n-1:
        k = -1
    snake[number].append(s[i])
for i in range(n):
    for j in range(len(snake[i])):
        print(snake[i][j], end='')
    print()