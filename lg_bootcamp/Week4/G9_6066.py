import sys


def input_data():
    readl = sys.stdin.readline
    return [list(map(int, readl().split())) for _ in range(9)]


# 입력받는 부분

# 여기서부터 작성
def init_check_pos():
    pos = []
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                pos.append((row, col))
            else:
                row_chk[row][sudoku[row][col]] = True
                col_chk[col][sudoku[row][col]] = True
                small_box_chk[row // 3][col // 3][sudoku[row][col]] = True
    return pos

def dfs(n):
    if n >= len(pos):
        return True

    for num in range(1, 10):
        if row_chk[pos[n][0]][num]: continue
        if col_chk[pos[n][1]][num]: continue
        if small_box_chk[pos[n][0]//3][pos[n][1]//3][num]: continue

        sudoku[pos[n][0]][pos[n][1]] = num
        row_chk[pos[n][0]][num] = True
        col_chk[pos[n][1]][num] = True
        small_box_chk[pos[n][0] // 3][pos[n][1] // 3][num] = True

        if dfs(n+1):
            return True

        sudoku[pos[n][0]][pos[n][1]] = 0
        row_chk[pos[n][0]][num] = False
        col_chk[pos[n][1]][num] = False
        small_box_chk[pos[n][0] // 3][pos[n][1] // 3][num] = False

    return False

sudoku = input_data()

row_chk = [[False] * 10 for _ in range(9)]
col_chk = [[False] * 10 for _ in range(9)]
small_box_chk = [[[False] * 10 for _ in range(3)] for _ in range(3)]

pos = init_check_pos()

dfs(0)
for row in sudoku:
    print(*row)