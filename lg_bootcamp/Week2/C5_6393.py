import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    chems = [list(map(int,readl().split())) for _ in range(N)]
    return N, chems

sol = 0

# 입력받는 부분
N, chems = input_data()

# 여기서부터 작성
def solution():
    chems.sort(key=lambda x: x[1] - x[0])
    ref = [chems[0]]

    for s, e in chems[1:]:
        overlap = False
        for i, prev in enumerate(ref):
            if prev[0] <= s <= prev[1] or prev[0] <= e <= prev[1] or s <= prev[0] <= e:
                new_s = max(prev[0], s)
                new_e = min(prev[1], e)

                ref[i] = [new_s, new_e]
                overlap = True
                break

        if not overlap:
            ref.append([s, e])

    return ref

def solution2():
    chems.sort(key=lambda x: x[1])
    ref_list = [chems[0]]
    last_end = chems[0][1]

    for s, e in chems[1:]:
        if last_end <= s:
            last_end = e
            ref_list.append([s,e])
    return ref_list

print(solution2())