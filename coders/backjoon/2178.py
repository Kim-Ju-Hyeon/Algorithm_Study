'''
https://www.acmicpc.net/problem/2178
'''

from collections import deque

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(row, col):
    q = deque()
    q.append((row, col, 1))
    visited[row][col] = True

    while q:
        cur_row, cur_col, step = q.popleft()

        if cur_row == N-1 and cur_col == M-1:
            return step

        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] == 1:
                q.append((nr, nc, step+1))
                visited[nr][nc] = True

    return -1

print(bfs(0, 0))