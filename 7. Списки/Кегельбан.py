N, K = [int(x) for x in input().split()]
a = ['I'] * N

for _ in range(K):
    l, r = [int(x) - 1 for x in input().split()]
    a[l:r + 1] = ['.'] * (r - l + 1)
print(''.join(a))