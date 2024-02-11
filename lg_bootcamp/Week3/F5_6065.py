import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int,readl().split())) for _ in range(K)]
    return R, C, K, rects


# 입력받는 부분
R, C, K, rects = input_data()

# 여기서부터 작성
def solution():
    visited = [[False] * C for _ in range(R)]
    move = [(1,0), (-1,0), (0,1), (0,-1)]

    grid = [[0] * C for _ in range(R)]
    for left_c, left_r, right_c, right_r in rects:
        for i in range(left_r, right_r):
            for j in range(left_c, right_c):
                grid[i][j] = 1

    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = True
        area = 0

        while q:
            cur_r, cur_c = q.popleft()
            area += 1

            for dr, dc in move:
                nr = cur_r + dr
                nc = cur_c + dc

                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True

        return area

    count = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0 and not visited[r][c]:
                count.append(bfs(r, c))

    count.sort()
    return count


answer = solution()
print(len(answer))
print(*answer)