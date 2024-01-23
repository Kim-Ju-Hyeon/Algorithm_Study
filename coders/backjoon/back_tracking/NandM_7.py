N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()

def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for num in num_list:
        stack.append(num)
        dfs()
        stack.pop()

stack = []
dfs()