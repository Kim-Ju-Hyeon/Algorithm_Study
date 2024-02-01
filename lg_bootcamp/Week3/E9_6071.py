import sys
from collections import deque
from heapq import heapify, heappop, heappush


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int, readl().split())) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, r_top, c_top, map_mountine


# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 여기서부터 작성
def solution():
    energy_map = [[1e99] * (N+2) for _ in range(N+2)]

    q = deque()
    q.append((0, 0, 0))
    energy_map[0][0] = 0

    while q:
        cur_r, cur_c, cur_e = q.popleft()

        if cur_e > energy_map[cur_r][cur_c]:
            continue

        for dr, dc in move:
            nr = cur_r + dr
            nc = cur_c + dc

            if nr < 0 or nc < 0 or nr > N + 1 or nc > N + 1:
                continue

            if map_mountine[cur_r][cur_c] == map_mountine[nr][nc]:
                energy = 0

            elif map_mountine[cur_r][cur_c] > map_mountine[nr][nc]:
                energy = abs(map_mountine[cur_r][cur_c] - map_mountine[nr][nc])

            else:
                energy = abs(map_mountine[cur_r][cur_c] - map_mountine[nr][nc]) ** 2

            new_energy = cur_e + energy
            if new_energy >= energy_map[nr][nc]:
                continue

            q.append((nr, nc, new_energy))
            energy_map[nr][nc] = new_energy

    return energy_map[r_top][c_top]


def solution2():
    energy_map = [[1e99] * (N + 2) for _ in range(N + 2)]

    pq = []

    # energy, row, col
    heappush(pq, (0, 0, 0))
    energy_map[0][0] = 0

    while pq:
        cur_energy, cur_r, cur_c = heappop(pq)

        if energy_map[cur_r][cur_c] < cur_energy:
            continue

        if cur_r == r_top and cur_c == c_top:
            return cur_energy

        for dr, dc in move:
            nr = cur_r + dr
            nc = cur_c + dc

            if nr < 0 or nc < 0 or nr > N + 1 or nc > N + 1:
                continue

            if map_mountine[cur_r][cur_c] == map_mountine[nr][nc]:
                energy = 0

            elif map_mountine[cur_r][cur_c] > map_mountine[nr][nc]:
                energy = abs(map_mountine[cur_r][cur_c] - map_mountine[nr][nc])

            else:
                energy = abs(map_mountine[cur_r][cur_c] - map_mountine[nr][nc]) ** 2

            new_energy = cur_energy + energy
            if energy_map[nr][nc] <= new_energy:
                continue

            heappush(pq, (new_energy, nr, nc))
            energy_map[nr][nc] = new_energy

print(solution2())