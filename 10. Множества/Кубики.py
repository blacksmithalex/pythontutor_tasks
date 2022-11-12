N, M = [int(x) for x in input().split()]
a, b = set(), set()
for _ in range(N):
    a.add(int(input()))
for _ in range(M):
    b.add(int(input()))

c1, a1, b1 = a & b, a - b,  b - a
for elem in [c1, a1, b1]:
    print(len(elem))
    for x in sorted(elem):
        print(x, end = ' ')
    print()
