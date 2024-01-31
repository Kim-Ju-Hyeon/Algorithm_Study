import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_game = [readl().strip() for _ in range(R)]
    return R, C, map_game

T = int(input())

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(R, C, map_game):
    visited = [[[False] * C for _ in range(R)] for _ in range(2)]

    q = deque()
    for row in range(R):
        for col in range(C):
            if map_game[row][col] == 'R':
                red = (row, col)
            elif map_game[row][col] == 'B':
                blue = (row, col)


    q.append((red, blue, 0))
    visited[0][red[0]][red[1]] = True
    visited[1][blue[0]][blue[1]] = True

    while q:
        print(q)
        cur_red, cur_blue, cur_try = q.popleft()
        if cur_try > 9:
            continue

        for dr, dc in move:
            nred_r = cur_red[0] + dr
            nred_c = cur_red[1] + dc

            nblue_r = cur_blue[0] + dr
            nblue_c = cur_blue[1] + dc

            if map_game[nred_r][nred_c] == '#':
                nred = (cur_red[0], cur_red[1])

            elif map_game[nred_r][nred_c] == 'H':
                return cur_try + 1

            else: # map_game[nred_r][nred_c] == '.':
                nred = (nred_r, nred_c)

            if map_game[nblue_r][nblue_c] == '#':
                nblue = (cur_blue[0], cur_blue[1])

            elif map_game[nblue_r][nblue_c] == 'H':
                continue

            else: # map_game[nblue_r][nblue_c] == '.':
                nblue = (nblue_r, nblue_c)

            # 지낫던 곳이면 Pass
            if visited[0][nred[0]][nred[1]] and visited[1][nblue[0]][nblue[1]]:
                continue

            # 파랑 공이랑 빨간공이 같은 위치로 움직이면 X
            if nblue[0] == nred[0] and nblue[1] == nred[1]:
                continue

            q.append((nred, nblue, cur_try+1))
            visited[0][nred[0]][nred[1]] = True
            visited[1][nblue[0]][nblue[1]] = True

    return -1


for t in range(T):
    # 입력받는 부분
    R, C, map_game = Input_Data()
    print(solution(R, C, map_game))