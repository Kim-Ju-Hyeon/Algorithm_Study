num_list = {str(num): None for num in range(10)}

string = input()

summation = 0
num_num = 0
answer = []
for l in string:
    if l in num_list:
        summation += int(l)
        num_num += 1
    else:
        answer.append(l)

answer.sort()

if num_num > 0:
    print("".join(answer + [str(summation)]))
else:
    print("".join(answer))