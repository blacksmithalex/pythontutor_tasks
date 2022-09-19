n, m = [int(x) for x in input().split()]
A = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            A[i][j] = '*'
for line in A:
    print(*line)