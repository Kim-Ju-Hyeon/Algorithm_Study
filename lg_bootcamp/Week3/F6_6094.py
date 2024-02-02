import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    return [['.'] + list(readl().strip()) + ['.'] if 1 <= r <= 12 else ['.'] * 8 for r in range(14)]


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
move2 = [(1, 0), (-1, 0)]

def bfs(r, c, typ):
    q = deque()
    q.append((r, c))
    del_list = [(r, c)]
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()

        for dr, dc in move:
            nr = cur_r + dr
            nc = cur_c + dc

            if not visited[nr][nc] and map_puyo[nr][nc] == typ:
                q.append((nr, nc))
                del_list.append((nr, nc))
                visited[nr][nc] = True

    return del_list


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    R = 12
    C = 6
    map_puyo = input_data()

    total_count = 0
    while True:
        visited = [[False] * 8 for _ in range(14)]
        count = 0
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if not visited[r][c] and map_puyo[r][c] != '.':
                    del_list = bfs(r, c, map_puyo[r][c])

                    if len(del_list) >= 4:
                        count += 1
                        for row, col in del_list:
                            map_puyo[row][col] = -1

        total_count += count
        if count == 0:
            break

        # 터트리기

        break

    print(total_count)

