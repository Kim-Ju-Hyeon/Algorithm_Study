import sys


def input_data():
    A, N = map(int, readl().split())
    W = list(map(int, readl().split()))
    return A, N, W


readl = sys.stdin.readline
T = int(readl())
for t in range(1, T + 1):
    # 입력받는 부분
    A, N, W = input_data()
    answer = [N]

    W.sort()

    def dfs(idx, cur_A, cur_skill):
        if cur_A == 1:
            return

        if cur_skill > answer[0]:
            return

        if idx == N:
            answer[0] = min(answer[0], cur_skill)
            return

        if W[idx] < cur_A:
            dfs(idx + 1, cur_A + W[idx], cur_skill)
        else:
            # 생성
            dfs(idx, cur_A + (cur_A - 1), cur_skill + 1)

            # 제거
            dfs(N, cur_A, cur_skill + N - idx)



    dfs(0, A, 0)
    print(f'Case #{t}: {answer[0]}')
