import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()


N = int(input())
tree = {}
for _ in range(N):
    parent, left_child, right_child = list(map(int, input().split()))
    tree[parent] = [left_child, right_child]

def solution():
    count = [0, 0]
    visited = [False] * (N+1)
    
    def dfs(cur_node):
        if tree[cur_node][0] != -1 and not visited[tree[cur_node][0]]:
            dfs(tree[cur_node][0])
            count[0] += 1

        if tree[cur_node][1] != -1 and not visited[tree[cur_node][1]]:
            dfs(tree[cur_node][1])
            count[0] += 1

    def dfs_right(cur_node):
        if tree[cur_node][1] != -1 and not visited[tree[cur_node][1]]:
            dfs_right(tree[cur_node][1])
            count[1] += 1

    visited[1] = True
    dfs(1)
    dfs_right(1)

    print(2*count[0] - count[1])

solution()