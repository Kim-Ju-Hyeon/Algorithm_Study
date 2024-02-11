import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    A, B, C, D = map(int, readl().split())
    return A, B, C, D


# 입력 받는 부분
A, B, C, D = Input_Data()

# 여기서부터 작성
answer = [1e99]
memo = [[False] * (B + 1) for _ in range(A + 1)]


def dfs(cur_A, cur_B, count):
    if memo[cur_A][cur_B]:
        return
    else:
        memo[cur_A][cur_B] = True

    if count >= answer[0]:
        return

    if cur_A == C and cur_B == D:
        answer[0] = min(answer[0], count)

    # F(A)
    if cur_A < A:
        dfs(A, cur_B, count + 1)
    # F(B)
    if cur_B < B:
        dfs(cur_A, B, count + 1)

    # E(A)
    if cur_A > 0:
        dfs(0, cur_B, count + 1)
    # E(B)
    if cur_B > 0:
        dfs(cur_A, 0, count + 1)

    # M(B,A)
    if 0 <= cur_A < A:
        if cur_B < A - cur_A:
            dfs(cur_A + cur_B, 0, count + 1)
        else:
            dfs(A, cur_B - (A - cur_A), count + 1)
    # M(A,B)
    if 0 <= cur_B < B:
        if cur_A < B - cur_B:
            dfs(0, cur_A + cur_B, count + 1)
        else:
            dfs(cur_A - (B - cur_B), B, count + 1)


def bfs():
    q = deque()
    q.append((0, 0, 0))
    memo[0][0] = True

    while q:
        cur_a, cur_b, cur_count = q.popleft()

        if cur_a == C and cur_b == D:
            return cur_count

        if not memo[A][cur_b]:
            q.append((A, cur_b, cur_count + 1))
            memo[A][cur_b] = True

        if not memo[cur_a][B]:
            q.append((cur_a, B, cur_count + 1))
            memo[cur_a][B] = True

        if not memo[0][cur_b]:
            q.append((0, cur_b, cur_count + 1))
            memo[0][cur_b] = True
        if not memo[cur_a][0]:
            q.append((cur_a, 0, cur_count + 1))
            memo[cur_a][0] = True

        if not memo[max(0, cur_a - (B - cur_b))][min(B, cur_b + cur_a)]:
            q.append((max(0, cur_a - (B - cur_b)), min(B, cur_b + cur_a), cur_count + 1))
            memo[max(0, cur_a - (B - cur_b))][min(B, cur_b + cur_a)] = True

        if not memo[min(A, cur_a + cur_b)][max(0, cur_b - (A - cur_a))]:
            q.append((min(A, cur_a + cur_b), max(0, cur_b - (A - cur_a)), cur_count + 1))
            memo[min(A, cur_a + cur_b)][max(0, cur_b - (A - cur_a))] = True

    return -1


print(bfs())
