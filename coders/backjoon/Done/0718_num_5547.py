'''
https://www.acmicpc.net/problem/5547
'''

import sys
from collections import deque

input = sys.stdin.readline

W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[False] * W for _ in range(H)]


def check_inside(yy, xx):
    q = deque()
    q.append((yy, xx))
    visited[yy][xx] = True
    graph[yy][xx] = 2

    while q:
        cur_yy, cur_xx = q.popleft()
        if (cur_yy + 1) % 2 == 0:
            dy = [-1, 0, +1, +1, 0, -1]
            dx = [-1, -1, -1, 0, +1, 0]
        else:
            dy = [-1, 0, +1, +1, 0, -1]
            dx = [0, -1, 0, +1, +1, +1]

        for ii in range(6):
            nyy, nxx = cur_yy + dy[ii], cur_xx + dx[ii]

            if nyy < 0 or nyy >= H or nxx < 0 or nxx >= W:
                continue

            if graph[nyy][nxx] == 0 and not visited[nyy][nxx]:
                q.append((nyy, nxx))
                visited[nyy][nxx] = True
                graph[nyy][nxx] = 2

for y in range(H):
    for x in range(W):
        if (y == 0 or y == H-1 or x == 0 or x == W-1) and graph[y][x] == 0 and not visited[y][x]:
            check_inside(y,x)


answer = 0
for y in range(H):
    for x in range(W):
        if graph[y][x] == 1 and not visited[y][x]:
            q = deque()
            q.append((y,x))
            visited[y][x] = True

            while q:
                cur_y, cur_x = q.popleft()
                if (cur_y + 1) % 2 == 0:
                    dy = [-1, 0, +1, +1, 0, -1]
                    dx = [-1, -1, -1, 0, +1, 0]
                else:
                    dy = [-1, 0, +1, +1, 0, -1]
                    dx = [0, -1, 0, +1, +1, +1]

                wall = 6
                for i in range(6):
                    ny, nx = cur_y + dy[i], cur_x + dx[i]

                    if 0 <= ny < H and 0 <= nx < W:
                        if graph[ny][nx] == 1 or graph[ny][nx] == 0:
                            wall -= 1

                        if graph[ny][nx] == 1 and not visited[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = True

                answer += wall
print(answer)
