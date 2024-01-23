import sys
from itertools import combinations
import copy

input = sys.stdin.readline

n = int(input())

grid = [[] for _ in range(n)]
obstacle = []
teacher = []
for i in range(n):
    row = input().split()

    for j in range(n):
        if row[j] == 'X':
            obstacle.append((i, j))
        elif row[j] == 'T':
            teacher.append((i, j))

    grid[i] = row

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_student(graph, x, y, d):
    n = len(graph)
    if x < 0 or y < 0 or x >= n or y >= n or graph[x][y] == 'O':
        return False

    elif graph[x][y] == 'S':
        return True

    else:
        nx = x + dx[d]
        ny = y + dy[d]
        return find_student(graph, nx, ny, d)

def good_hide(graph):
    for t in teacher:
        for ii in range(4):
            if find_student(graph, t[0], t[1], ii):
                return False

    return True


def solution():
    obstacle_combinations = combinations(obstacle, 3)

    for comb in obstacle_combinations:
        temp = copy.deepcopy(grid)
        for obs in comb:
            temp[obs[0]][obs[1]] = 'O'

        if good_hide(temp):
            return 'YES'

    return 'NO'


print(solution())