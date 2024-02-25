import sys


def input():
    return sys.stdin.readline()


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = [0]
d = [[(0, -1), (1, 0)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]

chk = [[False] * M for _ in range(N)]

def dfs(cur_sum):
    answer[0] = max(answer[0], cur_sum)
    for row in range(N):
        for col in range(M):
            if not chk[row][col]:
                for i in range(4):
                    n = d[i]
                    nr_1 = row + n[0][0]
                    nc_1 = col + n[0][1]
                    nr_2 = row + n[1][0]
                    nc_2 = col + n[1][1]

                    if nr_1 < 0 or nr_1 >= N: continue
                    if nc_1 < 0 or nc_1 >= M: continue
                    if nr_2 < 0 or nr_2 >= N: continue
                    if nc_2 < 0 or nc_2 >= M: continue

                    if chk[nr_1][nc_1]: continue
                    if chk[nr_2][nc_2]: continue

                    new_sum = 2 * grid[row][col] + grid[nr_1][nc_1] + grid[nr_2][nc_2]

                    cur_sum += new_sum
                    chk[row][col] = True
                    chk[nr_1][nc_1] = True
                    chk[nr_2][nc_2] = True

                    dfs(cur_sum)

                    cur_sum -= new_sum
                    chk[row][col] = False
                    chk[nr_1][nc_1] = False
                    chk[nr_2][nc_2] = False

dfs(0)
print(answer[0])
