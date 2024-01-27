import sys

def input():
    return sys.stdin.readline()

n = int(input())
mine_map = [list(input().rstrip()) for _ in range(n)]
show_map = [list(input().rstrip()) for _ in range(n)]


def solution():
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, 1, -1, 1, -1]

    for r in range(n):
        for c in range(n):
            if show_map[r][c] == 'x' and mine_map[r][c] == '.':
                count = 0
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n and mine_map[nr][nc] == '*':
                        count += 1

                show_map[r][c] = count

            elif show_map[r][c] == 'x' and mine_map[r][c] == '*':
                for row in range(n):
                    for col in range(n):
                        if mine_map[row][col] == '*':
                            show_map[row][col] = '*'


solution()

for row in range(n):
    for col in range(n):
        print(show_map[row][col], end='')
    print()

