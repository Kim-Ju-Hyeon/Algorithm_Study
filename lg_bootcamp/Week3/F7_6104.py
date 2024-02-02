import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M, K = map(int,readl().split())
    info = [list(map(int,readl().split()))for _ in range(M)]
    return N, M, K, info

sol = -1
# 입력 받는 부분
N, M, K, info = Input_Data()




def make_edge_list(info):
    edge_list = {city: [] for city in range(1, N+1)}

    for s, e in info:
        edge_list[s].append(e)
        edge_list[e].append(s)

    return edge_list

# 여기서부터 작성
def solution():
    edge_list = make_edge_list(info)
    visited = [False] * (N+1)

    def bfs(c):
        q = deque()
        q.append(c)
        visited[c] = True
        count = 0

        while q:
            _city = q.popleft()
            count += 1

            for to_city in edge_list[_city]:
                if not visited[to_city]:
                    q.append(to_city)
                    visited[to_city] = True
        return count

    group = []
    for city in range(1, N+1):
        if not visited[city]:
            num_city = bfs(city)
            group.append(num_city)


    group.sort(reverse=True)
    return sum(group[:K+1])

print(solution())