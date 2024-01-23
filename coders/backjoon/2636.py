import sys
from collections import deque


def input():
    return sys.stdin.readline()


M, N = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(M)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

cur_left_cheese = sum([sum(row) for row in grid])
T = 0


def bfs():
    q = deque()
    q.append((0, 0))

    visited[0][0] = True

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                if grid[nr][nc] == 1:
                    external_cheese.append((nr, nc))


while cur_left_cheese > 0:
    # print(f"Time = {T}")
    # print(grid)
    # print(cur_left_cheese)
    prev_left_cheese = cur_left_cheese
    visited = [[False] * N for _ in range(M)]
    external_cheese = []
    bfs()

    for che in external_cheese:
        grid[che[0]][che[1]] = 0

    cur_left_cheese = sum([sum(row) for row in grid])

    T += 1

print(T)
print(prev_left_cheese)



