'''
https://www.acmicpc.net/problem/16973
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
H, W, row, col, goal_row, goal_col = map(int, input().split())
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(cr, cc, direction):
    if direction == 0:
        for dc in range(W):
            nr, nc = cr - 1, cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == 1:
                return False

    elif direction == 1:
        cr += H - 1
        for dc in range(W):
            nr, nc = cr + 1, cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == 1:
                return False

    elif direction == 2:
        for dr in range(H):
            nr, nc = cr + dr, cc - 1
            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == 1:
                return False

    else:
        cc += W - 1
        for dr in range(H):
            nr, nc = cr + dr, cc + 1
            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == 1:
                return False

    return True


def bfs():
    q = deque()
    q.append((row-1, col-1, 0))
    visited[row][col] = True

    while q:
        cur_row, cur_col, cur_distance = q.popleft()

        if cur_row == goal_row-1 and cur_col == goal_col-1 and graph[cur_row][cur_col] == 0:
            return cur_distance

        for move in range(4):
            if check(cur_row, cur_col, move):
                new_row, new_col = cur_row + dx[move], cur_col + dy[move]
                if not visited[new_row][new_col]:
                    q.append((new_row, new_col, cur_distance + 1))
                    visited[new_row][new_col] = True
    return -1


print(bfs())
