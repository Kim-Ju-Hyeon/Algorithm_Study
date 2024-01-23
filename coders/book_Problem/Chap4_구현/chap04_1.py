n = int(input())
plan = list(map(str, input().split()))

x, y = 1, 1
move = {"U": [-1, 0],
        "D": [+1, 0],
        "R": [0, +1],
        "L": [0, -1]}

for i in range(len(plan)):
    dx = move[plan[i]][0]
    dy = move[plan[i]][1]

    new_x = x + dx
    new_y = y + dy

    if new_x > n or new_x <= 0 or new_y > n or new_y <= 0:
        continue

    x, y = new_x, new_y

print(x, y)