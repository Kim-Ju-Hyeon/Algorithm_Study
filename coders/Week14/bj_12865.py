import sys

def input():
    return sys.stdin.readline()

N, K = map(int, input().split())
W_V = [list(map(int, input().split())) for _ in range(N)]


def solution():
    W_V.sort()
    answer = [0]
    def dfs(start, cur_w, cur_v):
        answer[0] = max(answer[0], cur_v)
        
        for i in range(start, N):
            if cur_w + W_V[i][0] <= K:
                dfs(i + 1, cur_w + W_V[i][0], cur_v + W_V[i][1])
            else:
                return
            
    dfs(0, 0, 0)

    return answer[0]

print(solution())