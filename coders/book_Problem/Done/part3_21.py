import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

land = [[] for _ in range(n)]
for i in range(n):
    land[i] = list(map(int, input().split()))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]

    union_list = []
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                q = deque()
                q.append((row, col))
                visited[row][col] = True
                temp = [(row, col)]

                while q:
                    drow, dcol = q.popleft()

                    for i in range(4):
                        nrow = drow + dr[i]
                        ncol = dcol + dc[i]

                        if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and l <= abs(land[drow][dcol] - land[nrow][ncol]) <= r:
                            q.append((nrow, ncol))
                            visited[nrow][ncol] = True
                            temp.append((nrow, ncol))


                if len(temp) > 1:
                    union_list.append(temp)

    if len(union_list) == 0:
        break
    else:
        answer += 1

    for i in range(len(union_list)):
        average_people = 0
        for row, col in union_list[i]:
            average_people += land[row][col]
        average_people = int(average_people / len(union_list[i]))

        for row, col in union_list[i]:
            land[row][col] = average_people

print(answer)