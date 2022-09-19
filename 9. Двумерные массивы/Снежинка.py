n = int(input())
A = [['.'] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            A[i][j] = '*'
        elif i == j or i + j == n - 1:
            A[i][j] = '*'
for line in A:
    print(*line)