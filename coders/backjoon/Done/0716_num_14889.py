'''
https://www.acmicpc.net/problem/14889
'''

# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# N = int(input())

# 1. Brute Force by Itertools Combinations
# S = [[] for _ in range(N)]
# for i in range(N):
#     S[i] = list(map(int, input().split()))
#
# player = [n for n in range(N)]
#
# team_member_combination = list(combinations(player, N//2))
#
# answer = int(1e9)
# for start_team in team_member_combination:
#     start_team_score = 0
#     for i in start_team:
#         for j in start_team:
#             start_team_score += S[i][j]
#
#     link_team = [team for team in player if team not in start_team]
#     link_team_score = 0
#     for i in link_team:
#         for j in link_team:
#             link_team_score += S[i][j]
#
#     answer = min(answer, abs(link_team_score-start_team_score))
#
# print(answer)


# 2. Back Tracking + Brute Force
import sys

input = sys.stdin.readline
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]

INF = 2147000000
res = INF


# ✨ DFS
def DFS(L, idx):
    global res
    if L == N // 2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res = min(res, abs(A - B))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(L + 1, i + 1)
            visited[i] = False


DFS(0, 0)
print(res)