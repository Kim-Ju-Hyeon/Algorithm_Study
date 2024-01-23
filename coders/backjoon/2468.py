import sys
from collections import deque


def input():
    return sys.stdin.readline()


N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(start_r, start_c, visit_list):
    q = deque()
    q.append((start_r, start_c))
    visit_list[start_r][start_c] = True

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visit_list[nr][nc] and grid[nr][nc] > 0:
                q.append((nr, nc))
                visit_list[nr][nc] = True


def solution(N, grid):
    max_land = -1e99
    safe_tile = N * N

    for rain in range(0, 100):
        for r in range(N):
            for c in range(N):
                if grid[r][c] <= rain and grid[r][c] != 0:
                    grid[r][c] = 0
                    safe_tile -= 1

        num_land = 0
        visited = [[False] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if grid[row][col] != 0 and not visited[row][col]:
                    bfs(row, col, visited)
                    num_land += 1

        max_land = max(max_land, num_land)

        if safe_tile == 0:
            return max_land

    return max_land


print(solution(N, grid))
