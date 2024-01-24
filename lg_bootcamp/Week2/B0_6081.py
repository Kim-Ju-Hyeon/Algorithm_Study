import sys


def Input_Data():
    read = sys.stdin.readline
    N, d, k, c = map(int, read().split())
    dish = [int(read()) for _ in range(N)]
    return N, d, k, c, dish


sol = 0
# 입력받는 부분
N, d, k, c, dish = Input_Data()


# 여기서부터 작성
# def solution_1():
#     _dish = dish + dish[:k]
#     max_sushi = -1
#
#     for i in range(N):
#         can_eat = set(_dish[i:i + k])
#         can_eat.add(c)
#
#         max_sushi = max(max_sushi, len(can_eat))
#
#     return max_sushi

def solution_2():
    new_dish = dish + dish[:k]
    check = [0] * (d + 1)
    check[c] = 1
    num_sushi = 1

    for sushi in new_dish[:k]:
        if check[sushi] == 0:
            num_sushi += 1
        check[sushi] += 1

    result = num_sushi

    for l in range(N):
        if check[new_dish[l]] == 1:
            num_sushi -= 1
        check[new_dish[l]] -= 1

        if check[new_dish[l + k]] == 0:
            num_sushi += 1
        check[new_dish[l + k]] += 1

        result = max(result, num_sushi)

    return result


print(solution_2())
