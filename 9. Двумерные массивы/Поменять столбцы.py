def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    return a

n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
i, j = [int(x) for x in input().split()]
swap_columns(a, i, j)
for line in a:
    print(*line)