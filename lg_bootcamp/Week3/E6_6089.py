import sys
from collections import deque
from copy import deepcopy


def Input_Data():
    R, C = map(int,readl().split())
    map_forest = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    return R,C,map_forest


move = [(0,1), (0,-1), (1,0), (-1,0)]


def solution(R, C, map_forest):
    rain = []
    for row in range(1, R+1):
        for col in range(1, C+1):
            if map_forest[row][col] == 'S':
                S = (row, col)
                map_forest[row][col] = '.'
            elif map_forest[row][col] == '*':
                rain.append((row, col))

    visited = [[False] * (C+2) for _ in range(R+2)]

    q = deque()
    q.append((S[0], S[1], rain, 0, deepcopy(map_forest)))
    visited[S[0]][S[1]] = True

    while q:
        cur_row, cur_col, cur_rain, cur_dist, cur_map = q.popleft()

        new_rain = []
        for cr, cc in cur_rain:
            for dr, dc in move:
                nr = cr + dr
                nc = cc + dc

                if cur_map[nr][nc] == 0: continue
                if cur_map[nr][nc] == '.':
                    cur_map[nr][nc] = '*'
                    new_rain.append((nr, nc))

        for dr, dc in move:
            nrow = cur_row + dr
            ncol = cur_col + dc

            if cur_map[nrow][ncol] == 0: continue # 외각 이면 X
            if visited[nrow][ncol]: continue # 방문했었으면 No
            if cur_map[nrow][ncol] == 'X': continue # 바위 지역이면 X
            if cur_map[nrow][ncol] == '*': continue # 홍수 지역이면 X
            if cur_map[nrow][ncol] == 'D': return cur_dist + 1

            q.append((nrow, ncol, new_rain, cur_dist+1, deepcopy(cur_map)))
            visited[nrow][ncol] = True
            cur_map[nrow][ncol] = '.'

    return "KAKTUS"



readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    R, C, map_forest = Input_Data()
    # 여기서부터 작성
    print(solution(R, C, map_forest))