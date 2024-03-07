import sys


def input():
    return sys.stdin.readline()


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = [0]
d = [[(0, -1), (1, 0)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]

chk = [[False] * M for _ in range(N)]

def dfs(cur_row, cur_col, cur_sum):
    answer[0] = max(answer[0], cur_sum)

    if cur_col == M:
        cur_row += 1
        cur_col = 0
    
    n_row = cur_row
    n_col = cur_col + 1

    if cur_row == N:
        answer[0] = max(answer[0], cur_sum)
        return

    if not chk[cur_row][cur_col]:
        for i in range(4):
            n = d[i]
            nr_1 = cur_row + n[0][0]
            nc_1 = cur_col + n[0][1]
            nr_2 = cur_row + n[1][0]
            nc_2 = cur_col + n[1][1]

            if nr_1 < 0 or nr_1 >= N: continue
            if nc_1 < 0 or nc_1 >= M: continue
            if nr_2 < 0 or nr_2 >= N: continue
            if nc_2 < 0 or nc_2 >= M: continue

            if chk[nr_1][nc_1]: continue
            if chk[nr_2][nc_2]: continue

            new_sum = 2 * grid[cur_row][cur_col] + grid[nr_1][nc_1] + grid[nr_2][nc_2]

            chk[cur_row][cur_col] = True
            chk[nr_1][nc_1] = True
            chk[nr_2][nc_2] = True

            dfs(n_row, n_col, cur_sum + new_sum)

            chk[cur_row][cur_col] = False
            chk[nr_1][nc_1] = False
            chk[nr_2][nc_2] = False

    dfs(n_row, n_col, cur_sum)


dfs(0, 0, 0)
print(answer[0])
