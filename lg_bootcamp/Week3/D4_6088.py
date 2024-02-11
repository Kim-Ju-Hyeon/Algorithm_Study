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


def solution_2(list_height):
    stack = deque()
    max_area = 0
    for i, h in enumerate(list_height):
        n = i
        while stack and stack[-1][1] >= h:
            n = stack[-1][0]
            max_area = max(max_area, (i - n) * stack[-1][1])
            stack.pop()
        stack.append((n, h))

    while stack:
        max_area = max(max_area, (len(list_height) - stack[-1][0]) * stack[-1][1])
        stack.pop()
        
    return max_area


while 1:
    # 입력받는 부분
    N, list_height = Input_data()
    if N == 0: break
    print(solution_2(list_height))
