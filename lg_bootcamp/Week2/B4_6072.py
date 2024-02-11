import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    edges = [list(map(int, readl().split())) for _ in range(6)]
    return K, edges


# 입력받는 부분
K, edges = Input_Data()

# 여기서부터 작성
shape_dict = {
    'type1': [2, 3, 1, 3, 1, 4],
    'type2': [2, 3, 1, 4, 1, 4],
    'type3': [2, 4, 2, 3, 1, 4],
    'type4': [2, 3, 2, 3, 1, 4]
}

land_dict = {
    'type1': [(0, 5), (2, 3)],
    'type2': [(0, 1), (3, 4)],
    'type3': [(3, 4), (0, 1)],
    'type4': [(4, 5), (1, 2)]
}


def check_shape():
    edge_list = [0] * 4
    for edge, _ in edges:
        edge_list[edge - 1] += 1

    shape = ''
    for n in edge_list:
        shape += str(n)

    if shape == '2121':
        return "type1"
    elif shape == '2112':
        return 'type2'
    elif shape == '1212':
        return 'type3'
    elif shape == '1221':
        return 'type4'


def make_order(_type):
    _shape = shape_dict[_type]

    q = deque(edges)
    while True:
        for idx in range((len(_shape))):
            if _shape[idx] != q[idx][0]:
                q.rotate(-1)
                break
        else:
            return q


def Solve():
    _type = check_shape()
    new_edges = make_order(_type)
    total_land_idx, delete_land_idx = land_dict[_type]

    total_land = new_edges[total_land_idx[0]][1] * new_edges[total_land_idx[1]][1]
    delete_land = new_edges[delete_land_idx[0]][1] * new_edges[delete_land_idx[1]][1]

    used_land = total_land - delete_land

    return used_land * K



def Solve2():
    max_h, max_h_idx = -1, -1
    max_v, max_v_idx = -1, -1

    for idx, edge in enumerate(edges):
        if edge[0] == 1 or edge[0] == 2:
            if edge[1] > max_h:
                max_h = edge[1]
                max_h_idx = idx
        else:
            if edge[1] > max_v:
                max_v = edge[1]
                max_v_idx = idx

    delete_h_left = max_h_idx - 1
    delete_h_right = (max_h_idx + 1) % 6
    dh = abs(edges[delete_h_right][1] - edges[delete_h_left][1])

    delete_v_left = max_v_idx - 1
    delete_v_right = (max_v_idx + 1) % 6
    dv = abs(edges[delete_v_right][1] - edges[delete_v_left][1])

    total_land = max_v * max_h
    delete_land = dh * dv

    return K * (total_land - delete_land)


print(Solve())
print(Solve2())