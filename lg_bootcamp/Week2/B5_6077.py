import sys


def Input_Data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input


sol = 0

# 입력받는 부분
str_input = Input_Data()


# 여기서부터 작성
def Solve(str_input):
    change = 0
    while len(str_input) > 0:
        stack = []
        temp = [True] * len(str_input)

        for idx, l in enumerate(str_input):
            if l == '(':
                stack.append((l, idx))
            else:
                if len(stack) == 0:
                    continue
                _, d = stack.pop()
                temp[d] = False
                temp[idx] = False

        str_input = [ll for ii, ll in enumerate(str_input) if temp[ii] == True]
        str_input = ''.join(str_input)

        if len(str_input) == 0:
            return change

        # 남아 있는 괄호가 전부 ( 이면 그냥 나누기 2
        if set(str_input) == {'('}:
            change += len(str_input) // 2
            return change

        # 첫 번째 괄호가 닫는 괄호면 바꿔주고 change += 1
        if str_input[0] == ')':
            str_input = '(' + str_input[1:]
            change += 1

    return change

def solve2():
    check = 0
    change = 0

    for char in str_input:
        if char == '(':
            check += 1
        else:
            check -= 1

        if check < 0:
            change += 1
            check = 1

    change += (check // 2)
    return change

print(solve2())
