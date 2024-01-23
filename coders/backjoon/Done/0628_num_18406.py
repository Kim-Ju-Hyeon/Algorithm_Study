N = int(input())

N = str(N)
length = len(N)

front = N[:length//2]
back = N[length//2:]

f = 0
b = 0
for i in range(length//2):
    f += int(front[i])
    b += int(back[i])

if f == b:
    print("LUCKY")
else:
    print("READY")