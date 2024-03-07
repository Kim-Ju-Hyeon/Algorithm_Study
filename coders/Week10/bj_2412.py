import sys
from collections import deque


def input():
    return sys.stdin.readline()


n, T = map(int, input().split())
dot = {}
for _ in range(n):
    x, y = map(int, input().split())
    dot[(x, y)] = False


def solution_3():
    q = deque()
    q.append((0, 0, 0))

    while q:
        cur_x, cur_y, cur_step = q.popleft()

        if cur_y >= T:
            return cur_step
        
        for nx in range(cur_x-2, cur_x+3):
            for ny in range(cur_y-2, cur_y+3):
                if (nx, ny) in dot and not dot[(nx, ny)]:
                    q.append((nx, ny, cur_step + 1))
                    dot[(nx, ny)] = True
        
    return -1

print(solution_3())
