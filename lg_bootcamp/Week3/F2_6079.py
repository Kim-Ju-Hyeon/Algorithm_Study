import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, edges


# 입력받는 부분
N, M, edges = Input_Data()


# 여기서부터 작성
def get_route(prev_field):
    route = [N]
    node = N
    while node > 1:
        route.append(prev_field[node])
        node = prev_field[node]
    return route[::-1]


def get_min_distance(field, field_distance):
    distance = [1e99] * (N + 1)
    prev_field = [0] * (N + 1)

    q = deque()
    q.append((1, 0))
    distance[1] = 0

    while q:
        cur_field, cur_dist = q.popleft()

        if distance[cur_field] < cur_dist:
            continue

        for next_field in field[cur_field]:
            next_dist = field_distance[cur_field][next_field]
            new_dist = cur_dist + next_dist

            if distance[next_field] <= new_dist:
                continue

            q.append((next_field, new_dist))
            distance[next_field] = new_dist
            prev_field[next_field] = cur_field

    min_distance = distance[N]
    route = get_route(prev_field)

    return min_distance, route


def solution():
    field = {}
    field_distance = [[1e99] * (N + 1) for _ in range(N + 1)]

    for start, end, dist in edges:
        if start in field:
            field[start].append(end)
        else:
            field[start] = [end]
        field_distance[start][end] = dist

        if end in field:
            field[end].append(start)
        else:
            field[end] = [start]
        field_distance[end][start] = dist

    original_min_distance, route = get_min_distance(field, field_distance)

    new_min_distance = 0
    for idx in range(len(route) - 1):
        start, end = route[idx], route[idx + 1]

        field_distance[start][end] *= 2
        field_distance[end][start] *= 2

        min_distance, _ = get_min_distance(field, field_distance)
        new_min_distance = max(new_min_distance, min_distance)

        field_distance[start][end] *= 0.5
        field_distance[end][start] *= 0.5

    return int(new_min_distance - original_min_distance)


print(solution())
