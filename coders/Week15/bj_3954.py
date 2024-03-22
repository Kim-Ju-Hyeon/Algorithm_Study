import sys

def input():
    return sys.stdin.readline()

T = int(input())


def solution():
    for _ in range(T):
        sm, sc, si = map(int, input().split())
        program = input()
        input_string = input()

        loop = {}
        stack = []
        for i, command in enumerate(program):
            print(command)
            if command == '[':
                stack.append(i)
            elif command == ']':
                open = stack.pop()
                loop[open] = i
        
        print(loop)

solution()
