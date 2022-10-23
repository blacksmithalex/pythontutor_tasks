a = int(input())
prev, count, countM = -1, 1, 1
while a != 0:
    if prev == a:
        count += 1
        if countM < count:
            countM = count
    else:
        if countM < count:
            countM = count
        count = 1
    prev, a = a, int(input())
print(countM)