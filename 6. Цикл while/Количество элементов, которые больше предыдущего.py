prev = int(input())
count = 0
while prev != 0:
    cur = int(input())
    if cur > prev:
        count += 1
    prev = cur
print(count)
