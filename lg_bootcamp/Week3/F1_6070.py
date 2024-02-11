import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    P = int(readl())
    infos = [(lambda x: [x[0], x[1], int(x[2])])(readl().split()) for _ in range(P)]
    return P, infos


P, infos = Input_Data()


def solution():
    edge_list = {}
    cow = set()

    for start, end, distance in infos:
        if start in edge_list:
            edge_list[start].append((end, distance))
        else:
            edge_list[start] = [(end, distance)]

        if end in edge_list:
            edge_list[end].append((start, distance))
        else:
            edge_list[end] = [(start, distance)]

        if start.upper() == start:
            if start != 'Z':
                cow.add(start)
        if end.upper() == end:
            if end != 'Z':
                cow.add(end)

    cow = list(cow)

    distance = {from_f: {to_f: 1e99 if from_f != to_f else 0 for to_f in edge_list.keys()} for from_f in cow}

    q = deque([(c, c, distance[c][c]) for c in cow])

    while q:
        _cow, cur_farm, cur_dist = q.popleft()

        if distance[_cow][cur_farm] < cur_dist:
            continue

        for next_farm, dist in edge_list[cur_farm]:
            new_dist = cur_dist + dist

            if distance[_cow][next_farm] <= new_dist:
                continue

            q.append((_cow, next_farm, new_dist))
            distance[_cow][next_farm] = new_dist

    sol = 1e99
    best_cow = None
    for c in cow:
        if sol > distance[c]['Z']:
            sol = distance[c]['Z']
            best_cow = c

    return best_cow, sol


print(*solution())
