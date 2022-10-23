count, M = 0, 0
a = int(input())
while a != 0:
    if a > M:
        M, count = a, 1
    elif a == M:
        count += 1
    a = int(input())
print(count)
