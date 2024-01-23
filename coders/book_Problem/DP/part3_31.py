import sys

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''

input = sys.stdin.readline

dxdy = [(-1, -1), (0, -1), (1, -1)]

test_num = int(input())

for _ in range(test_num):
    N, M = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    input_graph = list(map(int, input().split()))

    idx = 0
    for i in range(N):
        for j in range(M):
            graph[i][j] = input_graph[idx]
            idx += 1

    print(graph)

    for col in range(1, M):
        for row in range(N):
            max_gold = 0
            for i in range(3):
                n_row, n_col = row + dxdy[i][0], col + dxdy[i][1]
                if 0 <= n_row < N and 0 <= n_col < M:
                    max_gold = max(max_gold, graph[n_row][n_col])
            graph[row][col] += max_gold

    answer = 0
    for idx in range(N):
        answer = max(answer, graph[idx][-1])
    print(answer)
