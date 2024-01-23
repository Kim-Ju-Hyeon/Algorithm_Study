'''
https://www.acmicpc.net/problem/7576
'''


import sys
from collections import deque

def input():
    return sys.stdin.readline()

M, N = map(int, input().split())

box = []
q = deque()
visited = [[False] * M for _ in range(N)]

space = N*M
for row in range(N):
    temp = list(map(int, input().split()))
    for col, c in enumerate(temp):
        if c == 1:
            q.append((row, col, 0))
            visited[row][col] = True
            space -= 1

        if c == -1:
            visited[row][col] = True
            space -= 1

    box.append(temp)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
cur_time = 0

def bfs():
    global space, cur_time

    while q:
        cur_row, cur_col, cur_time = q.popleft()

        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and box[nr][nc] == 0:
                q.append((nr, nc, cur_time+1))
                visited[nr][nc] = True
                space -= 1

    if space == 0:
        return cur_time
    else:
        return -1

print(bfs())