import sys

def input():
    return sys.stdin.readline()


N = int(input())
H = list(map(int, input().split()))


def solution():
    stack = []
    answer = [0] * (len(H)+1)

    for i, h in enumerate(H, 1):
        if not stack:
            stack.append((h, i))

        else:
            while stack and stack[-1][0] < h:
                stack.pop()

            if stack:
                answer[i] = stack[-1][1]
            stack.append((h, i))

    return answer[1:]

print(*solution())
