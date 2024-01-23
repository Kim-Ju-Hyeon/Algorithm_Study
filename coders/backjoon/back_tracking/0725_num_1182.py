N, S = map(int, input().split())
num_list = list(map(int, input().split()))
used = [False] * N
answer = 0


def dfs(idx):
    global N, S, answer
    if stack and sum(stack) == S:
        print(stack)
        answer += 1

    if len(stack) == N:
        return

    for ii in range(idx, N):
        if used[ii]:
            continue
        stack.append(num_list[ii])
        used[ii] = True
        dfs(ii)
        stack.pop()
        used[ii] = False


stack = []
dfs(0)
print(answer)
