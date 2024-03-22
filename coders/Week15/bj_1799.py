import sys
from copy import deepcopy

def input():
    return sys.stdin.readline()


N = int(input())
chess_map = [list(map(int, input().split())) for _ in range(N)]


def solution():
    answer = [0]
    move = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    def check(r, c, temp_map):
        for direc in range(len(move)):
            cr, cc = r, c
            while True:
                cr += move[direc][0]
                cc += move[direc][1]
                if cr < 0 or cr >= N or cc < 0 or cc >= N: break
                if temp_map[cr][cc] == 3:
                    return False
        return True

    def go(r, c, temp_map):
        temp_map[r][c] = 3
        for direc in range(len(move)):
            cr, cc = r, c
            while True:
                cr += move[direc][0]
                cc += move[direc][1]
                if cr < 0 or cr >= N or cc < 0 or cc >= N: break
                if temp_map[cr][cc] == 1:
                    temp_map[cr][cc] = 2

        return temp_map

    def backtracking(row, col, cmap, count):
        if col == N:
            col = 0
            row += 1
        
        if row == N:
            answer[0] = max(answer[0], count)
            return
        
        if cmap[row][col] == 1 and check(row, col, cmap):
            nmap = go(row, col, deepcopy(cmap))
            backtracking(row, col+1, nmap, count+1)

        backtracking(row, col+1, cmap, count)

    backtracking(0, 0, chess_map, 0)
    print(answer[0])

solution()