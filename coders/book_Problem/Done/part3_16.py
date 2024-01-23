import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [[] for _ in range(N)]
virus_loc = {}
can_make_wall = []
for i in range(N):
    row = list(map(int, input().split()))
    grid[i] = row
    for j, n in enumerate(row):
        if n == 2:
            virus_loc[(i, j)] = None
        elif n == 0:
            can_make_wall.append((i, j))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(_grid, _visited, x, y):
    _visited[x][y] = True

    if _grid[x][y] == 1:
        return

    elif _grid[x][y] == 0:
        _grid[x][y] = 2

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M and not _visited[nx][ny]:
            dfs(_grid, _visited, nx, ny)


answer = -1
for wall_combination in combinations(can_make_wall, 3):
    visited = [[False] * M for _ in range(N)]
    safe_zone = 0

    for make_wall in wall_combination:
        grid[make_wall[0]][make_wall[1]] = 1

    for virus in virus_loc:
        dfs(grid, visited, virus[0], virus[1])

    for row in range(N):
        for col in range(M):
            if grid[row][col] == 0:
                safe_zone += 1

            elif grid[row][col] == 2 and (row, col) not in virus_loc:
                grid[row][col] = 0

    for make_wall in wall_combination:
        grid[make_wall[0]][make_wall[1]] = 0

    answer = max(answer, safe_zone)

print(answer)
