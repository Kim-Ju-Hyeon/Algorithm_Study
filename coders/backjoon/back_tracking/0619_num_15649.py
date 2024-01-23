'''
https://www.acmicpc.net/problem/15649

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

import sys


def dfs():
    if len(stack) == M:
        print(*stack)
        return
    for num in range(1, N + 1):
        if not visited[num]:
            stack.append(num)
            visited[num] = True
            dfs()
            stack.pop()
            visited[num] = False


N, M = map(int, input().split())
stack = []
visited = [False] * (N + 1)

dfs()