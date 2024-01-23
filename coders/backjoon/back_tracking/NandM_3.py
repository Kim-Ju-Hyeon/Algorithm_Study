'''
https://www.acmicpc.net/problem/15651
'''

N, M = map(int, input().split())

def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for num in range(1, N+1):
        stack.append(num)
        dfs()
        stack.pop()

stack = []
dfs()
