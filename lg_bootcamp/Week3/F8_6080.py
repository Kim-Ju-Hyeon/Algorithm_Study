import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_field = [[0] + list(map(int, readl().split())) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_field


# 입력받는 부분
N, map_field = Input_Data()
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check(D):
    visited = [[False] * (N+2) for _ in range(N+2)]

    def bfs(row, col, D):
        q = deque()
        q.append((row, col))
        visited[row][col] = True
        count = 0

        while q:
            c_row, c_col = q.popleft()
            count += 1

            if count == round(N * N / 2):
                return True

            for dr, dc in move:
                nr = c_row + dr
                nc = c_col + dc

                diff = abs(map_field[c_row][c_col] - map_field[nr][nc])
                if 1 <= nr < N + 1 and 1 <= nc < N + 1 and diff <= D and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

        return False

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if not visited[r][c]:
                if bfs(r, c, D):
                    return True

    return False


def solution():
    s = 0
    e = max([max(row) for row in map_field])
    answer = 0

    while s <= e:
        D = (s + e) // 2
        if check(D):
            answer = D
            e = D - 1
        else:
            s = D + 1

    return answer


print(solution())
