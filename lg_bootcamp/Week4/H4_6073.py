import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus


# 입력받는 부분
N, M, relation, bonus = input_data()
sol = [0] * N


# 여기서부터 작성
def solution():
    tree_dict = {node: 0 for node in range(1, N + 1)}
    relation.sort()
    bonus.sort(reverse=True)

    edge_list = {node: [] for node in range(1, N + 1)}
    for from_node, to_node in relation:
        edge_list[from_node].append(to_node)
        tree_dict[to_node] += 1

    distance = [-1e99] * (N + 1)

    def bfs():
        q = deque()
        q.append((1, 0))
        distance[1] = 0

        while q:
            cur_node, cur_distance = q.popleft()

            if cur_distance < distance[cur_node]:
                continue

            for next_node in edge_list[cur_node]:
                ndist = cur_distance + 1
                if distance[next_node] >= ndist:
                    continue
                q.append((next_node, ndist))
                distance[next_node] = ndist

    bfs()
    order = [(dist, len(edge_list[i]), i) for i, dist in enumerate(distance[1:], 1)]
    order.sort(key=lambda x: (x[0], x[1], x[2]))
    idx = 0
    for dist, _, i in order:
        sol[i - 1] = bonus[idx]
        idx += 1

    print(*sol)


def solution2():
    sol = [-1] * (N + 1)
    chk = [False] * N
    bonus.sort(reverse=True)

    edge_list = {node: [] for node in range(1, N + 1)}
    for from_node, to_node in relation:
        edge_list[from_node].append(to_node)