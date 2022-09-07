n = int(input())
m = int(input())
k = int(input())

if k % n == 0 and 1 <= k // n <= m - 1:
    print('YES')
elif k % m == 0 and 1 <= k // m <= n - 1:
    print('YES')
else:
    print('NO')