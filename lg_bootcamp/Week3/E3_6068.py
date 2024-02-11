import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling


# 입력받는 부분
C, R, sc, sr, map_zergling = Input_Data()

# 여기서부터 작성
def solution(sr, sc):
    zergling = sum([sum([z for z in row]) for row in map_zergling])

    visited = [[False] * (C + 2) for _ in range(R + 2)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    q = deque()
    q.append((sc, sr, 3))
    visited[sc][sr] = True
    zergling -= 1

    while q:
        cur_r, cur_c, time = q.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if not visited[nr][nc] and map_zergling[nr][nc] == 1:
                q.append((nr, nc, time+1))
                visited[nr][nc] = True
                zergling -= 1

    return time, zergling

time, zergling = solution(sc, sr)

print(time)
print(zergling)
