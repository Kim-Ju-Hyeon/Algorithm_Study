'''
https://www.acmicpc.net/problem/7576
'''

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = [[] for _ in range(N)]
q = deque()
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            q.append((i, j))
    graph[i] = temp


def bfs():
    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            n_row, n_col = cur_r + dx[i], cur_c + dy[i]
            if 0 <= n_row < N and 0 <= n_col < M and graph[n_row][n_col] == 0:
                q.append((n_row, n_col))
                graph[n_row][n_col] += graph[cur_r][cur_c] + 1


def solution():
    answer = 0
    bfs()
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                return -1
            else:
                answer = max(answer, graph[r][c])
    return answer-1


print(solution())
