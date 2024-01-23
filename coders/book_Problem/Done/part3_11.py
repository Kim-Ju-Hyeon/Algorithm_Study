'''
뱀
https://www.acmicpc.net/problem/3190
'''

import sys
from collections import deque

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


input = sys.stdin.readline

N = int(input())
K = int(input())

grid = [[0] * N for _ in range(N)]

for _ in range(K):
    apple = list(map(int, input().split()))
    grid[apple[0]-1][apple[1]-1] = 1

L = int(input())
head_direction_list = []
for _ in range(L):
    temp = list(input().split())
    head_direction_list.append([int(temp[0]), temp[1]])


# def solution():
#     snack = deque()
#     x, y = 0, 0
#     snack.append((x, y))
#     head = 'R'
#     time = 0
#
#     for idx in range(L):
#         length, turn = head_direction_list[idx]
#         dx, dy = direction[head][0], direction[head][1]
#         for _ in range(length - time):
#             time += 1
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snack:
#                 snack.append((nx, ny))
#             else:
#                 return time
#
#             if grid[nx][ny] == 1:
#                 grid[nx][ny] = 0
#             else:
#                 snack.popleft()
#
#             x, y = nx, ny
#
#         head = chang_head_direction(head, turn)
#
#     dx, dy = direction[head][0], direction[head][1]
#     while True:
#         time += 1
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snack:
#             snack.append((nx, ny))
#         else:
#             return time
#
#         if grid[nx][ny] == 1:
#             snack.popleft()
#             grid[nx][ny] = 0
#
#         x, y = nx, ny


def solution():
    snack = deque()
    x, y = 0, 0
    snack.append((x, y))
    head = 'R'
    time = 0
    idx = 0

    while True:
        time += 1
        dx, dy = direction[head][0], direction[head][1]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snack:
            snack.append((nx, ny))

            if grid[nx][ny] == 1:
                grid[nx][ny] = 0
            else:
                snack.popleft()

            x, y = nx, ny

            if idx < L and time == head_direction_list[idx][0]:
                head = chang_head_direction(head, head_direction_list[idx][1])
                idx += 1
        else:
            return time





print(solution())
