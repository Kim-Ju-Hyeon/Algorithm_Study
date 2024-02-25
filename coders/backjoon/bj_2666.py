import sys

def input():
    return sys.stdin.readline()

def Input_Data():
    N = int(input())
    A, B = map(int, input().split())
    S = int(input())
    seq = [int(input()) for _ in range(S)]
    return N, A, B, S, seq

N, A, B, S, seq = Input_Data()

sol = []
def dfs(s, left, right, sum_move):
    if s == S:
        sol.append(sum_move)
        return

    dfs(s + 1, seq[s], right, sum_move + abs(left - seq[s]))
    dfs(s + 1, left, seq[s], sum_move + abs(right - seq[s]))

dfs(0, min(A, B), max(A, B), 0)
print(min(sol))


sol = [1e99]
def solution(s, left, right, sum_move):
    if sum_move >= s:
        return

    if s == s:
        sol[0] = sum_move
        return

    if seq[s] < right:
        solution(s + 1, seq[s], right, sum_move + abs(left - seq[s]))
    if left < seq[s]:
        solution(s + 1, left, seq[s], sum_move + abs(right - seq[s]))