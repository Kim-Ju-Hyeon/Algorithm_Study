import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    K = int(readl())
    pos = [tuple(map(int, readl().split())) for _ in range(K)]
    L = int(readl())
    cmd_list = [list(readl().split()) for _ in range(L)]

    return N, K, pos, L, cmd_list


# 입력받는 부분
N, K, pos, L, cmd_list = input_data()

direction = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}


def chang_head_direction(head, c):
    if head == 'R':
        if c == 'D':
            new_head = 'D'
        else:
            new_head = 'U'

    elif head == 'U':
        if c == 'D':
            new_head = 'R'
        else:
            new_head = 'L'

    elif head == 'L':
        if c == 'D':
            new_head = 'U'
        else:
            new_head = 'D'

    elif head == 'D':
        if c == 'D':
            new_head = 'L'
        else:
            new_head = 'R'

    return new_head


# 여기서부터 작성
def solution():
    grid = [[-1] + [0] * N + [-1] if 1 <= n <= N else [-1] * (N + 2) for n in range(N + 2)]

    for fr, fc in pos:
        grid[fr][fc] = 1

    cur_c, cur_r = 1, 1
    time = 0
    head = 'R'
    idx = 0

    q = deque()
    q.append((cur_c, cur_r))

    while True:
        time += 1
        nr = cur_r + direction[head][0]
        nc = cur_c + direction[head][1]

        if grid[nr][nc] == -1:
            return time

        if (nr, nc) in q:
            return time

        q.append((nr, nc))
        if grid[nr][nc] == 1:
            grid[nr][nc] = 0
        elif grid[nr][nc] == 0:
            q.popleft()

        if idx < L and time == int(cmd_list[idx][0]):
            head = chang_head_direction(head, cmd_list[idx][1])
            idx += 1

        cur_r, cur_c = nr, nc

print(solution())
