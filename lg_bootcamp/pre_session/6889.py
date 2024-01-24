import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


# 입력 받는 부분
N, M = Input_Data()

# 여기서부터 작성
num_list = [False] * 6

# M = 1
def dice_1(stack):
    if len(stack) == N:
        print(*stack)
        return

    for d in range(1, 7):
        stack.append(d)
        dice_1(stack)
        stack.pop()


def dice_2(stack, start):
    if len(stack) == N:
        print(*stack)
        return

    for d in range(start, 7):
        stack.append(d)
        dice_2(stack, d)
        stack.pop()



def dice_3(stack):
    if len(stack) == N:
        print(*stack)
        return

    for d in range(1, 7):
        if not num_list[d-1]:
            stack.append(d)
            num_list[d - 1] = True

            dice_3(stack)

            stack.pop()
            num_list[d-1] = False


stack = []

if M == 1:
    dice_1(stack)

elif M == 2:
    dice_2(stack, 1)

else:
    dice_3(stack)
