def height(x):
    if x not in d:
        return 0
    return 1 + height(d[x])

N = int(input())
d = {} #ребенок - родитель
alls = set() #множество всех уникальных людей

for _ in range(N - 1):
    f, s = input().split() #f - ребенок, s - родитель
    d[f] = s
    alls.add(f)
    alls.add(s)

for x in sorted(alls):
    print(x, height(x))
