n, m = map(int, input().split())
x, y, d = map(int, input().split())

visited = [[False] * m for _ in range(n)]

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

visited[x][y] = True
counts = 1
check = 0

move = {0: (-1, 0),
        1: (0, 1),
        2: (+1, 0),
        3: (0, -1)}

while True:
    for _ in range(4):
        d = (d + 3) % 4

        nx = x + move[d][0]
        ny = y + move[d][1]

        if n > nx >= 0 and m > ny >= 0 and maps[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny
            visited[x][y] = True
            counts += 1
            check = 0
            break
        else:
            check += 1

    if check == 4:
        _d = (d + 2) % 4
        nx = x + move[_d][0]
        ny = y + move[_d][1]

        if maps[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        check = 0

print(counts)
