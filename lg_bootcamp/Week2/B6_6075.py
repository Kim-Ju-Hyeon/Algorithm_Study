import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = 0

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
grid = [[0 for _ in range(101)] for _ in range(101)]
visited = [[False] * 101 for _ in range(101)]
length = [0]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < 101 and 0 <= nc < 101:
                if grid[nr][nc] == 1:
                    if not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True

                else:
                    length[0] += 1


for y, x in info:
    for l in range(10):
        grid[x + l][y] = 1
        for ll in range(10):
            grid[x + l][y + ll] = 1

for rr in range(101):
    for cc in range(101):
        if grid[rr][cc] == 1 and not visited[rr][cc]:
            bfs(rr, cc)

# 출력하는 부분
print(length[0])
