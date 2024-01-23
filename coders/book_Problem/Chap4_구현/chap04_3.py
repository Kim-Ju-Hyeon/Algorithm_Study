start = input()

y = start[0]
x = int(start[1])

count = 0

if y == 'a':
    y = 1
elif y == 'b':
    y = 2
elif y == 'c':
    y = 3
elif y == 'd':
    y = 4
elif y == 'e':
    y = 5
elif y == 'f':
    y = 6
elif y == 'g':
    y = 7
elif y == 'h':
    y = 8

dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -2, 1, -1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue

    count += 1

print(count)
