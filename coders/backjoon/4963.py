import sys
from collections import deque

def input():
    return sys.stdin.readline()

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 1 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True


while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break

    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    visited = [[False]*W for _ in range(H)]

    ans = 0
    for sx in range(H):
        for sy in range(W):
            if grid[sx][sy] == 1 and not visited[sx][sy]:
                bfs(sx, sy)
                ans += 1

    print(ans)

