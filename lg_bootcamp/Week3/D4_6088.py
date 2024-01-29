import sys
from collections import deque

'''
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
'''
def Input_data():
    readl = sys.stdin.readline
    N, *list_height = map(int, readl().split())
    return N, list_height


def make_grid(ncol, heights):
    grid = [[0] * ncol for _ in range(max(heights))]

    for col in range(N):
        for row in range(heights[col]):
            if row == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = grid[row - 1][col] + 1

    return grid


def solution_1(N, list_height):
    grid = make_grid(N, list_height)
    max_area = 0

    for row in range(len(grid)):
        for sc in range(N):
            if grid[row][sc] == 0:
                continue
            height = 1e99
            for ec in range(sc, N):
                height = min(height, grid[row][ec])
                if height == 0:
                    break
                area = height * (ec - sc + 1)
                max_area = max(max_area, area)

    return max_area


def solution_2(list_height):
    stack = deque()
    max_area = 0
    prev_idx = 0
    for i, h in enumerate(list_height):
        prev_idx = i
        while stack and stack[-1][1] >= h:
            prev_idx, prev_h = stack.pop()
            area = (i - prev_idx) * prev_h
            max_area = max(max_area, area)
        else:
            stack.append((prev_idx, h))

    while stack:
        prev_idx, prev_h = stack.pop()
        area = (len(list_height) - prev_idx) * prev_h
        max_area = max(max_area, area)

    return max_area


while 1:
    # 입력받는 부분
    N, list_height = Input_data()
    if N == 0: break
    print(solution_2(list_height))
