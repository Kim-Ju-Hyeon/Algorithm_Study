import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline()


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# move = [(1, -1), (1, 0), (1, 1)]
# def solution():
#     distance = [[1e99]*M for _ in range(N)]

#     def dijikstra(col):
#         pq = []
#         heappush(pq, (grid[0][col], 0, col, -1))
#         distance[0][col] = grid[0][col]

#         while pq:
#             cur_d, cur_r, cur_c, prev_d = heappop(pq)

#             if cur_r >= N-1:
#                 return cur_d
            
#             if distance[cur_r][cur_c] < cur_d: continue
            
#             for i in range(3):
#                 nr = cur_r + move[i][0]
#                 nc = cur_c + move[i][1]
                

#                 if prev_d != i and 0 <= nr < N and 0 <= nc < M and distance[nr][nc] >= cur_d + grid[nr][nc]:
#                     heappush(pq, (cur_d + grid[nr][nc], nr, nc, i))
#                     distance[nr][nc] = cur_d + grid[nr][nc]
#         return 1e99

#     answer = 1e99
#     for col in range(M):
#         answer = min(answer, dijikstra(col))

#     return answer

# print(solution())

move = [(-1, -1), (-1, 0), (-1, 1)]

def solution():
    dp = [[1e99] * M for _ in range(N)]
    dp[0] = grid[0]
    prev_dir = [9] * M

    for row in range(1, N):
        for col in range(M):
            for i in range(3):
                if prev_dir[col] == i: continue
                pr = row + move[i][0]
                pc = col + move[i][1]

                if 0 <= pr < N and 0 <= pc < M:
                    if dp[row][col] > grid[row][col] + dp[pr][pc]:
                        dp[row][col] = grid[row][col]+dp[pr][pc]
                        prev_dir[col] = i
        print(prev_dir)

    print(min(dp[-1]))

solution()