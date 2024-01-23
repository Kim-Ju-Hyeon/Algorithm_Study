N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer = set()


def dfs(length, idx):
    global N, M
    if length == M:
        answer.add(tuple(stack))
        return

    for i in range(idx, N):
        stack.append(num_list[i])
        dfs(length + 1, i)
        stack.pop()


stack = []
dfs(0, 0)
for ans in sorted(list(answer)):
    print(*ans)