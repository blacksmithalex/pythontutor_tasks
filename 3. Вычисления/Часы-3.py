a = float(input())

h = int(a / 30)
a = a - h * 30
m = int(2 * a)
a = a - m / 2
s = int(120 * a)

print(h, m, s)