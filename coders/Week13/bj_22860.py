import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()


N, M = map(int, input().split())

tree = {}
folders = ['main']
for _ in range(N+M):
    p, f, c = input().split()
    if int(c) == 1:
        folders.append(f)
    if p not in tree:
        tree[p] = [(f, int(c))]
    else:
        tree[p].append((f, int(c)))

for folder in folders:
    if folder not in tree:
        tree[folder] = []

Q = int(input())
querys = [input().rstrip() for _ in range(Q)]

def solution():
    def dfs(cur_dir):
        for next_dir in tree[cur_dir]:
            if next_dir[1] == 0:
                count[0] += 1
                files.add(next_dir[0])
            else:
                if len(tree[next_dir[0]]) == 0: continue
                dfs(next_dir[0])

    for q in querys:
        count = [0]
        files = set()

        start = q.split('/')[-1]

        dfs(start)
        print(len(files), count[0])


solution()