import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
house_list = []
chicken_list = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house_list.append((i,j))
        elif row[j] == 2:
            chicken_list.append((i,j))
            row[j] = 0

    graph[i] = row

m_chicken_combinations = combinations(chicken_list, m)
min_city_chicken_dist = int(1e9)
for chicken_comb in m_chicken_combinations:
    # Get chicken distance
    city_chicken_dist = 0
    for house in house_list:
        chicken_dist = int(1e9)
        for i in range(m):
            chicken_dist = min(abs(chicken_comb[i][0] - house[0]) + abs(chicken_comb[i][1] - house[1]), chicken_dist)
        city_chicken_dist += chicken_dist

    min_city_chicken_dist = min(min_city_chicken_dist, city_chicken_dist)

print(min_city_chicken_dist)