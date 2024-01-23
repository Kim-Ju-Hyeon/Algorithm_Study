'''
https://www.acmicpc.net/problem/2636
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

cheese = True
cheese_list = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


time = 0
while cheese:
    num_cheese = 0
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                num_cheese += 1

    if num_cheese == 0:
        break

    cheese_list.append(num_cheese)

    visited = [[False] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if (row == 0 or row == N-1 or col == 0 or col == M-1) and not visited[row][col] and graph[row][col] != 1:
                q = deque()
                q.append((row, col))
                visited[row][col] = True
                graph[row][col] = 2

                while q:
                    cn, cc = q.popleft()

                    for i in range(4):
                        nn, nc = cn + dx[i], cc + dy[i]


                        if 0 <= nn < N and 0 <= nc < M and not visited[nn][nc] and graph[nn][nc] != 1:
                            q.append((nn, nc))
                            visited[nn][nc] = True
                            graph[nn][nc] = 2

    visited = [[False] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1 and not visited[row][col]:
                q = deque()
                q.append((row,col))
                visited[row][col] = True

                while q:
                    cn, cc = q.popleft()

                    for i in range(4):
                        nn, nc = cn + dx[i], cc + dy[i]

                        if nn < 0 or nn >= N or nc < 0 or nc >= M:
                            continue

                        if not visited[nn][nc]:
                            if graph[nn][nc] == 2:
                                graph[cn][cc] = 2

                            elif graph[nn][nc] == 1:
                                q.append((nn, nc))
                                visited[nn][nc] = True

    time += 1
print(time)
print(cheese_list[-1])
