'''
https://www.acmicpc.net/problem/9663
'''

N = int(input())

used_col = [False] * N

stack = []
answer = 0


def check_diagonal(row, col):
    if len(stack) > 0:
        for prev_row, prev_col in stack:
            if abs(prev_row - row) == abs(prev_col - col):
                return False

    return True

def dfs(row):
    print(stack)
    global answer
    if len(stack) == N:
        answer += 1
        return

    for col in range(N):
        if used_col[col]:
            continue

        if check_diagonal(row, col):
            stack.append([row, col])
            used_col[col] = True
            dfs(row+1)
            stack.pop()
            used_col[col] = False

dfs(0)
print(answer)