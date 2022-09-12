fact = 1
S = 0
n = int(input())
for i in range(1, n + 1):
    fact *= i
    S += fact
print(S)
