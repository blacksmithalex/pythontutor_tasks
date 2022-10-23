M, sM = 0, 0
a = int(input())
while a != 0:
    if a > M:
        M, sM = a, M
    elif a > sM:
        sM = a
    a = int(input())
print(sM)
