N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))


def dfs(length, ii):
    if length == M:
        print(*stack)
        return

    for idx, num in enumerate(num_list[ii:]):
        stack.append(num)
        dfs(length + 1, idx + ii)
        stack.pop()


stack = []
dfs(0, 0)
