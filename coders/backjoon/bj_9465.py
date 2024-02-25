import sys


def input():
    return sys.stdin.readline()

def dfs(node, iter):
    visited[node] = True
    cycle[node] = iter
    team.append(node)
    next_node = wanted_list[node]

    if not visited[next_node]:
        dfs(next_node, iter+1)
    else:
        if next_node in cycle:
            result.append(team[cycle[next_node]:])
        return


T = int(input())
for _ in range(T):
    N = int(input())
    wanted_list = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    result = []

    for start_node in range(1, N+1):
        if not visited[start_node]:
            cycle = {}
            team = []
            iter = 0
            dfs(start_node, iter)
            print(result)

    count = sum([len(_team) for _team in result])

    print(N - count)