import sys


def input_data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input

# 입력받는 부분
str_input = input_data()


# 여기서부터 작성
def solution():
    check = []
    count = 0
    for char in str_input:
       if char == '(':
           count += 1
       else:
           count -= 1
       check.append(count)

    sol = 0
    if check[-1] < 0:
        for i, char in enumerate(str_input):
            if check[i] < 0:
                sol += 1
                break
            if char == ')':
               sol += 1

    elif check[-1] > 0:
        for i, char in enumerate(str_input[::-1]):
            i = len(str_input) - i - 1
            if check[i] - 2 < 0:
                break

            if char == '(':
                sol += 1

    return sol

print(solution())

