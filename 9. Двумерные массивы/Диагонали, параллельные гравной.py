n = int(input())
A = [[abs(i - j) for j in range(n)] for i in range(n)]
for line in A:
    print(*line)