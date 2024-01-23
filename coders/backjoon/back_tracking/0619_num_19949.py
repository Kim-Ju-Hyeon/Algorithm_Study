'''
https://www.acmicpc.net/problem/19949
'''

answer_list = list(map(int, input().split()))

answer = 0
stack = []


def dfs(correct):
    global answer
    if len(stack) == 10 and correct >= 5:
        answer += 1
        return

    if (10 - len(stack)) < (5 - correct):
        return

    for ans in range(1, 6):
        if len(stack) >= 2 and stack[-2] == stack[-1] and stack[-1] == ans:
            continue

        stack.append(ans)
        if ans == answer_list[len(stack) - 1]:
            dfs(correct + 1)
        else:
            dfs(correct)
        stack.pop()


dfs(0)
print(answer)