M, indM, i = 0, 0, 0
a = int(input())
while a != 0:
    if a > M:
        M, indM = a, i
    a = int(input())
    i += 1
print(indM)
