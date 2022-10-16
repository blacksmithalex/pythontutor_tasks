N = int(input())
a, deg = 1, 0
while a * 2 <= N:
    a *= 2
    deg += 1
print(deg, a)

