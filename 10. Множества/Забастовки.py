N, K = [int(x) for x in input().split()]
days = set()
for _ in range(K):
    a_i, b_i = [int(x) for x in input().split()]
    d = a_i
    while d <= N:
        if d % 7 != 6 and d % 7 != 0:
            days.add(d)
        d += b_i
print(len(days))