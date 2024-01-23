N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
used = [False] * N


def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for idx, num in enumerate(num_list):
        if not used[idx]:
            stack.append(num)
            used[idx] = True
            dfs()
            stack.pop()
            used[idx] = False


stack = []
dfs()