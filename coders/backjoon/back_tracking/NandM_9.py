N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
used = [False] * N
answer_dict = {}


def dfs(length):
    if length == M:
        key = str(stack)
        if key not in answer_dict:
            print(*stack)
            answer_dict[key] = None

        return

    for ii, num in enumerate(num_list):
        if used[ii]:
            continue

        stack.append(num)
        used[ii] = True
        dfs(length + 1)
        stack.pop()
        used[ii] = False


stack = []
dfs(0)
