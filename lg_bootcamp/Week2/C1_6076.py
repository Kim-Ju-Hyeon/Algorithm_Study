import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, input().split())) for _ in range(N)]
    return N, info


sol = -1
# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
def solution():
    info.sort(key=lambda x: x[1])

    movie_list = []
    for time in info:
        length = time[1] - time[0]
        if length < 2:
            continue
        if len(movie_list) == 0:
            movie_list.append(time)
            continue

        if movie_list[-1][1] <= time[0]:
            movie_list.append(time)

    return len(movie_list)

print(solution())