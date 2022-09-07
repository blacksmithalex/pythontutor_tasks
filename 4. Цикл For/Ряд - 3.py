A = int(input())
B = int(input())

for n in range(A - 1 + A % 2, B - 1, -2):
    print(n, end=' ')
