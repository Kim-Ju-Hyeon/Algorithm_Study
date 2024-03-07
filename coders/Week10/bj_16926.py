import sys
from collections import deque


def input():
    return sys.stdin.readline()


N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]


def solution():
    iteration = min(N, M) // 2

    for i in range(iteration):
        q = deque()

        row, col = i, i

        # case 1 - 위쪽
        for c in range(col, M - col):
            q.append(array[row][c])

        # case 2 - 오른쪽
        for r in range(row + 1, N - row):
            q.append(array[r][M - 1 - col])

        # case 3 - 아래
        for c in range(M - col - 1, col - 1, -1):
            q.append(array[N - 1 - row][c])

        # case 4 - 왼쪽
        for r in range(N - row - 2, row, -1):
            q.append(array[r][col])

        # 회전
        for _ in range(R):
            q.appendleft(q.pop())

        # 다시 배열에 채우기
        for c in range(col, M - col):
            array[row][c] = q.popleft()

        for r in range(row + 1, N - row):
            array[r][M - 1 - col] = q.popleft()

        for c in range(M - col - 1, col - 1, -1):
            array[N - 1 - row][c] = q.popleft()

        for r in range(N - row - 2, row, -1):
            array[r][col] = q.popleft()

    for row in array:
        print(' '.join(map(str, row)))


solution()
