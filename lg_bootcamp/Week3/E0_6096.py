import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    intvals = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, intvals


# 입력받는 부분
N, M, intvals = Input_Data()

# 여기서부터 작성
def check(distance):
    count = N - 1
    stack = [intvals[0][0]]

    for start, end in intvals:
        loc = stack[-1] + distance

        if loc < start:
            loc = start

        while start <= loc <= end:
            count -= 1
            stack.append(loc)
            loc += distance

            if count == 0:
                return True

    if count > 0:
        return False
    else:
        return True


def solution():
	intvals.sort()
    s = 1
    e = max(intvals, key=lambda x: x[1])[1]
    sol = -1

    while s <= e:
        distance = (s + e) // 2

        if check(distance):
            s = distance + 1
            sol = distance
        else:
            e = distance - 1

    return sol

print(solution())

'''
5 6
2 4
6 8
13 14
15 16
17 18
20 23
'''
