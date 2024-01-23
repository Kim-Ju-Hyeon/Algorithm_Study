N, M = map(int, input().split())


def dfs(start):
    if len(stack) == M:
        print(*stack)
        return

    for num in range(start, N+1):
        stack.append(num)
        dfs(num)
        stack.pop()

stack = []
dfs(1)