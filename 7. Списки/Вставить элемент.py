a = [int(x) for x in input().split()]
k, C = [int(x) for x in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(*a)