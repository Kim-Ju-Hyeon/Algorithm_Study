import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_uv = [list(map(int, readl().strip())) for _ in range(N)]
    return N, map_uv


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
def solution():
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    distance = [[1e99]*N for _ in range(N)]

    q = deque()
    q.append((0, 0, map_uv[0][0]))
    distance[0][0] = map_uv[0][0]

    while q:
        cur_r, cur_c, cur_dist = q.popleft()
        if distance[cur_r][cur_c] < cur_dist:
            continue

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                ndist = cur_dist + map_uv[nr][nc]

                if ndist >= distance[nr][nc]:
                    continue

                distance[nr][nc] = ndist
                q.append((nr, nc, ndist))

    return distance[N-1][N-1]

print(solution())
