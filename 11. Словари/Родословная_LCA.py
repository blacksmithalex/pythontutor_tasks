def lca(a, b):
    set_a, set_b = set(), set()
    set_a.add(a)
    set_b.add(b)
    while a in d:
        set_a.add(d[a])
        a = d[a]
    while b in d:
        set_b.add(d[b])
        b = d[b]
    return list(set_a & set_b)[0]

d = {}
N = int(input())
for _ in range(N - 1):
    f, s = input().split()
    d[f] = s

K = int(input())
for _ in range(K):
    f, s = input().split()
    print(lca(f, s))