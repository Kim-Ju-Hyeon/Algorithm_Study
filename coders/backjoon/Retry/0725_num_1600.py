'''
https://www.acmicpc.net/problem/1600
'''

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

dr = [-1, 1, 0, 0, 2, 2, -1, 1, -2, -2, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 2, 2, -1, 1, -2, -2]


def bfs():
    q = deque()
    q.append((0, 0, 0, 0))
    visited[0][0][0] = True

    while q:
        cr, cc, dist, horse = q.popleft()
        if cr == H - 1 and cc == W - 1:
            return dist

        for i in range(12):
            nr, nc = cr + dr[i], cc + dc[i]

            if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] == 1:
                continue

            if i > 3 and horse < K and not visited[nr][nc][horse+1]:
                q.append((nr, nc, dist + 1, horse + 1))
                visited[nr][nc][horse+1] = True

            elif i <= 3 and not visited[nr][nc][horse]:
                q.append((nr, nc, dist + 1, horse))
                visited[nr][nc][horse] = True

    return -1


print(bfs())
