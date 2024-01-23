'''
https://www.acmicpc.net/problem/7569
'''

from collections import deque
import sys


def input():
    return sys.stdin.readline()


dh = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]

M, N, H = map(int, input().split())

q = deque()
box = [[] for _ in range(H)]
for h in range(H):
    floor = []
    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            if temp[m] == 1:
                q.append((h, n, m))
        floor.append(temp)
    box[h] = floor

def bfs():
    while q:
        cur_h, cur_row, cur_col = q.popleft()

        for d in range(6):
            nh, nr, nc = cur_h + dh[d], cur_row + dx[d], cur_col + dy[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = box[cur_h][cur_row][cur_col] + 1
                q.append((nh, nr, nc))

def solution():
    bfs()
    answer = 0
    for hh in range(H):
        for nn in range(N):
            for mm in range(M):
                if box[hh][nn][mm] == 0:
                    return -1
                answer = max(answer, box[hh][nn][mm])
    return answer - 1

print(solution())