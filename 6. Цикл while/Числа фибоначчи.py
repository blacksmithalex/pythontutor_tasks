n = int(input())
if n == 0:
    print(0)
else:
    prev, cur = 0, 1
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur
    print(cur)
