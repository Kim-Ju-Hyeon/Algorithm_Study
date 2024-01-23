'''
https://www.acmicpc.net/problem/2583
'''

import sys
from collections import deque

def input():
    return sys.stdin.readline()

M, N, K = map(int, input().split())

grid = [[0]*N for _ in range(M)]
for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int,input().split())
    for x in range(x_1, x_2):
        for y in range(y_1, y_2):
            grid[M-1-y][x] = 1


visited = [[False] * N for _ in range(M)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(row, col):
    q = deque()
    q.append((row,col))
    land = 1
    visited[row][col] = True

    while q:
        cur_row, cur_col = q.popleft()

        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]

            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == 0:
                q.append((nr, nc))
                land += 1
                visited[nr][nc] = True

    return land

answer = []
for r in range(M):
    for c in range(N):
        if grid[r][c] == 0 and not visited[r][c]:
            answer.append(bfs(r, c))

print(len(answer))
print(*sorted(answer))

