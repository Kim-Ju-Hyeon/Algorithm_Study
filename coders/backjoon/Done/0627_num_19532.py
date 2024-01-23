coeff = list(map(int, input().split()))

a = coeff[0]
b = coeff[1]
c = coeff[2]
d = coeff[3]
e = coeff[4]
f = coeff[5]

det = a*e - b*d

x = (c*e - b*f) / det
y = (a*f - c*d) / det

print(round(x), round(y))