N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for num in num_list:
        if not stack:
            stack.append(num)
            dfs()
            stack.pop()
        else:
            if stack[-1] < num:
                stack.append(num)
                dfs()
                stack.pop()


stack = []
dfs()