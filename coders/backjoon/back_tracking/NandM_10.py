N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
used = [False] * N
answer_dict = {}


def dfs(length, idx):
    global N, M

    if length == M:
        key = str(stack)
        if key not in answer_dict:
            print(*stack)
            answer_dict[key] = None

        return

    for ii, num in enumerate(num_list[idx:]):
        if used[ii + idx]:
            continue

        stack.append(num)
        used[ii + idx] = True
        dfs(length + 1, ii + idx)
        stack.pop()
        used[ii + idx] = False


stack = []
dfs(0, 0)