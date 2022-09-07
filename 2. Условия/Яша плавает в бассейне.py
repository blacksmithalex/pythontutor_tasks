N = int(input())
M = int(input())
x = int(input())
y = int(input())

N, M = min(N, M), max(N, M)
R = min(x, y, M - y, N - x)
print(R)

