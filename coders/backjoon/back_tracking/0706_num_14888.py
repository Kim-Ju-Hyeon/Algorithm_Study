'''
https://www.acmicpc.net/problem/14888
'''

N = int(input())
num_list = list(map(int, input().split()))
temp = list(map(int, input().split()))

symbol_list = []
for sym in range(4):
    if sym == 0:
        symbol = '+'
    elif sym == 1:
        symbol = '-'
    elif sym == 2:
        symbol = '*'
    else:
        symbol = '/'

    for _ in range(temp[sym]):
        symbol_list.append(symbol)

used = [False] * len(symbol_list)

stack = []
min_val = int(1e9)
max_val = int(-1e9)


def dfs():
    global max_val, min_val
    if len(stack) == N-1:
        answer = num_list[0]
        for ii, sy in enumerate(stack):
            if sy == '+':
                answer += num_list[ii+1]
            elif sy == '-':
                answer -= num_list[ii+1]
            elif sy == '*':
                answer *= num_list[ii+1]
            else:
                if answer < 0:
                    answer = -(-answer // num_list[ii+1])
                else:
                    answer = answer // num_list[ii+1]

        max_val = max(max_val, answer)
        min_val = min(min_val, answer)
        return

    for idx, sym in enumerate(symbol_list):
        if used[idx]:
           continue

        stack.append(sym)
        used[idx] = True
        dfs()
        stack.pop()
        used[idx] = False


dfs()
print(max_val)
print(min_val)