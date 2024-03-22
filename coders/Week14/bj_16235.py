from collections import deque
import heapq
from copy import deepcopy
import sys

def input():
    return sys.stdin.readline()

N, M, K = map(int, input().split())

land = [[5]*N for _ in range(N)]
add_land = [list(map(int, input().split())) for _ in range(N)]

trees = []
for _ in range(M):
    r, c, age = list(map(int, input().split()))
    heapq.heappush(trees, (age, r-1, c-1))

move = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def solution(trees):
    for _ in range(K):
        # Spring
        temp = []
        dead_trees = []
        while trees:
            age, r, c = heapq.heappop(trees)
            
            if land[r][c] - age < 0:
                dead_trees.append((age, r, c))
            else:
                land[r][c] -= age
                temp.append((age+1, r, c))

        # Summer
        while dead_trees:
            age, r, c = dead_trees.pop()
            land[r][c] += int(age / 2)
        
        # Fall
        trees = temp.copy()
        while temp:
            age, r, c = temp.pop()
            if age % 5 == 0:
                for i in range(8):
                    nr, nc = r + move[i][0], c + move[i][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        trees.append((1, nr, nc))
        heapq.heapify(trees)
        

        # winter
        for r in range(N):
            for c in range(N):
                land[r][c] += add_land[r][c]

    
    return len(trees)


print(solution(trees))