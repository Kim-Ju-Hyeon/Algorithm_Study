import sys
from collections import deque

def input():
    return sys.stdin.readline()


N, M, T = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))



def bfs1(N, M, T, grid):
    visited = [[False] * M for _ in range(N)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True

    while q:
        cur_r, cur_c, dist = q.popleft()

        if grid[cur_r][cur_c] == 2:
            return dist + (N + M - cur_c - cur_r - 2)

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] != 1:
                    q.append((nr, nc, dist + 1))
                    visited[nr][nc] = True

    return T + 1


def solution(N, M, T, grid):
    visited = [[False] * M for _ in range(N)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True

    while q:
        cur_r, cur_c, dist = q.popleft()

        if cur_r == N-1 and cur_c == M-1:
            if dist > T:
                return T + 1
            else:
                return dist

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] != 1:
                    q.append((nr, nc, dist+1))
                    visited[nr][nc] = True

    return T + 1

gram = bfs1(N, M, T, grid)
result = solution(N, M, T, grid)

result = min(gram, result)

if result <= T:
    print(result)
else:
    print('Fail')

'''
3 3 100
0 0 2
1 1 1
0 0 0
'''
