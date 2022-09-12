N = int(input())
S1, S2 = 0, 0
for _ in range(N - 1):
    S1 += int(input())
for i in range(1, N + 1):
    S2 += i

print(S2 - S1)
