import sys
from collections import deque


def input():
    return sys.stdin.readline()


n, T = map(int, input().split())
x_y = [list(map(int, input().split())) for _ in range(n)]

answer = 1e99


def solution_1():
    global answer
    visited = [False] * n

    def dfs(x, y, t):
        global answer
        if y >= T:
            answer = min(answer, t)
            return True

        if t >= answer:
            return False

        for i, next_xy in enumerate(x_y):
            if not visited[i] and abs(x - next_xy[0]) <= 2 and abs(y - next_xy[1]) <= 2:
                visited[i] = True
                if dfs(next_xy[0], next_xy[1], t + 1):
                    return True
                visited[i] = False

    dfs(0, 0, 0)
    if answer == 1e99:
        answer = -1

    return answer


def solution_2():
    q = deque()
    distance = [1e99] * (n+1)

    q.append((0, 0, 0, 0)) # x, y, idx, step
    distance[0] = 0

    while q:
        cur_x, cur_y, cur_idx, cur_t = q.popleft()

        if distance[cur_idx] < cur_t:
            continue

        if cur_y >= T:
            return cur_t

        for i, next_xy in enumerate(x_y, 1):
            if distance[i] <= cur_t:
                continue

            if abs(cur_x - next_xy[0]) <= 2 and abs(cur_y - next_xy[1]) <= 2:
                q.append((next_xy[0], next_xy[1], i, cur_t + 1))

    return -1

print(solution_2())