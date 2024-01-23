N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer = set()


def dfs(length):
    global N, M
    if length == M:
        answer.add(tuple(stack))
        return

    for i in range(N):
        stack.append(num_list[i])
        dfs(length + 1)
        stack.pop()


stack = []
dfs(0)
for ans in sorted(list(answer)):
    print(*ans)
