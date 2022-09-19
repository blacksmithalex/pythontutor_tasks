n, m = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n)]
iM, jM, M = 0, 0, -1e10
for i in range(n):
    for j in range(m):
        if A[i][j] > M:
            M = A[i][j]
            iM, jM = i, j
print(iM, jM)


